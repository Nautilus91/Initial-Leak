#!/usr/bin/env python
# coding: utf-8

# In[16]:


import streamlit as st
import math


fluid = st.selectbox('Please select your type of fluid', ('Gas','Liquid','Multiphase'))

if fluid == "Liquid":

    p1 = st.number_input('Please specify the inventory pressure (Pa)')
    # Pressure inside vessel
    patm = st.number_input('Please specify the pressure outside the inventory (Pa)')
    #Pressure outside vessel
    stath = st.number_input('Please provide the liquids static height')
    #Static height of liquid inside the vessel
    C_d = st.number_input('Please provide the discharge coefficient, (0-1)')
    #Discharge coefficient
    density = st.number_input("Please provide the liquids density (kg/m\u00b3 )")
    #Density of the fluid

    if density == 0:
        density=1
        st.write('No density was provided')
    else:
        mflux = C_d*density*(2*stath*9.81+2*((p1-patm)/density))**0.5

        st.write('Based on the input, the mass flux(kg/sm\u00b2) is: ', round(mflux,2))
        # The mass flux per square meter
        hole = st.number_input('Please specify your hole size (mm)')

        leak = round(10**(-6)*mflux * math.pi*0.25*hole**2,2)
        #Leak size

        st.write('The leak size for the ', hole, 'mm leak size is ', round(leak,2), " kg/s")
    
elif fluid == "Gas":
    p1 = st.number_input('Please specify the inventory pressure (Pa)')
    # Pressure inside vessel
    patm = st.number_input('Please specify the pressure outside the inventory (Pa)')
    #Pressure outside vessel
    Temp = st.number_input('Inventory temperature (\N{DEGREE SIGN}C)')
    C_d = st.number_input('Please provide the discharge coefficient, (0-1)')
    #Discharge coefficient
    M = st.number_input('Please provide the Molar weight')
    #Molar weight of the gas
    k = st.number_input('Please provide the ratio of specific heats (Cp/Cv)')
    #Specific Heats
    Z = st.number_input('Please provide the compressibility')
    #Compressibility
    
    R = 8314
    #Boltzmann constant
    Temp = Temp+273.15
    #Convert from Celsius to Kelvin
    
    if not 0 in {p1,patm,Temp,C_d,M,k,Z}:        

        Crit_pressure = patm*((k+1)/2)**(k/(k-1))
        # Calculates Critical pressure
        
        if Crit_pressure < p1:
        #Choked flow
            mflux = C_d*p1*(k*(M/(Z*R*Temp))*(2/(k+1))**((k+1)/(k-1)))**0.5
            st.write('The flow is sonic (choked)')
        else:
            mflux = C_d * p1 *(((M / (Z * R * Temp)) * (2 * k / (k - 1)) * (1 - (patm / p1)**((k - 1) / k)))**0.5) * (patm / p1)**(1 / k)
            #mflux = C_d*p1*(((M/(Z*R*Temp))*(2*k/(k-1))*((1-(patm/p1))**((k-1)/k)))**0.5)*(patm/p1)**(1/k)
            st.write('The flow is subsonic')

        st.write('Based on the input, the mass flux(kg/sm\u00b2) is: ', round(mflux,2))
        # The mass flux per square meter
        hole = st.number_input('Please specify your hole size (mm)')

        leak = round(10**(-6)*mflux * math.pi*0.25*hole**2,2)
        #Leak size

        st.write('The leak size for the ', hole, 'mm leak size is ', round(leak,2), " kg/s")
    else:
        st.write('Input is missing')
    
    
    
    
else:
    st.write('Still under development')
    p1 = st.number_input('Please specify the inventory pressure (Pa)')
    # Pressure inside vessel
    C_d = st.number_input('Please provide the discharge coefficient, (0-1)')
    #Discharge coefficient
    density = st.number_input("Please provide the average density for the multiphase fluid (kg/m\u00b3 )")
    #Density of the fluid
        
    p_c = 0.55*p1
    #Pressure at throat
    
    if density == 0:
        density=1
        st.write('No density was provided')
    else:
        mflux = C_d*(2*density*(p1-p_c))**0.5

        st.write('Based on the input, the mass flux(kg/sm\u00b2) is: ', round(mflux,2))
        # The mass flux per square meter
        hole = st.number_input('Please specify your hole size (mm)')

        leak = round(10**(-6)*mflux * math.pi*0.25*hole**2,2)
        #Leak size

        st.write('The leak size for the ', hole, 'mm leak size is ', round(leak,2), " kg/s")
    
        


# In[ ]:





# In[ ]:




