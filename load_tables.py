import sqlite3
from create_dataframes import df_companies_08_2019, df_companies_09_2019, df_companies_10_2019, df_users, df_pass



con = sqlite3.connect('entretien_gymlib.db')
df_companies_08_2019.to_sql('companies_08_2019', con, index=False)
df_companies_09_2019.to_sql('companies_09_2019', con, index=False)
df_companies_10_2019.to_sql('companies_10_2019', con, index=False)
df_users.to_sql('users', con, index=False)
df_pass.to_sql('pass', con, index=False)
