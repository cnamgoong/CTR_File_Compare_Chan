'''
Created on Aug 10, 2016

@author: cnamgoong
'''
import numpy as np
import re

def apply_map_rule(value,rulename):
    
    try:
        if rulename == 'change_flag': return change_flag(value)
        elif rulename == 'boolean_maker': return boolean_maker(value)
        elif rulename == 'pay_holiday' : return pay_holiday(value)
        elif rulename == 'not_in_scope': return not_in_scope(value)        
        elif rulename == 'average_frequency' : return average_frequency(value)
        elif rulename == 'ctr_to_var_name' : return ctr_to_var_name(value)
        elif rulename == 'special_frequency' : return special_frequency(value)
        elif rulename == 'cap_frequency' : return cap_frequency(value)
        elif rulename == 'ctr_id_changer' : return ctr_id_changer(value)
        elif rulename == 'ctr_daycount_changer' : return ctr_daycount_changer(value)
        elif rulename == 'change_datetype' : return change_datetype(value)
        elif rulename == 'numstr' : return numstr(value)
        elif rulename == 'numnum' : return numnum(value)
        elif rulename == 'paylagconvention' : return paylagconvention(value)
        elif rulename == 'holiday_org' : return holiday_org(value)
        elif rulename == 'mode_change' : return mode_change(value)
        else: return 'rule not in if-else tree'
    except:
        return value

def mode_change(value):
    val = value.strip()
    val = val.replace(" ","_")
    return val


def holiday_org(value):
    val = str(value).strip()
    val = val.replace(";",",")
    print val
    val = val.split(",")
    hol = sorted(val)
    hol = ';'.join(hol)
    return hol

def ctr_id_changer(value):
    val = str(value).strip()
    id = val.split(".")[1]
    return ":" + id

def numstr(value):
    val = value.strip()
    val = int(val)
    val = str(val)
    return val

def numnum(value):
    val = value.strip()
    val = int(val)
    return val

def change_datetype(value):
    val = str(value).strip()
    dates = val.split("-")[0]
    year = val.split("-")[2]
    mon = val.split("-")[1]
    dict_case = {
                'JAN' : '01'
                ,'FEB' : '02'
                ,'MAR' : '03'
                ,'APR' : '04'
                ,'MAY' : '05'
                ,'JUN' : '06'
                ,'JUL' : '07'
                ,'AUG' : '08'
                ,'SEP' : '09'
                ,'OCT' : '10'
                ,'NOV' : '11'
                ,'DEC' : '12'
                }
    new_mon = dict_case.get(mon,mon)
    new_date = int(dates)
    new_date = str(new_date)
    new_time = "20" + year + "/" + new_mon + "/" + new_date  
    print new_time
    return new_time

def ctr_daycount_changer(value):
    flag = str(value).strip()
    dict_case = {
                'ACT/360' : 'actual/360'
                , 'ACT/365' : 'actual/365'
                , 'ACT360' : '30/360'
                }
    new_flag = dict_case.get(flag,flag)
    return new_flag

def paylagconvention(value):
    return "Business"

def cap_frequency(value):
    flag = str(value).strip()
    dict_case = {
                '28-Day' : '28DAY'
                , 'Month' : 'MON'
                , 'Quarter' : 'QURT'
                , 'semi-annual' : 'SEMI'
                }
    new_flag = dict_case.get(flag,flag)
    return new_flag

def ctr_to_var_name(value):
    value = str(value).strip()
    value = str(value)[3:]
    return value

def not_in_scope(value):
    value = value.strip()
    return None

def change_flag(value):
    value = str(value.strip())
    dict_case = {
                'Sell' : '-1'
                ,'Buy' : '1'
                }
    return dict_case.get(value,value)

def boolean_maker(value):
    flag = str(value).strip()
    dict_case = {
                 'N' : 'False'
                 ,'Y' : 'True'
                 }
    new_flag = dict_case.get(flag,flag)
    return new_flag

def average_frequency(value):
    flag = str(value).strip()
    dict_case = {
                'Month' : 'MON'
                }
    new_flag = dict_case.get(flag,flag)
    return new_flag

def special_frequency(value):
    flag = str(value).strip()
    dict_case = {
                'Month' : 'MONTH'
                }
    new_flag = dict_case.get(flag,flag)
    return new_flag

def pay_holiday(value):
    flag = str(value).strip()
    dict_case = {
                'Err_03' : 'LON;NYC'
                }
    new_flag = dict_case.get(flag,flag)
    return new_flag
