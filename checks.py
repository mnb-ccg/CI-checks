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
from xlrd import open_workbook, XLRDError

column_names = ['company_id', 'company_name', 'year', 'person_id', 'name', 'annual_report', 'birth_date', 'gender', 'nationality', 'role code', 'position', 'election_form', 'independent', 'on_board', 'appointment_date', 'committee - audit', 'committee - nomination', 'committee - remuneration', 'committee - risk', 'step_down', 'months serving', 'comment', 'current ownership - a-shares', 'current ownership - b-shares', 'current ownership - p-options', 'current ownership - t-options', 'currency', 'base salary', 'bonus', 'total salary', 'bonus.1', 'incentives', 'share-based incentive schemes - total', 'long-t', 'short-t', "stock opt's", 'p shares', 'r shares', 'pension - total', 'monetary', 'non-mon.']




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

def standardize_df(df):
    df.columns = column_names
    return df



def col_standardize(columns):
    col_low = [x.lower() for x in columns]
    col_clean = [s.translate(str.maketrans('', '', string.punctuation)) for s in col_low] 
    return col_clean


def column_check(df):
    st.subheader("Column Check \"Invdividual\"")
    
    df_col = df.columns.astype(str)
    df_col_clean = col_standardize(df_col)
    df_col_clean = df_col_clean[1:47]
    
    correct_col = ['company_id', 'company_name', 'year', 'person_id', 'name', 'annual_report', 'birth_date', 'gender', 'nationality', 'role code', 'position', 'election_form', 'independent', 'on_board', 'appointment_date', 'committee - audit', 'committee - nomination', 'committee - remuneration', 'committee - risk', 'step_down', 'months serving', 'comment', 'current_shares_a_number', 'current_shares_a_value', 'current_shares_b_number', 'current_shares_b_value', 'current_shares_total_number', 'current_shares_total_value', 'current_options_number', 'current_options_value', 'currency', 'base salary', 'bonus', 'total', 'award_total_value', 'award_options', 'award_options_number', 'award_options_value', 'award_shares', 'award_performance', 'award_restricted', 'award_tot_shares_value', 'award_tot_shares_number', 'pension_total', 'other_monetary', 'other_non_monetary']
    correct_col_clean = col_standardize(correct_col)
    
    st.write(df_col_clean)
    st.write(correct_col_clean)
     
    if (df_col_clean[1:47] == correct_col_clean):
        correct = True
        st.write("Columns check out!")
    else:
        correct = False
        st.write("The columns are not the same as the template. Make sure the first 41 columns are the same as in the template.")
    
    return correct


