import streamlit as st
import pandas as pd
#import importing_files as imfil
import file_selector as fs
import checks as ch

header = st.container()
#guide = st.container()

get_file = st.container()


st.markdown("---")

basic_check = st.container()
type_check = st.container()

st.markdown("---")

role_code_check = st.container()
position_check = st.container()
date_check = st.container()
nationality_check = st.container()
year_check = st.container()
downloader = st.container()



with header:
    st.title("Data Self-Checking App v. 1.0")
    st.write("Hello, and welcome to the CBS-CCG data-checking app.")
    st.write("The idea behind this app is to minimize time spent correcting data sent to CBS-CCG, allowing our suppliers to deliver high-quality data on time!")
    st.write("You can upload the datasheet in the drag-and-drop box below. When you have done so, the app will make a series of automated checks according to the manual sent to our suppliers.")
    


# with guide:
#     st.subheader("Tutorial")
#     st.write("The behind this app is to minimize time spent correcting data sent to CBS-CCG, allowing our suppliers to deliver high-quality data on time!")
#     st.write("You can upload the datasheet in the drag-and-drop box under the Tutorial section. When you have done so, the app will make a series of automated checks according to the manual sent to our suppliers.")
#     st.write("Include link here?")
#     st.write("For every check, a green, yellow or red box will appear.")
#     st.success("Green indicates success, or the check has passed, meaning that the automated check is satisfied.")
#     st.warning("Yellow indicates a warning. These are rare at the moment, but indicates something the we think the supplier should be aware of")
#     st.error("Red indicates and error, and the issue should be resolved before sending the data to CBS-CCG.")
#     st.write("Time and effort was put into this app in order to help our suppliers. But the app is not perfect. If you disagree with the checks or find any bugs, let us know at....")
#     st.write("Hopefully the feedback from these automatic checks are useful!")
    


with get_file:
    file_bool_i = False
    file_bool_c = False
    upload_bool = False
    
    df_i, df_c, file_bool_i, file_bool_c, upload_bool, country, file_name = fs.upload_file()
    
    
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
            column_check_i = ch.column_check(df_i, 'Individual', country)
        st.subheader("Column Check - 'Company'")
        if (file_bool_c):
            column_check_c = ch.column_check(df_c, 'Company', country)
            

with type_check:
    df_type_check = pd.DataFrame()
    if(column_check_i & column_check_c):
        
        #now that we know that the dataset conforms to our format, we can now 
        #focus on the data quality on the individuals found in the annual reports
        df_i = fs.filter_an_report(df_i.copy())
    
        types = fs.get_types()
        
        columns_checked = []
        for column, type_c in types:
            if(type_c != 'str' and type_c != 'no check'):
                columns_checked.append(column)
                df_check = ch.check_type(df_i, column, type_c)
                df_type_check[column] = df_check
        df_type_check['feedback'] = df_type_check[df_type_check.columns.tolist()].agg(''.join, axis=1)

    
with role_code_check:
    if(column_check_i & column_check_c):
        
        df_check = ch.check_role_code(df_i)
        df_type_check['feedback'] = df_type_check['feedback'] + df_check.to_frame()['role_code']
        

with position_check:
    if(column_check_i & column_check_c):
        
        df_check = ch.check_position(df_i)
        df_type_check['feedback'] = df_type_check['feedback'] + df_check.to_frame()['key']
     
        

            

with date_check:
    if(column_check_i & column_check_c):
        df_check = ch.check_date(df_i, 'birth_date')
        df_type_check['feedback'] = df_type_check['feedback'] + df_check.to_frame()[0]
        
        df_check = ch.check_date(df_i, 'appointment_date')
        df_type_check['feedback'] = df_type_check['feedback'] + df_check.to_frame()[0]



            

with nationality_check:
    if(column_check_i & column_check_c):
        df_check = ch.check_nationality(df_i)
        df_type_check['feedback'] = df_type_check['feedback'] + df_check.to_frame()['nationality']


with year_check:
    if(column_check_i & column_check_c):
        df_check = ch.check_year(df_i)
        df_type_check['feedback'] = df_type_check['feedback'] + df_check.to_frame()['year']



with downloader:
    if(column_check_i & column_check_c):
        df_i['feedback'] = df_type_check['feedback']
        st.markdown(fs.get_table_download_link(df_i, file_name), unsafe_allow_html=True)
        
    #DC function here, returns new df with wrong rows, input dataframe from upload
    
    
    # with appointment_date_check:
#     bool_cad = False 
#     if(column_check_i & column_check_c):
#         st.subheader("'Individual' - 'appointment_date' check" )
        
#         bool_cad, faulty_rows = ch.check_date(df_i, "appointment_date")
#         if (bool_cad):
#             st.success("Check passed")
#         else:
#             st.error("These rows do not look correct:")
#             st.write(faulty_rows)