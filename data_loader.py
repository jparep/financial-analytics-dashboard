import pandas as pd

def load_filtered_data(region, account_type):
    # Load the dataset
    df = pd.read_csv("./data/banking_data.csv")
    # Filter data based on the selected region and account type
    return df[(df["Region"] == region) & (df["Account_Type"] == account_type)]

def get_monthly_transaction_data():
    # Load the dataset
    df = pd.read_csv("./data/banking_data.csv", parse_dates=["Date"])
    # Group by month and calculate total transaction amount
    df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()
    monthly_data = df.groupby("Month")["Transaction_Amount"].sum().reset_index()
    return monthly_data
