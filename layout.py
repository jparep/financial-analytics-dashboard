import pandas as pd
import os

def load_filtered_data(region, account_type):
    try:
        # Ensure the correct path to the data file
        data_path = os.path.join(os.getcwd(), "data", "banking_data.csv")
        df = pd.read_csv(data_path)

        # Filter data based on the selected region and account type
        return df[(df["Region"] == region) & (df["Account_Type"] == account_type)]
    except FileNotFoundError:
        raise FileNotFoundError("The file banking_data.csv is not found.")
    except Exception as e:
        raise RuntimeError(f"Error loading data: {e}")
