'''
Created on Aug 10, 2016

@author: cnamgoong
'''
import pandas as pd, os
from Map_Rules import apply_map_rule

#in CTR files
in_folder = 'C:/Users/cnamgoong/Desktop/Shared/RW/CTR Files/2016-09-22-DEV/'
in_file_cross_currency_swap = 'K2/K2_Cross_Currency_Swap_D_20160922_5_RiskWatch.csv'
in_file_interest_rate_swap = 'K2/K2_Interest_Rate_Swap_D_20160922_5_RiskWatch.csv'
in_file_inflation_linked_swap = 'K2/K2_Inflation_Linked_Swap_D_20160922_5_RiskWatch.csv'


#in map files
map_folder = in_folder
map_file = 'map/map_K2_Swap.csv'

#out files
out_folder = in_folder + 'out_K2/'
out_file = 'out_K2_Swap_CTR_preprocessed_file.csv'

#open in_files
df_K2_cross_currency_swap = pd.read_csv(in_folder+in_file_cross_currency_swap)
df_K2_interest_rate_swap = pd.read_csv(in_folder+in_file_interest_rate_swap)
df_K2_inflation_linked_swap = pd.read_csv(in_folder+in_file_inflation_linked_swap)


#Merge 2 CTR files/dataframes into 1 file/dataframe
df_merge = pd.concat([df_K2_cross_currency_swap, df_K2_interest_rate_swap, df_K2_inflation_linked_swap],axis=0)
df_merge.reset_index(inplace=True,drop=True)

#drop the deals with Issue Date = File Creation Date
#df_merge = df_merge[(~df_merge['Issue Date'].str.contains("2016/09/27"))]

#reorder columns
df_merge.sort_index(axis=1,inplace=True)

#apply mapping rules
df_map = pd.read_csv(map_folder+map_file)
for i in df_map['Column Name'].index:
    this_col = str(df_map.at[i,'Column Name'])
    this_map_rule = str(df_map.at[i,'CTR Map Rule'])
    
    #apply the mapping rule if rule 'not nan/blank'
    if not this_map_rule == 'nan':
        for j in df_merge.index:
            df_merge.at[j, this_col] = apply_map_rule(df_merge.at[j, this_col], this_map_rule) 

#sort the CTR dataframe by Name
sort_col = 'Name'

#write out_files
try: os.stat(out_folder[:-1])
except: os.mkdir(out_folder[:-1])

#df_merge.to_csv(out_folder + out_file_merged,index=False,columns=out_cols_FX_Deals)
df_merge.to_csv(out_folder + out_file,index=False)

print 'done.'
print 'from ' + in_folder
print 'to ' + out_folder