import pandas as pd

def load_data(file_path):
    """
    Loads transaction data from a specified CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The loaded transaction data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the file. Please check the file format.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


def get_monthly_transaction_trend(data):
    """
    Groups transaction data by month and calculates the total transaction amount for each month.

    Parameters:
    - data (pd.DataFrame): The filtered transaction data. Must contain 'Date' and 'Transaction_Amount' columns.

    Returns:
    - pd.DataFrame: Monthly transaction trends with total transaction amounts.
    """
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.dropna(subset=['Date'])
    data['Month'] = data['Date'].dt.to_period('M')

    if 'Transaction_Amount' not in data.columns:
        raise KeyError("The input data does not contain a 'Transaction_Amount' column.")
    if not pd.api.types.is_numeric_dtype(data['Transaction_Amount']):
        raise TypeError("'Transaction_Amount' column must contain numeric values.")

    monthly_trend = data.groupby('Month')['Transaction_Amount'].sum().reset_index()
    monthly_trend['Month'] = monthly_trend['Month'].dt.to_timestamp()
    return monthly_trend


def filter_data(data, start_date=None, end_date=None):
    """
    Filters the transaction data based on the specified date range.

    Parameters:
    - data (pd.DataFrame): The transaction data.
    - start_date (str): The start date in 'YYYY-MM-DD' format (optional).
    - end_date (str): The end date in 'YYYY-MM-DD' format (optional).

    Returns:
    - pd.DataFrame: The filtered transaction data.
    """
    if 'Date' not in data.columns:
        raise KeyError("The input data does not contain a 'Date' column.")
    
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.dropna(subset=['Date'])

    if start_date:
        data = data[data['Date'] >= pd.to_datetime(start_date)]
    if end_date:
        data = data[data['Date'] <= pd.to_datetime(end_date)]
    
    return data


def load_filtered_data(file_path, start_date=None, end_date=None):
    """
    Loads and filters transaction data based on a date range.

    Parameters:
    - file_path (str): The path to the CSV file.
    - start_date (str): The start date in 'YYYY-MM-DD' format (optional).
    - end_date (str): The end date in 'YYYY-MM-DD' format (optional).

    Returns:
    - pd.DataFrame: The filtered transaction data.
    """
    data = load_data(file_path)
    filtered_data = filter_data(data, start_date=start_date, end_date=end_date)
    return filtered_data
