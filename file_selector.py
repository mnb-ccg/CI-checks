# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:53:28 2021

@author: mnb.ccg
"""

import streamlit as st
import pandas as pd
import os
import base64
from xlrd import open_workbook, XLRDError


def col_standardize(columns):
    col_low = [x.lower() for x in columns]
    return col_low

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
    country = ''
    df_i = pd.DataFrame()
    df_c = pd.DataFrame()
    
    
    
    if uploaded_file is not None:
        try:
            df_i = pd.read_excel(uploaded_file, engine="openpyxl", sheet_name='individual')
            df_c = pd.read_excel(uploaded_file, engine="openpyxl", sheet_name='company')
        except ValueError:
            df_i = pd.read_excel(uploaded_file, engine="openpyxl", sheet_name='Individual')
            df_c = pd.read_excel(uploaded_file, engine="openpyxl", sheet_name='Company')
        
        df_i.columns = [x.lower() for x in df_i.columns]
        df_c.columns = [x.lower() for x in df_c.columns]
        
        country = uploaded_file.name[0:2]
        st.write(country)
        if (df_i.empty == False):
            file_bool_i = True
        if (df_c.empty == False): 
            file_bool_c = True
        upload_bool = True
            
    return df_i, df_c, file_bool_i, file_bool_c, upload_bool, country

def get_types():
    types_r = types
    return types_r

def filter_an_report(df):
    new_df = df[df['annual_report'] == 1]
    return new_df


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download file of "Individual" sheet with feedback</a>'
    return href

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
        ['months_serving', 'float'],
        ['comment', 'str'],
        ['current_shares_a_number', 'float'],
        ['current_shares_a_value', 'float'],
        ['current_shares_b_number', 'float'],
        ['current_shares_b_value', 'float'],
        ['current_shares_total_number', 'float'],
        ['current_shares_total_value', 'float'],
        ['current_options_number', 'float'],
        ['current_options_value', 'float'],
        ['currency', 'str'],
        ['base_salary', 'float'],
        ['bonus', 'float'],
        ['total', 'float'],
        ['award_total_value', 'float'],
        ['award_options', 'dummy'],
        ['award_shares', 'dummy'],
        ['award_performance', 'dummy'],
        ['award_restricted', 'dummy'],
        ['pension_total', 'float'],
        ['other_monetary', 'float'],
        ['other_non_monetary', 'str'],
        ['row_id', 'no check'],
    ]