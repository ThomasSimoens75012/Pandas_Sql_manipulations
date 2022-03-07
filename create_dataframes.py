import pandas as pd
import format_datas as fd


df_companies = pd.read_excel(r'datas/Gymlib_data_entretien.xlsx', sheet_name='Companies', header=None)
df_companies = df_companies.fillna(method='ffill', axis=1) 
df_pass = pd.read_excel(r'datas/Gymlib_data_entretien.xlsx', sheet_name='Pass')
df_users = pd.read_excel(r'datas/Gymlib_data_entretien.xlsx', sheet_name='Utilisateurs')
 
  
df_companies_formatted = fd.format_df_companies(df_companies)    

df_companies_08_2019 = fd.create_df_companies_date(df_companies, '08/2019')
df_companies_09_2019 = fd.create_df_companies_date(df_companies, '09/2019')
df_companies_10_2019 = fd.create_df_companies_date(df_companies, '10/2019')


df_pass = fd.format_df_pass(df_pass)   
df_users.columns = [fd._field_name_to_db_format(col) for col in list(df_users)]

