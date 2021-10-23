import streamlit as st
#mport pandas as pd
#import importing_files as imfil
import file_selector as fs
import checks as ch

header = st.container()
get_file = st.container()
basic_check = st.container()
year_check = st.container()
birth_date_check = st.container()
appointment_date_check = st.container()
role_code_check = st.container()




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
        st.header("Basic Columns Check")
        st.subheader("Column Check - 'Individual'")
        if (file_bool_i):
            column_check_i = ch.column_check(df_i, 'Individual')
        st.subheader("Column Check - 'Company'")
        if (file_bool_c):
            column_check_c = ch.column_check(df_c, 'Company')
            
with role_code_check:
    bool_rc = False
    if(column_check_i & column_check_c):
        st.header("Row-by-Row Checks")
        #now that we know that the dataset conforms to our format, we can now 
        #focus on the data quality on the individuals found in the annual reports
        df_i = fs.filter_an_report(df_i.copy())
        
        st.subheader("'role_code' - Check")
        
        bool_rc, faulty_rows_rc = ch.check_role_code(df_i)
        if (bool_rc):
            st.success("'Individual' - 'role_code', check passed")
            bool_rc = True
        else:
            st.error("These rows do not look correct:")
            st.write(faulty_rows_rc)
        
    
     
        
with year_check:
    bool_cy_i = False
    bool_cy_c = False
    if(column_check_i & column_check_c):

        st.subheader("'year' - Check" )
        
        bool_cy_i, faulty_rows_i = ch.check_year(df_i)
        if (bool_cy_i):
            st.success("'Individual' - 'year', check passed")
            year_check_i = True
        else:
            st.error("These rows do not look correct:")
            st.write(faulty_rows_i)
            
        bool_cy_c, faulty_rows_c = ch.check_year(df_c)
        if (bool_cy_c):
            st.success("'Company' - 'year', check passed")
            year_check_C = True
        else:
            st.error("These rows do not look correct:")
            st.write(faulty_rows_c)
            

with birth_date_check:
    bool_cbd = False 
    if(column_check_i & column_check_c):
        st.subheader("'Individual' - 'birth_date' check" )
        
        bool_cbd, faulty_rows = ch.check_date(df_i, "birth_date")
        if (bool_cbd):
            st.success("Check passed")
        else:
            st.error("These rows do not look correct:")
            st.write(faulty_rows)


            
with appointment_date_check:
    bool_cad = False 
    if(column_check_i & column_check_c):
        st.subheader("'Individual' - 'appointment_date' check" )
        
        bool_cad, faulty_rows = ch.check_date(df_i, "appointment_date")
        if (bool_cad):
            st.success("Check passed")
        else:
            st.error("These rows do not look correct:")
            st.write(faulty_rows)
            


        
    
    #DC function here, returns new df with wrong rows, input dataframe from upload