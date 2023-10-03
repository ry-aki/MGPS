import streamlit as st
from PIL import Image
from time import sleep
import base64
import sqlite3
import pandas as pd

from Page1 import add_records, new_project, del_records
from Page2 import DOT_table

image = Image.open('modcon.png')  
icon = Image.open('MC.png')
st.set_page_config(page_title = "Modcon - Medical Gas Pipeline System", page_icon = icon) 
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)

def login_page():
    if 'logged_in' in st.session_state:
        main()
        return
    
    placeholder = st.empty()
    au = "modcon"
    ap = "bW9kY29uQDEyMw=="
    
    encoded_bytes = ap.encode()
    decoded_bytes = base64.b64decode(encoded_bytes)
    ap = decoded_bytes.decode()

    with placeholder.form("Login"):
        st.markdown("#### Enter your credentials")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if username != '' and password != '':
        if submit and username == au and password == ap:
            st.session_state.logged_in = True
            success_placeholder = st.empty()
            with st.spinner(text = 'Logging In'):
                sleep(2)
                st.success('Logged In')
            success_placeholder.empty()
            placeholder.empty()
            main() 
        elif submit and username != au or password != ap:
            st.error("Incorrect Username or Password")

def main():    
    st.sidebar.image(image, caption = 'Turnkey Medical Engineering',width = 240)
    st.title('MGPS Designer')
    col1,col2 = st.columns(2)
    with col1:
        with st.expander('**New project**'):
            new_project()
    with col2:
        with st.expander('**Delete Project**'):
            del_records()
    conn = sqlite3.connect('Database.db')
    projects_df = pd.read_sql_query('''SELECT project_name FROM Projects''', conn) 

    if projects_df.empty:
        st.error('No Projects to show, Add a New Project')
    else:
        with st.expander('**Edit Project**',expanded = True):
            project = st.selectbox('Select the project', [''] + projects_df['project_name'].tolist(), key=20)
            if project != '':
                add_records(project) 
       
        DOT_table(project)
        
if __name__ == '__main__':
    main()    
    
