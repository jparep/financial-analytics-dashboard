import pandas as pd

# Load the dataset once
DATA_PATH = "./data/banking_data.csv"
df = pd.read_csv(DATA_PATH, parse_dates=["Date"])  # Parse dates upfront

def filter_data(region=None, account_type=None):
    """
    Filters the dataset based on the provided criteria (region and account type).
    If no filters are provided, returns the full dataset.
    """
    filtered_df = df.copy()

    if region:
        filtered_df = filtered_df[filtered_df["Region"] == region]
    if account_type:
        filtered_df = filtered_df[filtered_df["Account_Type"] == account_type]

    return filtered_df

def get_monthly_transaction_data(filtered_df):
    """
    Groups filtered data by month and calculates the total transaction amount.
    """
    filtered_df["Month"] = filtered_df["Date"].dt.to_period("M").dt.to_timestamp()
    monthly_data = filtered_df.groupby("Month")["Transaction_Amount"].sum().reset_index()
    return monthly_data

def get_customer_segmentation(filtered_df):
    """
    Segments filtered data into categories based on balances.
    """
    # Define balance categories
    conditions = [
        (filtered_df["Balance"] < 10000),
        (filtered_df["Balance"] >= 10000) & (filtered_df["Balance"] < 50000),
        (filtered_df["Balance"] >= 50000)
    ]
    categories = ["Low", "Medium", "High"]
    filtered_df["Balance_Category"] = pd.cut(
        filtered_df["Balance"], bins=[-1, 9999, 49999, float("inf")], labels=categories
    )
    segmentation = filtered_df.groupby("Balance_Category").size().reset_index(name="Customer_Count")
    return segmentation
