'''
Created on Aug 10, 2016

@author: cnamgoong
'''
import numpy as np
import re

def apply_map_rule(value,rulename):
    
    try:
        if rulename == 'change_flag': return change_flag(value)
        elif rulename == 'true_to_Y_and_false_to_N': return true_to_Y_and_false_to_N(value)
        elif rulename == 'null_in_var': return ""    
        elif rulename == 'varstr_rate' : return varstr_rate(value)
        elif rulename == 'round_notional' : return round_notional(value)
        elif rulename == 'ctrstr_rate' : return ctrstr_rate (value)
        elif rulename == 'ctr_to_var_name' : return ctr_to_var_name(value)
        elif rulename == 'change_freq' : return change_freq(value)
        elif rulename == 'space_to_underline' : return space_to_underline(value)
        elif rulename == 'id_change' : return id_change(value)
        elif rulename == 'capitalize' : return capitalize(value)
        elif rulename == 'numnum' : return numnum(value)
        elif rulename == 'numnum_zero' : return numnum_zero(value)
        elif rulename == 'spec_units' : return spec_units(value)
        elif rulename == 'false_to_true' : return false_to_true(value)
        elif rulename == 'falser' : return falser(value)
        elif rulename == 'fraction_index' : return fraction_index(value)
        elif rulename == 'holiday_org' : return holiday_org(value)
        elif rulename == 'round_two_decimals_with_currency' : return round_two_decimals_with_currency(value)
        elif rulename == 'round_two_decimals_no_currency' : return round_two_decimals_no_currency(value)
        elif rulename == 'remove_bracket' : return remove_bracket(value)
        elif rulename == 'remove_bracket_round_notional_two_decimals' : return remove_bracket_round_notional_two_decimals(value)
        else: return 'rule not in if-else tree'
    except:
        return value


def holiday_org(value):
    val = str(value).strip()
    val = val.replace(";",",")
    val = val.split(",")
    hol = sorted(val)
    hol = ';'.join(hol)
    return hol

def remove_bracket(value):
    val = value.strip()
    if val[:1] == '(':
        val = val[1:-1]
    else:
        val
    return val

def remove_bracket_round_notional_two_decimals(value):
    val = value.strip()
    if val[:1] == '(':
        val = val[1:-1]
        new_val_list = ""
        new_val_amount = ""
        new_val_amount1 = ""
        if '|' in val:
            split_str = val.split('|')
            for i in split_str:
                new_val_date = i.split(' ')[0]
                new_val_amount = str(i.split(' ')[1])
                new_val_currency = i.split(' ')[2]
                amount = 0.00
                amount = float(new_val_amount)
                amount = "%0.2f" % amount
                new_val = new_val_date + " " + amount + " " + new_val_currency
                new_val_list = new_val_list + " | " + new_val
            new_val_list = new_val_list[3:]
            value_output = new_val_list
        else:
            new_val_date1 = val.split(' ')[0]
            new_val_amount1 = val.split(' ')[1]
            new_val_currency1 = val.split(' ')[2]
            amount1 = 0.00
            amount1 = float(new_val_amount1)
            amount1 = "%0.2f" % amount1
            new_val1 = new_val_date1 + " " + amount1 + " " + new_val_currency1
            new_val_list = new_val1
        value_output = new_val_list
    else:
        value_output = str(val)
    print value_output
    return value_output

def round_two_decimals_no_currency(value):
    val = value.strip()
    new_val_list = ""
    if ',' in val:
        split_str = val.split(',')
        for i in split_str:
            if '.' not in i:
                new_val = i[:-4] + ".00"
                new_val_list = new_val_list + " |" + new_val
            else:
                split_i = i.split('.')[1]
                if split_i[1:2] == " ":
                    new_val = i[:-4] + "0"
                    new_val_list = new_val_list + " |" + new_val
                else:
                    new_val_list = new_val_list + " |" + i[:-4]
        new_val_list = new_val_list[2:]
    else:
        if '.' not in val:
            new_val_list = val[:-4] + ".00"
    return new_val_list
    
def round_two_decimals_with_currency(value):
    val = value.strip()
    new_val_list = ""
    if ',' in val:
        split_str = val.split(',')
        for i in split_str:
            if '.' not in i:
                new_val = i[:-4] + ".00" + i[-4:]
                new_val_list = new_val_list + " |" + new_val
            else:
                split_i = i.split('.')[1]
                if split_i[1:2] == " ":
                    new_val = i[:-4] + "0" + i[-4:]
                    new_val_list = new_val_list + " |" + new_val
                else:
                    new_val_list = new_val_list + " |" + i
        new_val_list = new_val_list[2:]
    else:
        if '.' not in val:
            new_val_list = val[:-4] + ".00" + val[-4:]
    return new_val_list

def falser(value):
    val = value.strip()
    val = "False"
    return val

def fraction_index(value):
    val = value.strip()
    if val == 1:
        val = ""
    return val

def numnum_zero(value):
    val = value.strip()
    if val == "":
        val = 0.0
    return val

def numnum(value):
    val = value.strip()
    val = float(val)
    return val

def false_to_true(value):
    if str(value.strip()) == 'False':
        return 'True'
    else:
        return value

def id_change(value):
    val = value.strip()
    val = val.split(".")[1]
    return ":" + val

def spec_units(value):
    val = value.strip()
    dict_case = {
                'ANNUAL' : 'YEAR'
                ,'Month' : 'MONTH'
                ,'year' : 'YEAR'
                ,'Annual' : 'YEAR'
                }
    return dict_case.get(value,value)

def capitalize(value):
    val = value.strip()
    val = val.upper()
    return val

def space_to_underline(value):
    val = value.strip()
    val = val.replace(" ","_")
    return val

def change_freq(value):
    value = str(value.strip())
    dict_case = {
                '28-day' : '28DAY'
                ,'84-day' : '84DAY'
                ,'91-day' : '91DAY'
                ,'annu' : 'ANNU'
                ,'Annual' : 'ANNU'
                ,'Month' : 'MON'
                ,'qurt' : 'QURT'
                ,'semi-annual' : 'SEMI'
                }
    return dict_case.get(value,value)

def ctr_to_var_name(value):
    value = str(value).strip()
    value = str(value)[3:]
    return value

def round_notional(value):
    amount = str(value)[:-3]
    amount = amount.split(".")[0]
    return amount.strip()


def ctrstr_rate(value):
    val = str(value).strip()
    perc = val.split(" %")[0]
    new_perc = round(perc, 6)
    return new_perc + " % ANNU"

def varstr_rate(value):
    val = str(value).strip()
    perc = val.split(" %")[0]
    perc = perc.rstrip("0") #remove trailing zeros from numbers
    if str(perc)[0] == '-' :
        if str(perc)[1] == '0' :
            perc = '-' + str(perc)[2:]
        else : 
            perc = str(perc)[1:]
    elif str(perc)[0] == '0':
        perc = str(perc)[1:]
    return perc + " % ANNU"
    
def change_flag(value):
    value = str(value.strip())
    dict_case = {
                'Sell' : '-1'
                ,'Buy' : '1'
                }
    return dict_case.get(value,value)

def true_to_Y_and_false_to_N(value):
    flag = str(value).strip()
    dict_case = {
                 'False' : 'N'
                 ,'True' : 'Y'
                 }
    new_flag = dict_case.get(flag,flag)
    return new_flag

