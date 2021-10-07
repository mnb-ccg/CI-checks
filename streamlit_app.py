import streamlit as st
#mport pandas as pd
#import importing_files as imfil
import file_selector as fs
import checks as ch

header = st.container()
get_file = st.container()
basic_check = st.container()

# To be replaced with something dynamic, like somewhere to upload
#path_dk = 'C:\\Users\\mnb.ccg\\OneDrive - CBS - Copenhagen Business School\\Data Collection DATABASE\\material for credit info\\Final Templates and material\\CI_mnb_check\\13-09-2021'

with header:
    st.title("Welcome to my project")


with get_file:
    #filename = fs.drop_down_files()
    df, filename = fs.upload_file()
    file_check = fs.test_book(filename)
    
    
with basic_check:
    #df_c = ch.standardize_df(df)
    column_check = False
    if (file_check):
        column_check = ch.column_check(df)
     
