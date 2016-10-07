'''
Created on Aug 10, 2016

@author: cnamgoong
'''
import pandas as pd
from Map_Rules import apply_map_rule

#control variables
bWriteReport = 1

#in VAR files
in_folder = 'C:/Users/cnamgoong/Desktop/Shared/RW/VAR Session/market.16.09.27/'
in_file_Swap = 'all/ByProduct/out_20160929_deals_BNS_Swap.csv' 

#in mapping rule files
map_folder = 'C:/Users/cnamgoong/Desktop/Shared/RW/CTR Files/2016-09-22-DEV/'
map_file = 'map/map_K2_Swap.csv'

#out folder
out_folder = map_folder
out_file_Swap_Deals =  'out_K2/' + 'out_K2_Swap_VAR_preprocessed_file.csv'

#open in_files
df_Swap = pd.read_csv(in_folder+in_file_Swap)
#print len(df_TRS.index)

#filter 

import csv
with open('C:/Users/cnamgoong/Desktop/Shared/RW/VAR Session/market.16.09.27/all/file_list.csv') as f:
    lis = [x.split() for x in f]
cols = [x for x in zip(*lis)]
for x in cols:
    print (x)
file_list_in_scope = (x)
#file_list_in_scope = ['/__bns__derivProdData__riskWatch__ABS__CAD__Sybase_K2.csv'
#                      ,'/__bns__derivProdData__riskWatch__ADMINRES__CAD__Sybase_K2.csv'
#                      ,'/__bns__derivProdData__riskWatch__ADMINRES__EUR__Sybase_K2.csv'
#
#                      ,'/__bns__derivProdData__riskWatch__SWAPS_BOOK__USD__Sybase_K2.csv']
df_merge = df_Swap[(df_Swap.Filename.isin(file_list_in_scope))]
df_merge.reset_index(inplace=True,drop=True)
print len(df_merge.index)

print df_merge['Filename']
#reorder columns
df_merge.sort_index(axis=1,inplace=True)

#open mapping rules
df_map = pd.read_csv(map_folder+map_file)

#apply transformation for alias
#copy alias values to real column and drop alias column
for i in df_map[~df_map['RW Alias'].isnull()].index:
    #assume only 1 alias per column for now
    this_col = str(df_map.at[i,'Column Name'])
    this_alias = str(df_map.at[i,'RW Alias'])
    
    #copy alias values to 'this_col'
    for j in df_merge[~df_merge[this_alias].isnull()].index:
        df_merge.at[j,this_col] = df_merge.at[j,this_alias] 
    
    #drop alias column
    df_merge.drop([this_alias],axis=1,inplace=True)

#now apply 'within-cell' mapping rules
for i in df_map['Column Name'].index:
    this_col = str(df_map.at[i,'Column Name'])
    this_map_rule = str(df_map.at[i,'RW Map Rule'])
    
    #apply the mapping rule if rule 'not nan/blank'
    if not this_map_rule == 'nan':
        for j in df_merge.index:
            df_merge.at[j, this_col] = apply_map_rule(df_merge.at[j, this_col], this_map_rule) 

#sort by Name
df_merge.sort('Name', inplace = True)

#write out_files
df_merge.to_csv(out_folder + out_file_Swap_Deals,index=False)

print 'done.'
print 'from ' + in_folder
print 'to ' + out_folder