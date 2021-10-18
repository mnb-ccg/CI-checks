# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:53:28 2021

@author: mnb.ccg
"""

import streamlit as st
import pandas as pd
import os
from xlrd import open_workbook, XLRDError


def test_book(filename):
    try:
        open_workbook(filename)
    except XLRDError:
        return False
        st.write("Excel file chosen")
    else:
        st.write("File is not .xlsx or .xls format")
        return True

def drop_down_files():
    folder_path='.'
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename), selected_filename
 

def upload_file():
    uploaded_file = st.file_uploader("Choose a file")
    file_bool_i = False
    file_bool_c = False
    upload_bool = False
    df_i = pd.DataFrame()
    df_c = pd.DataFrame()
    
    if uploaded_file is not None:
        df_i = pd.read_excel(uploaded_file, engine="openpyxl", sheet_name='individual')
        df_c = pd.read_excel(uploaded_file, engine="openpyxl", sheet_name='company')
        #df_i = df_i.astype(str)
        #df_c = df_c.astype(str)
        if (df_i.empty == False):
            file_bool_i = True
        if (df_c.empty == False): 
            file_bool_c = True
        upload_bool = True
            
    return df_i, df_c, file_bool_i, file_bool_c, upload_bool


