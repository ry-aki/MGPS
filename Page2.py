import streamlit as st 
import pandas as pd
import sqlite3

def downloadbutton(df,key): 
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        checked = st.checkbox('Print 🖨️',key = key)
        st.write('')
    with col2:
        if checked:
            if st.download_button(
                label = "Download Excel ",
                data = df.to_csv(index=False),
                file_name = "table.csv",
                mime = "text/csv" ):
                st.success('Downloaded')
    
def DOT_table(project):
    conn = sqlite3.connect('Database.db')
    with st.expander('**DOT**', expanded= True):
        if project != '':
            floors_df = pd.read_sql_query('''SELECT DISTINCT(floor) from medical_rooms 
                                    WHERE project_id = (SELECT project_id FROM Projects WHERE project_name = ?)''' 
                                  ,conn, params = (project,))
            if floors_df.empty:
                st.error('No Floor Data to show')

            else:                              
                query = '''SELECT floor AS Floor,
                                  dept AS 'Dept',
                                  dept_AVSU AS 'Dept AVSU',
                                  room_name AS 'Room',
                                  room_AVSU AS 'Room AVSU',
                                  no_of_rooms AS 'No of Rooms',
                                  no_of_beds AS 'No of Beds',
                                  O2_unit AS 'O2',
                                  O2_flow AS 'O2 Flow',
                                  N2O_unit AS 'N2O',
                                  N2O_flow AS 'N2O Flow',
                                  N2O_O2_unit AS 'N2O/O2',
                                  N2O_O2_flow AS 'N2O/O2 Flow',
                                  MA4_unit AS 'MA4',
                                  MA4_flow AS 'MA4 Flow',
                                  SA7_unit AS 'SA7',
                                  SA7_flow AS 'SA7 Flow',
                                  VAC_unit AS 'VAC',
                                  VAC_flow AS 'VAC Flow',
                                  He_O2_unit 'He/O2',
                                  He_O2_flow AS 'He/O2 Flow',
                                  CO2_unit AS 'CO2',
                                  CO2_flow AS 'CO2 Flow',
                                  AGS_unit AS 'AGS'
                           FROM Medical_rooms
                           WHERE project_id = ( SELECT project_id FROM Projects 
                                                WHERE project_name = ? )
                        '''
                df = pd.read_sql_query(query, conn, params = (project,))
                floor_order = ['Ground', 'First', 'Second', 'Third', 'Fourth', 'Fifth'] 
                
                
                df2 = df.groupby('Floor').sum().reset_index()
                df2 = df2.drop(columns=['Room']) 
                df3 = df2.sum().drop('Floor')

                data = {'Details': df3.index.tolist(),
                        'Grand Total': df3.tolist()}
                formatted_data = {key: [f"{value:.1f}" if isinstance(value, float) else value for value in values]
                                  for key, values in data.items()}

                grand_total_df = pd.DataFrame([['Grand Total'] + formatted_data['Grand Total']], columns=df2.columns)
                df2 = pd.concat([df2,grand_total_df], ignore_index=True)

                
                df = df.assign(sorting_order=df['Floor'].map({floor: i for i, floor in enumerate(floor_order)})) \
                       .sort_values(by=['sorting_order']) \
                       .reset_index(drop=True) \
                       .drop(columns='sorting_order')
                
                df2 = df2.assign(sorting_order=df2['Floor'].map({floor: i for i, floor in enumerate(floor_order)})) \
                       .sort_values(by=['sorting_order']) \
                       .reset_index(drop=True) \
                       .drop(columns='sorting_order')
                
                downloadbutton(df2,key=14)
                df2.replace({'None': '', 0: '', None : ''}, inplace=True)
                df2.drop(columns=['Dept','Dept AVSU','Room AVSU'], inplace=True) 
                st.dataframe(df2,hide_index=True) 

                st.info('**DOT Table:-**')
                df.replace({'None': '', 0: '', None : ''}, inplace=True)
                downloadbutton(df,key=15)
                st.dataframe(df,hide_index=True)  
                
    conn.close() 
    