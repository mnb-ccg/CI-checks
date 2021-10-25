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
        if (df_i.empty == False):
            file_bool_i = True
        if (df_c.empty == False): 
            file_bool_c = True
        upload_bool = True
            
    return df_i, df_c, file_bool_i, file_bool_c, upload_bool

def get_types():
    types_r = types
    return types_r

def filter_an_report(df):
    new_df = df[df['annual_report'] == 1]
    return new_df




types = [
        ['company_id', 'str'],
        ['company_name', 'str'],
        ['year', 'int'],
        ['person_id', 'str'],
        ['name', 'str'],
        ['annual_report', 'dummy'],
        ['birth_date', 'str'],
        ['gender', 'str'],
        ['nationality',	'str'],
        ['role_code', 'str'],
        ['position', 'str'],
        ['election_form', 'str'],
        ['independent', 'str'],
        ['on_board', 'dummy'],
        ['appointment_date', 'str'],
        ['nomination',	'str'],
        ['audit', 'str'],
        ['remuneration', 'str'],
        ['risk', 'str'],
        ['step_down', 'str'],
        ['months_serving', 'int'],
        ['comment', 'str'],
        ['current_shares_A_number', 'int'],
        ['current_shares_A_value', 'int'],
        ['current_shares_B_number', 'int'],
        ['current_shares_B_value', 'int'],
        ['current_shares_total_number', 'int'],
        ['current_shares_total_value', 'int'],
        ['current_options_number', 'int'],
        ['current_options_value', 'int'],
        ['currency', 'str'],
        ['base_salary', 'int'],
        ['bonus', 'int'],
        ['total', 'int'],
        ['award_total_value', 'int'],
        ['award_options', 'dummy'],
        ['award_shares', 'dummy'],
        ['award_performance', 'dummy'],
        ['award_restricted', 'dummy'],
        ['pension_total', 'int'],
        ['other_monetary', 'str'],
        ['other_non_monetary', 'str'],
        ['row_id', 'no check'],
    ]