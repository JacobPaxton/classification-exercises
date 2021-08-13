from env import username, host, password
import pandas as pd

def prep_iris(iris_df):
    df = iris_df.copy()
    df.drop(columns=['species_id', 'measurement_id'], inplace=True)
    df.rename(columns={'species_name':'species'}, inplace=True)
    dummy_df = pd.get_dummies(df[['species']], dummy_na=False, drop_first=True)
    return dummy_df