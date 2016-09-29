'''
Created on Feb 24, 2016

@author: cnamgoong
'''
import numpy as np
import re

def apply_map_rule(value,rulename):
    
    try:
        if rulename == 'KO_dot_right6': return KO_dot_right6(value)
        elif rulename == 'colon_KO_dot_right6': return colon_KO_dot_right6(value)
        elif rulename == 'add_bracket_add_2decimals': return add_bracket_add_2decimals(value)
        elif rulename == 'add_2decimals': return add_2decimals(value)
        elif rulename == 'Y_to_true':return Y_to_true(value)
        elif rulename == 'round_to_2decimal':return round_to_2decimal(value)
        elif rulename == 'replace_bar_with_comma':return replace_bar_with_comma(value) 
        elif rulename == 'asset_reset_freq_remap':return asset_reset_freq_remap(value)
        elif rulename == 'comma_list_of_num_add_10decimals':return comma_list_of_num_add_10decimals(value)
        elif rulename == 'add_colon':return add_colon(value)
        elif rulename == 'right7':return right7(value)
        elif rulename == 'left14':return left14(value)
        elif rulename == 'get_deal_num':return get_deal_num(value)
        elif rulename == 'not_in_scope': return not_in_scope(value)
        elif rulename == 'remove_colon': return remove_colon(value)
        elif rulename == 'currency_change': return currency_change(value)
        elif rulename == 'true_underlying': return true_underlying(value)
        elif rulename == 'change_datetype': return change_datetype(value)
        elif rulename == 'reset_freq': return reset_freq(value)
        else: return 'rule not in if-else tree'
    except:
        return value

def reset_freq(value):
    flag = str(value).strip()
    dict_case = {
                 'DAY' : 'Day'
                 ,'QURT' : ''
                 }
    new_flag = dict_case.get(flag,flag)
    return new_flag


def change_datetype(value):
    print value
    print "chan"
    dt = value.datetime.strptime(value,'%Y/%m/%d')
    print "seperate" + dt 
    new_dt = dt.datetime.strftime('%-m/%d/%y')
    print "new date" + new_dt
    return new_dt

def true_underlying(value):
    new_str = value.split('~')
    #if "CA" in str(new_str[0]) : return ':' + str(new_str[0])[4:-1]  
    #else : return ':' + str(new_str[0])[2:]
    return ':' + str(new_str[0])[2:]

def currency_change(value):
    flag = str(value).strip()
    dict_case = {
                'MXN' : 'USD'
                ,':USD' : ':MXN'
                }
    new_flag = dict_case.get(flag,flag)
    return new_flag

def remove_colon(value):
    return str(value)[1:]

def not_in_scope(value):
    return None

def get_deal_num(value):
    return str(value)[-7:]

def right7(value):
    return str(value)[-7:]

def left14(value):
    return str(value)[:14]

def round_to_2decimal(value):
    return np.round(value,0)

def KO_dot_right6(value):
    return 'KO' + value[-6:]

def colon_KO_dot_right6(value):
    return ':KO' + value[-6:]

def add_bracket_add_2decimals(value):
    date_num_USD = value.split(' ')
    return '(' + date_num_USD[0] + ' ' '{0:.2f}'.format(float(date_num_USD[1])) + ' ' +date_num_USD[2] + ')' 

def add_2decimals(value):
    num_USD = value.split(' ')
    return '{0:.2f}'.format(float(num_USD[0])) + ' ' +num_USD[1]

def Y_to_true(value):
    if value=='Y': return 'True'
    else: return value

def replace_bar_with_comma(value):
    #actually replacing with ', ', not ','
    return str(value).replace('|',', ')

def asset_reset_freq_remap(value):
    if str(value) in ('nan','NaT'):
        return value
        
    dict_case = {
                  'Mon': 'Month'
                }
    return dict_case.get(value,value)

def add_10decimals(value):
    return str('{0:.10f}'.format(float(value)))

def comma_list_of_num_add_10decimals(value):
    #
    #hmmm.... this function doesn't work correct right now.
    #
    if str(value) in ('nan','NaT'):
        return value
    
    if isinstance(value, np.ndarray):
        preprocess_str =  ', '.join([str(i) for i in value.tolist()])
    
    elif isinstance(value, basestring):
        preprocess_str =  str(value)
    
    else:
        print type(value)
        return 'missing case in mapping process'
    
    comma_list_val = preprocess_str.split(', ')
    #print comma_list_val
    return ', '.join([add_10decimals(i) for i in comma_list_val])
    
def add_colon(value):
    return ':' + str(value)

