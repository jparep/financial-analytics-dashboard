import pandas as pd

def load_filtered_data(region, account_type):
    # Load the dataset
    df = pd.read_csv("synthetic_banking_data.csv")
    # Filter data based on the selected region and account type
    return df[(df["Region"] == region) & (df["Account_Type"] == account_type)]
