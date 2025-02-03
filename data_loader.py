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
    Groups filtered data by month
