# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:34:31 2021

@author: mnb.ccg
"""

import streamlit as st
#import importing_files as imfil
import matplotlib.pyplot as plt
import numpy as np
import string
#from xlrd import open_workbook, XLRDError

column_names_i = ['company_id', 'company_name', 'year', 'person_id', 'name', 'annual_report', 'birth_date', 'gender', 'nationality', 'role_code', 'position', 'election_form', 'independent', 'on_board', 'appointment_date', 'nomination', 'audit', 'remuneration', 'risk', 'step_down', 'months_serving', 'comment', 'current_shares_A_number', 'current_shares_A_value', 'current_shares_B_number', 'current_shares_B_value', 'current_shares_total_number', 'current_shares_total_value', 'current_options_number', 'current_options_value', 'currency', 'base_salary', 'bonus', 'total', 'award_total_value', 'award_options', 'award_shares', 'award_performance', 'award_restricted', 'pension_total', 'other_monetary', 'other_non_monetary', 'row_id']
column_names_c = ['company_id', 'company_name', 'year', 'size_management', 'total_pay_management', 'size_board', 'total_pay_board', 'employees_year_end', 'employees_average', 'total_pay_employees', 'currency', 'fisca_year_start', 'fiscal_year_end', 'row_id']





def calc_missing(df):
    new_df = df.isnull().sum(axis=0)/len(df)
    return new_df

def plot_barh_missing(columns, values, start_index, final_index, title):
    fig = plt.figure()
 
    # creating the bar plot
    plt.barh(columns[start_index:final_index], values[start_index:final_index])
 
    plt.xlabel("Column names")
    plt.ylabel("Ratio of missing values")
    plt.title(title)
    plt.xlim(left = 0.0, right = 1.05)

    return fig



def col_standardize(columns):
    col_low = [x.lower() for x in columns]
    col_clean = [s.translate(str.maketrans('', '', string.punctuation)) for s in col_low] 
    return col_clean


def column_check(df, sheet):
    
    df_col = df.columns.astype(str)
    df_col_clean = col_standardize(df_col)
    
    if(sheet == 'Individual'):
        templ_col = column_names_i
        templ_col_clean = col_standardize(templ_col)
    elif(sheet == 'Company'):
        templ_col = column_names_c
        templ_col_clean = col_standardize(templ_col)
    else:
        st.error("Sheet name not recognized")
        
    
    correct = False
    df_set = set(df_col_clean)
    templ_set = set(templ_col_clean)
    missing_columns = templ_set - df_set
    excess_columns = df_set - templ_set
    

    if (len(missing_columns) == 0):
        correct = True
        st.success("Columns passed the check")
    else:
        correct = False
        st.error("The columns are not the same as the template.")
        st.error("These columns were not found in the uploaded dataset (Note: punctuation has been removed):")
        st.write(missing_columns)
        st.warning("These columns were found in the dataset, but not in the template (Note: punctuation has been removed):")
        st.write(excess_columns)

    return correct

def check_year_length(string):
    if(len(string) == 4):
        return True
    if(len(string) != 4):
        return False


def check_basic_types(df):
    df['year'].apply(check_year_length)
    return df
    
