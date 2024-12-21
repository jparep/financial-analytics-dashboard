import pandas as pd

def load_filtered_data(region, account_type):
    df = pd.read_csv('synthetic_banking_data.csv')
    return df[(df['Region'] == region) & (df['Account_Type'] == account_type)]
