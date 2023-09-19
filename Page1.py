import streamlit as st 
import pandas as pd
import sqlite3
from AddROOMStoDB import AddROOMStoDB

floors = ['Ground', 'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Nineth', 'Tenth']   

depts = ['Accident and Emergency', 'Operating Department', 'Maternity Department', 'Diagnostic Department',
        'In-patient accomodation', 'Renal', 'Critical Care Area', 'Adult Mental illness accomodation',
        'Adult acute day care accomodation', 'Day patient accommodation', 'Fracture clinic',
        'Oral surgery, orthodontic department', 'Out-patient department', 'Sterile Services Dpartment']

rooms = ['Resuscitation Room', 'Major Treatment Room(Emergency)', 'Plaster Room(Emergency)', 
         'Post anaesthsia Recovery Room(Emergency)', 'Treatment Room(Emergency)', 'Anesthetic Rooms(all OT)', 
         'Operating Room(Ortho)', 'Operating Room(Neuro)', 'Operating Room(General)', 'Post Anesthesia Recovery(OT)', 
         'Equipment Service Room(OT)', 'LDRP(Mother)', 'LDRP(Baby)', 'Operating suite Anesthetist(Maternity)',
         'Operating suite Pediatrician(Maternity)', 'Post Anesthesia Recovery Room(Maternity)', 
         'Equipment Service Room(Maternity)', 'Neonatal Unit(Maternity)', 'Single Bedroom In Patient(Maternity)', 
         'Multi Bedroom In Patient(Maternity)', 'Nursery(Maternity)', 'Special Procedure Room(Diagnostic)', 
         'Anaesthic Room(Diagnostic)', 'Holding and recovery Room', 'Ultrasound Room', 'Fluroscopy Room', 
         'Urography Room', 'Tomography Room', 'MRI Room', 'CAT Room', 'Angiography Room', 'Endoscopy Room', 
         'Lineac bunkers Room', 'General Purpose Room', 'In Patient-single Bedroom', 'In Patient-multi Bedroom', 
         'Treatment Room(In Patient)', 'Dialysis Renal Room', 'Critical Care Area', 'Equipment Service Room(Critical Care)', 
         'Coronory Care Unit(CCU)', 'High Dependency Unit(HDU)', 'Burns Unit', 'Electro-Convulsive Therapy(ECT)', 
         'Post anesthesia Recovery(Adult mental)', 'Single Bedroom(Day Patient)', 'Multi Bedroom(Day Patient)', 
         'Treatment Room(Day Patient)', 'Endoscopy Room (Day Patient)', 'Plaster Room(Fracture)', 
         'Treatment Room(Adult Acute Day Care)', 'Post Anesthesia Recovery(Adult Acute Day Care)', 
         'Treatment Room/Cubicles(Out-Patient)', 'Sterile Services', 'IAP(Sterile)', 
         'Consulting/treatment type 1(Orthodontic)', 'Consulting/treatment type 2/3(Orthodontic)', 
         'Consulting/treatment type 1(Oral Surgery)', 'Consulting/treatment type 2/3(Oral Surgery)']


def add_records(project):
    conn = sqlite3.connect('Database.db')
    
    floor = st.selectbox('Choose the floor', floors, key=1)
    
    col1,col2 = st.columns(2)
    with col1:
        dept = st.selectbox('Department', depts, key=2)
    with col2:
        subcol1,subcol2 = st.columns(2)
        with subcol1:
            if dept:
                dept_AVSU = st.number_input("Dept AVSU Set(s)", min_value=0, max_value=5, value=1)
        with subcol2:
            AVSU_gas_placeholder = st.container()
      
    room = st.selectbox('Select the Room', [''] + sorted(rooms), key=3)
     
    with AVSU_gas_placeholder:
            gas_df = pd.read_sql_query('''SELECT O2_unit,N2O_unit,N2O_O2_unit,MA4_unit,SA7_unit,VAC_unit,
                                                 He_O2_unit,CO2_unit
                                          FROM Medical_rooms
                                          WHERE project_id = (SELECT project_id 
                                                               FROM Projects 
                                                               WHERE project_name=?)
                                          AND floor = ? AND dept = ?
                                       ''', conn, params = (project,floor,dept)) 

            o2_check = (gas_df['O2_unit'] != 0).any() if not gas_df.empty else None
            n2o_check = (gas_df['N2O_unit'] != 0).any() if not gas_df.empty else None 
            n2o_o2_check = (gas_df['N2O_O2_unit'] != 0).any() if not gas_df.empty else None 
            ma4_check = (gas_df['MA4_unit'] != 0).any() if not gas_df.empty else None 
            sa7_check = (gas_df['SA7_unit'] != 0).any() if not gas_df.empty else None 
            vac_check = (gas_df['VAC_unit'] != 0).any() if not gas_df.empty else None
            he_o2_check = (gas_df['He_O2_unit'] != 0).any() if not gas_df.empty else None 
            co2_check = (gas_df['CO2_unit'] != 0).any() if not gas_df.empty else None 

            check = [o2_check,n2o_check,n2o_o2_check,ma4_check,sa7_check,vac_check,he_o2_check,co2_check]
            dept_gascount = str(check.count(True))
            dept_AVSU = 'None' if dept_AVSU == 0 else str(dept_AVSU) + ' Set' 
            st.write('')
            st.info(dept_gascount + 'G AVSU')
        
    if floor != '' and dept!='' and room != '': 
        AddROOMStoDB(project, dept, dept_AVSU, floor, room)
        
    conn.close()  

def new_project():
    projname = st.text_input('', label_visibility = 'collapsed', placeholder = 'Project Name')
    projloc = st.text_input('', label_visibility = 'collapsed', placeholder = "Project Location")

    if st.button('Add Project'):
        if projname and projloc:
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()
            cursor.execute('SELECT project_name FROM Projects')
            projects = cursor.fetchall()
            projlist = [item[0] for item in projects]
            if projname in projlist:
                st.error('Project Already Added')
            else:    
                cursor.execute('INSERT INTO Projects (project_name, project_location) VALUES (?, ?)', (projname, projloc))
                conn.commit()
                conn.close()
                st.success('Project Added')
        elif projname and not projloc:
            st.error("Please Enter the Project location")
        else:
            st.error("Please Enter a Project name")      
    
def del_records(): 
    conn = sqlite3.connect('Database.db')
    projects_df = pd.read_sql_query('''SELECT DISTINCT(project_name) FROM Projects''', conn) 

    if projects_df.empty:
        st.error('No Projects in Database, Add a New Project')
    else:    
        project = st.selectbox('Select Project to Delete', [''] + projects_df['project_name'].tolist(), key=5)        
        if project != '':
            delete_project = st.checkbox('Click to Delete all Data of '+ '**' + project + '**', key=10)
            if delete_project and st.button('Press to confirm'):
                cursor = conn.cursor()
                cursor.execute(''' DELETE FROM Medical_rooms
                                   WHERE project_id IN ( SELECT project_id FROM Projects WHERE project_name = ?)''', (project,))
                cursor.execute(''' DELETE FROM Projects WHERE project_name = ?''', (project,))
                cursor.close()
                conn.commit()
                st.success('All Records of ' + project + ' Deleted')
                st.experimental_rerun()
            elif not delete_project:
                floors_df = pd.read_sql_query(''' SELECT DISTINCT(floor) from medical_rooms 
                                                  WHERE project_id = (SELECT project_id FROM Projects WHERE project_name = ?)
                                              ''', conn, params = (project,))

                if floors_df.empty:
                    st.error('No floor records found')
                else:
                    floorlist = sorted(floors_df['floor'].tolist(), key=lambda x: floors.index(x))
                    floor = st.selectbox('Select Floor to Delete', [''] + floorlist, key=6)

                    if floor != '':
                        delete_floor = st.checkbox('Click to Delete all '+ '**' + floor + '**' + ' Floor Data of ' + '**' + project + '**', key=11)
                        if delete_floor and st.button('Press to confirm'):
                            cursor = conn.cursor()
                            cursor.execute(''' DELETE FROM Medical_rooms 
                                               WHERE project_id = ( SELECT project_id FROM Projects 
                                                                    WHERE project_name = ? )
                                               AND floor = ?
                                           ''',(project, floor,))
                            cursor.close()
                            conn.commit()
                            st.success('All '+ floor +' Floor Records of ' + project + ' Deleted')
                            st.experimental_rerun()                                     
    conn.close()             
