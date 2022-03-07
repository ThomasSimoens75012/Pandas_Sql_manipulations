import regex as re
import unidecode
import numpy as np
import pandas as pd



def field_name_to_db_format(column_name):
    """
    transforms the string passed into a sequence of alphanumeric characters in lower case
    any non alphanumeric characters will be deleted, the alphanumeric numeric characters will then
    be joined with underscores

        Parameters:
            :param column_name: The string to format -> str

        Returns:
            if input: '//:ZErt88//:fdgg__Xkf'
            output: 'zert88_fdgg_xkf'
    """
    pattern = '[_\W]'
    l = re.split(pattern, unidecode.unidecode(column_name.lower()))
    string_to_return_list = []
    for element in l:
        if element != '':
            string_to_return_list.append(element)
    string_to_return = '_'.join(string_to_return_list)
    return string_to_return


def format_df_companies(raw_df):
    raw_df = raw_df.fillna(method='ffill', axis=1) 
    raw_df.columns = raw_df.iloc[0]
    raw_df = raw_df.drop(0)
    raw_df.columns = [field_name_to_db_format(col) for col in list(raw_df)]
    return raw_df


def format_df_pass(raw_df):
    raw_df.columns = ['code', 'gym_id', 'date', 'user_id', 'companyid', 'total_par_pass']
    raw_df = raw_df.astype({'code': 'int', 'gym_id': 'string', 'user_id': 'string', 'companyid': 'string', 'total_par_pass': 'float'})
    raw_df['date'] = pd.to_datetime(raw_df['date'])
    return raw_df


def format_df_users(raw_df):
    raw_df = raw_df.replace('N\\A', 0).replace(np.nan, 0)
    raw_df = raw_df.replace('Utilisateur anonyme', 0).replace('7501i', 75011).replace(75116, 75016).replace(75914, 75014)
    raw_df.columns = [field_name_to_db_format(col) for col in list(raw_df)]
    raw_df = raw_df.astype({'id': 'string', 'companyid': 'string','zipcode': 'int', 'country': 'string', 'age' : 'int', 'statut_user': 'string'})
    return raw_df


def create_df_companies_date(df_companies, date): 
    df_companies_date = df_companies[date]
    df_companies_date.columns = df_companies_date.iloc[0]
    df_companies_date = df_companies_date.drop([1])
    
    companyid = df_companies['companyid'].dropna()
    df_companies_date.insert(0, 'companyid', companyid)
    df_companies_date['date'] = date
    df_companies_date.columns = [field_name_to_db_format(col) for col in list(df_companies_date)]
    return df_companies_date
