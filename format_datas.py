import pandas as pd
import regex as re
import unidecode



def _field_name_to_db_format(column_name):
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
    raw_df.columns = raw_df.iloc[0]
    raw_df = raw_df.drop(0)
    return raw_df


def create_df_companies_date(df_companies, date):   
    
    df_companies_date = df_companies[date]
    df_companies_date.columns = df_companies_date.iloc[1]
    df_companies_date = df_companies_date.drop([0, 1])
    
    company_id = df_companies['CompanyId'].dropna()
    df_companies_date.insert(0, 'company_id', company_id)
    df_companies_date.columns = [_field_name_to_db_format(col) for col in list(df_companies_date)]

    return df_companies_date


def format_df_pass(raw_df):
    raw_df.columns = ['code', 'gym_id', 'date', 'user_id', 'company_id', 'total_par_pass']
    return raw_df