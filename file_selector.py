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
    df = pd.DataFrame()    
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        df = df.astype(str)
        file_bool = True
    else:
        file_bool = False
    return df, file_bool


