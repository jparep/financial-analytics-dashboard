import pandas as pd

# Load the dataset once at the module level
DATA_PATH = "./data/banking_data.csv"
df = pd.read_csv(DATA_PATH, parse_dates=["Date"])  # Parse dates upfront

def get_data():
    """
    Returns a copy of the entire dataset to ensure immutability.
    """
    return df.copy()

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
    return filtered_df.groupby("Month")["Transaction_Amount"].sum().reset_index()

def get_customer_segmentation(filtered_df):
    """
    Segments filtered data into categories based on balances.
    """
    categories = ["Low", "Medium", "High"]
    filtered_df["Balance_Category"] = pd.cut(
        filtered_df["Balance"],
        bins=[-1, 9999, 49999, float("inf")],
        labels=categories,
    )
    return filtered_df.groupby("Balance_Category").size().reset_index(name="Customer_Count")

def filter_data_by_criteria(regions=None, account_types=None):
    """
    Filters the dataset based on regions and account types.
    """
    filtered_df = df.copy()
    if regions:
        filtered_df = filtered_df[filtered_df["Region"].isin(regions)]
    if account_types:
        filtered_df = filtered_df[filtered_df["Account_Type"].isin(account_types)]
    return filtered_df
