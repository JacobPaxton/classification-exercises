from env import username, host, password
import os
import pandas as pd

def get_titanic_data(db_name='titanic_db', username=username, hostname=host, password=password):
    if os.path.isfile('titanic.csv'):
        return pd.read_csv('titanic.csv')
    else:
        url = f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'
        sql = 'SELECT * FROM passengers'
        return pd.read_sql(sql, url)

def get_iris_data(db_name='iris_db', username=username, hostname=host, password=password):
    if os.path.isfile('iris.csv'):
        return pd.read_csv('iris.csv')
    else:
        url = f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'
        sql = 'SELECT * FROM measurements JOIN species USING(species_id)'
        return pd.read_sql(sql, url)
