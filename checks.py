# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:34:31 2021

@author: mnb.ccg
"""

import streamlit as st
#import importing_files as imfil
import matplotlib.pyplot as plt
#import numpy as np
import string
import math
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

def check_if_nan(value):
    if (type(value) == float):
        if(math.isnan(value)):
            return True
    return False

def col_standardize(columns):
    col_low = [x.lower() for x in columns]
    col_clean = [s.translate(str.maketrans('', '', string.punctuation)) for s in col_low] 
    return col_clean


###
def column_check(df, sheet):
    
    df_col = df.columns.astype(str)
    #df_col_clean = col_standardize(df_col)
    
    if(sheet == 'Individual'):
        templ_col = column_names_i
        #templ_col_clean = col_standardize(templ_col)
    elif(sheet == 'Company'):
        templ_col = column_names_c
        #templ_col_clean = col_standardize(templ_col)
    else:
        st.error("Sheet name not recognized")
        
    
    correct = False
    df_set = set(df_col)
    templ_set = set(templ_col)
    missing_columns = templ_set - df_set
    excess_columns = df_set - templ_set
    

    if (len(missing_columns) == 0):
        correct = True
        st.success("Columns passed the check")
    else:
        correct = False
        st.error("The columns are not the same as the template.")
        st.error("These columns were not found in the uploaded dataset:")
        st.write(missing_columns)
        st.warning("These columns were found in the dataset, but not in the template:")
        st.write(excess_columns)

    return correct
###

###
def check_year_length(year):
    comment = ""
    if(len(str(year)) == 4):
        return comment
    if(len(str(year)) != 4):
        comment = "year: Not correct format, should be a 4 digit number | "
        return comment


def check_year(df):
    df_check = df['year'].apply(check_year_length)
    return df_check
###


###
def date_split(date):
    try:
        split_date = date.split("-")
    except AttributeError:
        print("AttributeError, most likely nan value")
        split_date = []
        

    if(len(split_date) == 3):
        days = split_date[2]
        months = split_date[1]
        years = split_date[0]
        return days, months, years, True
    else:
        days = 32
        months = 13
        years = 0     
        return days, months, years, False

def check_date_format(date, column):
    comment = ""
    ## Do we accept that dates are nan values?
    if (type(date) == float):
        if(math.isnan(date)):
            return comment
    
    days, months, years, bool_split = date_split(date)
    
    if (bool_split == True):
        days_b0 = (len(days) == 2)
        
        try:
            st.write(days)
            days_b1 = (int(days) <= 31)
        except ValueError:
            pass
            
        days_b1 = days in 'X XX x xx'
        
        
        months_b0 = (len(months) == 2)
        try:
            months_b1 = (int(months) <= 12)
            st.write(months)
        except ValueError:
            pass
        
        months_b1 = months in 'X XX x xx'
        
        
        years_b0 = (len(years) == 4)
        
        try:
            years_b1 = ((int(years)<=2030) and (int(years)>1900))
            st.write(years)
        except ValueError:
            pass
        
        years_b1 = years in 'X XX XXX XXXX x xx xxx xxxx'
        
        
        bool_cd = (days_b0 and days_b1 and months_b0 and months_b1 and  years_b0 and years_b1)
        st.write(bool_cd)
        st.write(days_b1)
        st.write(months_b1)
        st.write(years_b1)
        if (bool_cd == True):
            return comment
        else:
            comment = column + ": Wrong format. Ensure YYYY-MM-DD | "
            return comment
    
    else:
        comment = column + ": Wrong format. Ensure YYYY-MM-DD | "
        return comment
    

def check_date(df, column):
    df_check = df.apply(lambda x: check_date_format(x[column], column), axis=1)
    return df_check
###


###
def check_rc_format(rc):
    comment = ""
    if (type(rc) == float):
        if(math.isnan(rc)):
            return comment
        
    if(rc == 'EXECUTIVE' or rc == 'BOARD'):
        return comment
    else: 
        comment = "role_code: Should be either 'EXECUTIVE' or 'BOARD' | "
        return comment


def check_role_code(df):
    df_check = df['role_code'].apply(check_rc_format)
    # bool_cd = df_check.all()
    # faulty_rows = df[df_check == False]
    return df_check
###


###
def check_position_format(inp):
    comment = ""
    board_pos = ['CHAIRMAN', 'VICECHAIRMAN', 'BOARD MEMBER', 'DEPUTY BOARD MEMBER']
    
    rc, pos = inp.split(",")
    
    if ((rc == "nan") or (pos == "nan")):
        comment = "position: Should not be empty |"
        return comment
        
    elif((rc == 'EXECUTIVE') and (len(pos)>0)):
        return comment
    
    elif ((rc == 'BOARD') and (pos in board_pos)):
        return comment
    
    else: 
        comment = "position: Does not fit specifications, e.g. if role_code = 'BOARD', must be e.g. 'CHAIRMAN' or 'BOARD MEMBER' | "
        return comment


def check_position(df):
    new_df = df.copy()
    new_df['key'] = df['role_code'].astype(str) + "," + df['position'].astype(str) 
    df_check = new_df['key'].apply(check_position_format)
    return df_check
###



###
def check_nationality_format(nat):
    comment = ""
    if (type(nat) == float and math.isnan(nat)) :
        return comment
    elif(len(nat) == 2):
        return comment
    else:
        comment = "nationality: Should adhere to the two letter ISO2 codes, e.g. US | "
        return comment
    
    

def check_nationality(df):
    new_df = df.copy()
    df_check = new_df['nationality'].apply(check_nationality_format)
    return df_check
###

### 
def apply_type(line, column, type_inp):
    comment = ""
    if(type(line) == float and math.isnan(line)):
        return comment
    
    if(type_inp == 'int'):
        try:
            int(line)
            return comment
        except (ValueError, TypeError):
            comment = column + ": " + "This should be a non-decimal number"  + " | "
            return comment  
        
    elif(type_inp == 'float'):
        try:
            float(line)
            return comment
        except (ValueError, TypeError):
            comment = column + ": " +  "This should be a number"  + " | "
            return comment
        
    elif(type_inp == 'dummy'):
        try:
            dummy = int(line)
            if(dummy == 0 or dummy == 1):
                return comment
            else:
                comment = column + ": " +  "This should be either a 0 or a 1"  + " | "
                return comment
        except (ValueError, TypeError):
            comment = column + ": " +  "This should be either 0 or 1" + " | "
            return comment
        
    else:
        return comment

        
    

def check_type(df, column, type_inp):
    new_df = df.copy()
    df_check = new_df.apply(lambda x: apply_type(x[column], column, type_inp), axis=1)
    return df_check
    
###