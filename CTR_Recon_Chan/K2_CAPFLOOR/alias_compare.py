'''
Created on Aug 15, 2016

@author: cnamgoong
'''
import pandas as pd, os, numpy as np

#in files
in_CTR_folder = 'C:/Users/cnamgoong/Desktop/Shared/RW/CTR Files/2016-08-10-PROD/'
in_CTR_file = 'MXNOPICS/' + 'MXNOPICS_FX_Option(OTC)_D_20160810_27_RiskWatch.csv'
in_VAR_folder = 'C:/Users/cnamgoong/Desktop/Shared/RW/VAR Session/market.16.08.10/all/ByProduct/'
in_VAR_file = 'out_20160812_deals_BNS_FX_Option.csv'
in_alias_folder = 'C:/Users/cnamgoong/Desktop/Shared/RW/CTR Files/2016-08-10-PROD/map/'
in_alias_file = 'alias.xlsx'


#load data
df_CTR = pd.read_csv(in_CTR_folder+in_CTR_file)
df_VAR = pd.read_csv(in_VAR_folder+in_VAR_file)
df_alias = pd.read_excel(in_alias_folder+in_alias_file)

print len(df_CTR.columns)
print len(df_VAR.columns)
print len(df_alias.columns)

#out files
out_file_alias_columns_diff = 'out_MXNOPICS/' + 'out_MXNOPICS_FXOption_diff_alias_columns_diff.csv'

#output difference in columns
df_CTR_col = pd.DataFrame({'in_CTR':['Y' for col in df_CTR.columns]},index=df_CTR.columns) 
df_VAR_col = pd.DataFrame({'in_VAR':['Y' for col in df_VAR.columns]},index=df_VAR.columns)
df_merge_col = pd.concat([df_CTR_col,df_VAR_col],axis=1)
df_merge_col.sort_index(axis=0,inplace=True)


common_names = np.intersect1d(df_merge_col.index, df_alias)
df_merge_col['alias_of'] = df_merge_col.loc[col for col in common_names,df_alias.columns]


df_merge_col.to_csv(in_CTR_folder + out_file_alias_columns_diff)