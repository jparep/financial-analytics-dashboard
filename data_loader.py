import pandas as pd

def load_filtered_data(region, account_type):
    """
    Load and filter data based on the selected region and account type.
    """
    # Load the dataset
    df = pd.read_csv("./data/banking_data.csv")
    # Filter data based on the selected region and account type
    return df[(df["Region"] == region) & (df["Account_Type"] == account_type)]

def get_monthly_transaction_trend(filtered_df):
    """
    Process data to compute monthly transaction trends.
    """
    # Ensure the 'Date' column is in datetime format
    filtered_df["Date"] = pd.to_datetime(filtered_df["Date"])
    # Group by month and calculate the total transaction amount
    monthly_trend = (
        filtered_df.groupby(filtered_df["Date"].dt.to_period("M"))
        .sum()
        .reset_index()
    )
    monthly_trend["Date"] = monthly_trend["Date"].dt.to_timestamp()
    return monthly_trend

def get_customer_segmentation(filtered_df):
    """
    Process data to compute customer segmentation by region.
    """
    # Group by region and customer segment to get counts
    segmentation = (
        filtered_df.groupby(["Region", "Customer_Segment"])
        .size()
        .reset_index(name="Customer_Count")
    )
    return segmentation
