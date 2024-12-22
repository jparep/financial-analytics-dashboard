import pandas as pd

# Load the DataFrame once at the module level
DATA_PATH = "./data/banking_data.csv"
df = pd.read_csv(DATA_PATH, parse_dates=["Date"])  # Parse "Date" upfront for efficiency

def load_filtered_data(region, account_type):
    """
    Filters the preloaded DataFrame based on region and account type.
    """
    return df[(df["Region"] == region) & (df["Account_Type"] == account_type)]

def get_monthly_transaction_data():
    """
    Groups transactions by month and calculates the total transaction amount.
    """
    df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()
    monthly_data = df.groupby("Month")["Transaction_Amount"].sum().reset_index()
    return monthly_data

def get_customer_segmentation():
    """
    Segments customers into categories based on their balance.
    """
    # Define balance categories
    conditions = [
        (df["Balance"] < 10000),
        (df["Balance"] >= 10000) & (df["Balance"] < 50000),
        (df["Balance"] >= 50000)
    ]
    categories = ["Low", "Medium", "High"]
    df["Balance_Category"] = pd.cut(
        df["Balance"], bins=[-1, 9999, 49999, float("inf")], labels=categories
    )
    segmentation = df.groupby("Balance_Category").size().reset_index(name="Customer_Count")
    return segmentation
