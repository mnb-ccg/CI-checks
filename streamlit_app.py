import streamlit as st
#mport pandas as pd
#import importing_files as imfil
import file_selector as fs
import checks as ch

header = st.container()
get_file = st.container()
basic_check = st.container()
advanced_check = st.container()


with header:
    st.title("Data Self-Checking App")
    st.write("When you upload your data, this app will make a series of check.")
    st.write("For every check, a green, yellow or red box will appear. Green indicates succes, yellow a warning, and red an error.")
    st.write("Hopefully the feedback from these automatic checks are useful!")


with get_file:
    file_bool_i = False
    file_bool_c = False
    upload_bool = False
    
    df_i, df_c, file_bool_i, file_bool_c, upload_bool = fs.upload_file()
    
    if(upload_bool == True):
        if(file_bool_i == False):
            st.error("No 'Individual' sheet found. Check to see if this is the correct file, and check spelling")
        if(file_bool_c == False):
            st.error("No 'Company' sheet found. Check to see if this is the correct file, and check spelling")
        
    
with basic_check:
    column_check_i = False
    column_check_c = False
    if(file_bool_i and file_bool_c):
        st.subheader("Column Check - 'Individual'")
        if (file_bool_i):
            column_check_i = ch.column_check(df_i, 'Individual')
        st.subheader("Column Check - 'Company'")
        if (file_bool_c):
            column_check_c = ch.column_check(df_c, 'Company')
     
with advanced_check:
    if(column_check_i & column_check_c):
        df_cy = check_basic_types(df_i)
        st.write(df_cy)
        
        
    
    
    #DC function here, returns new df with wrong rows, input dataframe from upload
    