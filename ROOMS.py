import streamlit as st
import sqlite3 
import sys 

def ROOMS(room):
    conn = sqlite3.connect('Database.db')
    col1,col2 = st.columns(2)
    with col1:
        subcol1,subcol2 = st.columns(2)
        with subcol1:
            R = st.number_input("Number of Rooms", min_value=1)  
        with subcol2:
            B = st.number_input("Number of Beds per Room", min_value=1) 
        flow_container = st.container()
    with col2:
        st.write('')
        st.write('')
        st.info('HTM 02-01 Default Units:- ')
    
    if room == 'Resuscitation Room': 
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=2)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=2)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=2)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
        with col1:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=2)
            with subcol2:
                checklist = [O2,N2O,N2O_O2,MA4,SA7,VAC,He_O2,CO2]
                gas = 8 - checklist.count(0)
                st.write('')
                st.info(str(gas) + 'G AVSU')
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 100 + (TB - 1)*6/4 if O2 != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*20/4 if MA4 != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC != 0 else 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        AGS_units = AGS*TB 
         
    elif room == 'Major Treatment Room(Emergency)':           
        with col2:  
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=2)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1) 
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
        with col1:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
            with subcol2:
                checklist = [O2,N2O,N2O_O2,MA4,SA7,VAC,He_O2,CO2]
                gas = 8 - checklist.count(0)
                st.write('')
                st.info(str(gas) + ' G AVSU')
                
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow =0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*20/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0
        AGS_units = AGS*TB 

    elif room == 'Plaster Room(Emergency)':                                                                        
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:   
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)          
    
        TB = R*B                                
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*20/4 if MA4_units != 0 else 0 
        SA7_units = SA7*TB 
        SA7_flow = 0
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0
        AGS_units = AGS*TB  

    elif room == 'Post anaesthsia Recovery Room(Emergency)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=2)
        with col2:  
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=2)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)  
            
                
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/8 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB       

    elif room == 'Treatment Room(Emergency)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:  
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)  
        
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0
        AGS_units = AGS*TB   

    elif room == 'Anesthetic Rooms(all OT)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2: 
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)  

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 0 #'No addtion made' 
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/10 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 10 + (TB - 1)*6/10 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0
        AGS_units = AGS*TB     

    elif room == 'Operating Room(Ortho)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:  
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=4)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=4)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
                
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/10 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 10 + (TB - 1)*6/10 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0
        AGS_units = AGS*TB      

    elif room == 'Operating Room(Neuro)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2: 
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=2)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=4)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 


        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/10 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 10 + (TB - 1)*6/10 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4  if VAC_units != 0 else 0
        AGS_units = AGS*TB        

    elif room == 'Operating Room(General)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:  
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=2)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=2)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=2)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)  

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/10 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 10 + (TB - 1)*6/10 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0
        AGS_units = AGS*TB       

    elif room == 'Post Anesthesia Recovery(OT)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=2)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=2)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)  
                
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*10/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Equipment Service Room(OT)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=1)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)  
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 0 #'Residual Oxygen Capacity'
        N2O_units = N2O*TB 
        N2O_flow = 0 #'No Additional Flow Included'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB
        MA4_flow = 0 #'No Additional Flow Included'
        SA7_units = SA7*TB
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB

    elif room == 'LDRP(Mother)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0) 
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=2)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)            

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + ((TB - 1)*40)/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'LDRP(Baby)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*3/2 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 0 #'No addtional flow' 
        AGS_units = AGS*TB 

    elif room == 'Operating suite Anesthetist(Maternity)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=4)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/10 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 10 + (TB - 1)*6/10 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 
        AGS_units = AGS*TB 

    elif room == 'Operating suite Pediatrician(Maternity)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=4)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*3 if O2_units != 0 else 0
        N2O_units = N2O*TB
        N2O_flow = 10 + (TB - 1)*6/10 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 10 + (TB - 1)*6/10 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB    

    elif room == 'Post Anesthesia Recovery Room(Maternity)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)   
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*3/4 if O2_units != 0 else 0
        N2O_units = N2O*TB
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if N2O_units != 0 else 0
        SA7_units = SA7*TB
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Equipment Service Room(Maternity)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 0 #'Residual Capacity'
        N2O_units = N2O*TB 
        N2O_flow = 0 #'No Additional Flow included'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'No Additional Flow included'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 0 #'Residual Capacity' 
        AGS_units = AGS*TB 

    elif room == 'Neonatal Unit(Maternity)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=2)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)                
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=2)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40*TB
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Single Bedroom In Patient(Maternity)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/6 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 
        AGS_units = AGS*TB 

    elif room == 'Multi Bedroom In Patient(Maternity)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_va1ue=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/6 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Nursery(Maternity)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB  
        O2_flow = 10 + (TB - 1)*3/2 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 0 #'No additional to be included'
        AGS_units = AGS*TB 

    elif room == 'Special Procedure Room(Diagnostic)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB

    elif room == 'Anaesthic Room(Diagnostic)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0
        AGS_units = AGS*TB 

    elif room == 'Holding and recovery Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Ultrasound Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0
        AGS_units = AGS*TB 

    elif room == 'Fluroscopy Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Urography Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Tomography Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)                
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0
        AGS_units = AGS*TB 

    elif room == 'MRI Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'CAT Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Angiography Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0 
        He_O2_units = He_O2*TB
        He_O2_flow = 0 
        CO2_units = CO2*TB
        CO2_flow = 0 
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0
        AGS_units = AGS*TB 

    elif room == 'Endoscopy Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Lineac bunkers Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'General Purpose Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 10 + (TB - 1)*6/4 if N2O_units != 0 else 0
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'In Patient-single Bedroom':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*6/10 if MA4_units != 0 else 0
        SA7_units = SA7*TB
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 
        AGS_units = AGS*TB 

    elif room == 'In Patient-multi Bedroom':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 10 + (TB - 1)*6/10 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Treatment Room(In Patient)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units= N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*20/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Dialysis Renal Room':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 20 + (TB - 1)*10/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0
        AGS_units = AGS*TB 

    elif room == 'Critical Care Area':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=2)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=4)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=4)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=4)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB- 1)*6*(3/4) if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 80 + (TB - 1)*80/2 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Equipment Service Room(Critical Care)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 0 #'Residual Capacity'
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'No additional flow included'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 0 #'Residual Capacity' 
        AGS_units = AGS*TB 

    elif room == 'Coronory Care Unit(CCU)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=2)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=4)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=4)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=4)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6*(3/4) if O2_units != 0 else 0
        N2O_units = N2O*TB
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O02*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB
        MA4_flow = 80 + (TB - 1)*80/2 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'High Dependency Unit(HDU)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=2)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=4)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=4)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=4)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow  = 10 + (TB - 1)*6*(3/4) if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 80 + (TB - 1)*80/2 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Burns Unit':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=2)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=2)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=2)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=2)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*20/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Electro-Convulsive Therapy(ECT)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=1)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'No additonal flow included'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*20/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Post anesthesia Recovery(Adult mental)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 40 + (TB - 1)*40/4 if MA4_units != 0 else 0
        SA7_units = SA7*TB
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Single Bedroom(Day Patient)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 
        AGS_units = AGS*TB 

    elif room == 'Multi Bedroom(Day Patient)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/10 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Treatment Room(Day Patient)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow  = 10 + (TB - 1)*6/4 if O2_units != 0 else 0 
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Endoscopy Room (Day Patient)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0) 
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/3 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Plaster Room(Fracture)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=1)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Treatment Room(Adult Acute Day Care)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=3)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/4 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Post Anesthesia Recovery(Adult Acute Day Care)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Treatment Room/Cubicles(Out-Patient)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 + (TB - 1)*40/8 if VAC_units != 0 else 0 
        AGS_units = AGS*TB 

    elif room == 'Consulting/treatment type 1(Oral Surgery)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=0)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB  
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 0 #'Dental Vacuum Only' 
        AGS_units = AGS*TB 

    elif room == 'Consulting/treatment type 2/3(Oral Surgery)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=0)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B    
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 0 #'Dental Vacuum Only' 
        AGS_units = AGS*TB   

    elif room == 'Consulting/treatment type 1(Orthodontic)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40 
        AGS_units = AGS*TB 

    elif room == 'Consulting/treatment type 2/3(Orthodontic)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=0)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=0)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=1)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B    
        O2_units = O2*TB 
        O2_flow = 10 + (TB - 1)*6/4 if O2_units != 0 else 0
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'None'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'None'
        VAC_units = VAC*TB 
        VAC_flow = 40
        AGS_units = AGS*TB 

    elif room == 'Sterile Services':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=0)
        with col2:
            info_container = st.container()   
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=0)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=1)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=0)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)

        TB = R*B
        O2_units = O2*TB 
        O2_flow = 0 #'Residual Capacity'
        N2O_units = N2O*TB 
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB 
        MA4_flow = 0 #'No addtional flow included'
        SA7_units = SA7*TB 
        SA7_flow = 0 #'No addtional flow required'
        VAC_units = VAC*TB 
        VAC_flow = 0 #'Residual Capacity'
        AGS_units = AGS*TB 

    elif room == 'IAP(Sterile)':
        with col1:
            room_AVSU = st.number_input("Room AVSU Set(s)", min_value=0, max_value=5, value=1)
        with col2:
            info_container = st.container()   
            subcol1,subcol2 = st.columns(2)
            with subcol1:
                O2 = st.number_input("O2 units", min_value=0, max_value=5, value=1)
                N2O_O2 = st.number_input("N2O/O2 units", min_value=0, max_value=5, value=0)
                SA7 = st.number_input("SA7 units", min_value=0, max_value=5, value=1)
                He_O2 = st.number_input("He/O2 Units", min_value=0, max_value=5, value=0)
            AGS = st.number_input("AGS units", min_value=0, max_value=5, value=0)
            with subcol2:
                N2O = st.number_input("N2O units", min_value=0, max_value=5, value=0)  
                MA4 = st.number_input("MA4 units", min_value=0, max_value=5, value=1)
                VAC = st.number_input("VAC units", min_value=0, max_value=5, value=0)
                CO2 = st.number_input("CO2 units", min_value=0, max_value=5, value=0)
            
        TB = R*B
        O2_units = O2*TB
        O2_flow = 0 #'Residual Capacity'
        N2O_units = N2O*TB
        N2O_flow = 0 #'None'
        N2O_O2_units = N2O_O2*TB
        N2O_O2_flow = 0
        He_O2_units = He_O2*TB
        He_O2_flow = 0
        CO2_units = CO2*TB
        CO2_flow = 0
        MA4_units = MA4*TB
        MA4_flow = 0 #'No addtional flow includeds'
        SA7_units = SA7*TB
        SA7_flow = 0 #'No addtional flow required'
        VAC_units = VAC*TB
        VAC_flow = 0 #'None'
        AGS_units = AGS*TB
    
    with flow_container:
        data = { 'Gas': ['O2', 'N2O', 'N2O/O2', 'MA4', 'SA7', 'VAC', 'He/O2', 'CO2'],
                 'Gas Flow (L/min) to the room': [O2_flow, N2O_flow, N2O_O2_flow, MA4_flow, SA7_flow, VAC_flow, He_O2_flow, CO2_flow]}

        formatted_data = { key: [f"{value:.1f}" if isinstance(value, float) else value for value in values]
                           for key, values in data.items()}

        st.table(formatted_data)
    
    gases_list = [O2_units,N2O_units,N2O_O2_units,MA4_units,SA7_units,VAC_units,He_O2_units,CO2_units]
    units_list = gases_list + [AGS_units]
    flow_list = [O2_flow,N2O_flow,N2O_O2_flow,MA4_flow,SA7_flow,VAC_flow,He_O2_flow,CO2_flow]
    gas_count = 8 - gases_list.count(0)
    
    room_AVSU = str(room_AVSU) + ' Set'+ ' (' + str(gas_count) + 'G' + ')' if room_AVSU != 0 and gas_count != 0 else 'None'
        
    return R, B, units_list, flow_list, [room_AVSU]
