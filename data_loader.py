import pandas as pd

# Load the dataset once at the module level (lazy loading for efficiency)
DATA_PATH = "./data/banking_data.csv"

def load_data():
    """
    Lazy loads the dataset, parsing dates upfront.
    Uses caching to avoid redundant I/O operations.
    """
    return pd.read_csv(DATA_PATH, parse_dates=["Date"])

# Cache the dataset at the module level to avoid redundant reads
_df = load_data()

def get_data():
    """
    Returns a copy of the dataset to ensure immutability.
    """
    return _df.copy()

def filter_data(region=None, account_type=None):
    """
    Filters the dataset based on the provided criteria.
    Uses `.query()` for better performance.
    """
    filtered_df = _df
    if region:
        filtered_df = filtered_df.query("Region == @region")
    if account_type:
        filtered_df = filtered_df.query("Account_Type == @account_type")
    return filtered_df.copy()

def get_monthly_transaction_data(filtered_df):
    """
    Groups filtered data by month and calculates total transaction amounts.
    Uses `.dt.to_period()` for efficient datetime processing.
    """
    filtered_df = filtered_df.copy()
    filtered_df["Month"] = filtered_df["Date"].dt.to_period("M").dt.to_timestamp()
    return (
        filtered_df.groupby("Month", observed=True)["Transaction_Amount"]
        .sum()
        .reset_index()
    )

def get_customer_segmentation(filtered_df):
    """
    Segments customers based on their balance into 'Low', 'Medium', and 'High'.
    Uses `.loc` to avoid SettingWithCopyWarning.
    """
    filtered_df = filtered_df.copy()
    categories = ["Low", "Medium", "High"]
    bins = [-1, 9999, 49999, float("inf")]

    filtered_df.loc[:, "Balance_Category"] = pd.cut(
        filtered_df["Balance"], bins=bins, labels=categories
    )

    return (
        filtered_df.groupby("Balance_Category", observed=True)
        .size()
        .reset_index(name="Customer_Count")
    )

def filter_data_by_criteria(regions=None, account_types=None):
    """
    Filters the dataset based on multiple regions and account types.
    Uses `.query()` for faster filtering.
    """
    filtered_df = _df
    if regions:
        filtered_df = filtered_df.query("Region in @regions")
    if account_types:
        filtered_df = filtered_df.query("Account_Type in @account_types")
    return filtered_df.copy()
