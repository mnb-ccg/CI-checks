# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:04:32 2021

@author: mnb.ccg
"""
import os
import re
import pandas as pd



def find_country_files(path, country_ISO):
    file_list = os.listdir(path)
    pattern = re.compile(country_ISO)
    files = list(filter(pattern.match, file_list))

    return files


def load_files_df(path, file_names, name_sheet):
    
    ret_list = []
    for file_name in file_names:
        sheet_path = path + '\\' + file_name
        single_year_df = pd.read_excel(sheet_path, sheet_name= name_sheet)
        ret_list.append(single_year_df)

        
    ret_df = -1
    if (len(ret_list) == 1):
        ret_df = pd.DataFrame(ret_list[0])
    else:
        ret_df = pd.concat(ret_list)
    return ret_df


def read_and_append(path, file_names, name_sheet):
    
    column_names = ['company_id', 'company_name', 'year', 'person_id', 'name', 'annual_report', 'birth_date', 'gender', 'nationality', 'role code', 'position', 'election_form', 'independent', 'on_board', 'appointment_date', 'committee - audit', 'committee - nomination', 'committee - remuneration', 'committee - risk', 'step_down', 'months serving', 'comment', 'current ownership - a-shares', 'current ownership - b-shares', 'current ownership - p-options', 'current ownership - t-options', 'currency', 'base salary', 'bonus', 'total salary', 'bonus.1', 'incentives', 'share-based incentive schemes - total', 'long-t', 'short-t', "stock opt's", 'p shares', 'r shares', 'pension - total', 'monetary', 'non-mon.']
    
    ret_list = []
    for file_name in file_names:
        sheet_path = path + '\\' + file_name
        single_year_df = pd.read_excel(sheet_path, sheet_name= name_sheet)
        single_year_df.columns = column_names
        single_year_df['company_id'] = single_year_df['company_id'].astype(str)
        print(file_name + " shape", single_year_df.shape)
        ret_list.append(single_year_df)

        
    ret_df = -1
    if (len(ret_list) == 1):
        ret_df = pd.DataFrame(ret_list[0])
    else:
        ret_df = pd.concat(ret_list)
    return ret_df