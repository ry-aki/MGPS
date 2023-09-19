import streamlit as st 
import pandas as pd
import sqlite3
from ROOMS import ROOMS

def AddROOMStoDB(project, dept, dept_AVSU, floor, room): 
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT project_id FROM Projects WHERE project_name = ?", (project,))
    project_id = cursor.fetchone()[0]
    
    flag = 0
    
    if floor != '':
        R, B, units_list, flow_list, room_AVSU = ROOMS(room)   
        
        changed_room = st.text_input('Change Room Name (Optional)')
        
        if changed_room != '':
            room = changed_room
        else:
            pass
        
        data = [project_id, floor, dept, dept_AVSU, room] + room_AVSU + [R, B] + units_list + flow_list 
        
        cursor.execute(''' SELECT room_id FROM Medical_rooms
                           WHERE project_id = ? AND floor = ? AND dept = ? AND room_name = ?
                       ''', (project_id, floor, dept, room))
        existing_room_id = cursor.fetchone()

        col1,col2,col3,col4,col5 = st.columns(5)
        if existing_room_id is not None:
            with col4:
                if st.button('Delete'):
                    cursor.execute(''' DELETE FROM Medical_rooms
                                       WHERE project_id = ( SELECT project_id FROM Projects 
                                                            WHERE project_name = ? )
                                       AND floor = ? 
                                       AND room_name = ?
                                   ''',(project, floor,room,))  
                    flag = 1
                    conn.commit()
                    conn.close()
                    st.experimental_rerun()
            with col5:
                if st.button('Save'): 
                    cursor.execute(''' UPDATE Medical_rooms
                                       SET project_id = ?, floor = ?, dept = ?, dept_AVSU = ?, room_name = ?, room_AVSU = ?,
                                           no_of_rooms = ?, no_of_beds = ?, O2_unit = ?, N2O_unit = ?, N2O_O2_unit = ?,
                                           MA4_unit = ?, SA7_unit = ?, VAC_unit = ?, He_O2_unit = ?, CO2_unit = ?,
                                           AGS_unit = ?, O2_flow = ?, N2O_flow = ?, N2O_O2_flow = ?, MA4_flow = ?, 
                                           SA7_flow = ?, VAC_flow = ?, He_O2_flow = ?, CO2_flow = ?
                                       WHERE room_id = ?
                                   ''', data + [existing_room_id[0]])
                    flag = 2 
                    conn.commit()
                    conn.close()
                    st.experimental_rerun()
        else:
            with col5:
                if st.button('Add'): 
                    cursor.execute(''' INSERT INTO Medical_rooms (project_id, floor, dept, dept_AVSU, room_name,
                                                                  room_AVSU, no_of_rooms, no_of_beds, O2_unit,
                                                                  N2O_unit, N2O_O2_unit, MA4_unit, SA7_unit,
                                                                  VAC_unit, He_O2_unit, CO2_unit, 
                                                                  AGS_unit, O2_flow, N2O_flow, N2O_O2_flow,
                                                                  MA4_flow, SA7_flow, VAC_flow, He_O2_flow, CO2_flow) 
                                       VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                                   ''', data)
                    flag = 3
                    conn.commit()
                    conn.close()
                    st.experimental_rerun()
    
    else:
        st.error('Select all options')
    
    if flag == 1:
        st.error(room +' deleted from '+ floor +' floor')
    elif flag == 2:    
        st.success('Values Updated')
    elif flag == 3:    
        st.success('Room Added')
