import plotly.express as px
import pandas as pd

def create_balance_histogram(data):
    """Creates a histogram for account balance distribution."""
    return px.histogram(data, x="Balance", nbins=20, title="Balance Distribution")

def create_loan_status_pie(data):
    """Creates a pie chart for loan status distribution."""
    return px.pie(data, names="Loan_Status", title="Loan Status Distribution")

def create_monthly_transaction_trend(data):
    """Creates a line chart showing monthly transaction trends."""
    # Convert 'Date' column to datetime if not already
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data['Date'].dt.to_period('M')

    # Aggregate transaction amounts by month
    monthly_data = data.groupby('Month')['Transaction_Amount'].sum().reset_index()
    monthly_data['Month'] = monthly_data['Month'].dt.to_timestamp()

    return px.line(
        monthly_data,
        x="Month",
        y="Transaction_Amount",
        title="Monthly Transaction Trend",
        labels={"Transaction_Amount": "Transaction Amount ($)", "Month": "Month"}
    )

def create_customer_segmentation(data):
    """Creates a bar chart for customer segmentation."""
    segmentation_data = data.groupby('Account_Type')['Customer_ID'].count().reset_index()
    segmentation_data.rename(columns={'Customer_ID': 'Count'}, inplace=True)

    return px.bar(
        segmentation_data,
        x="Account_Type",
        y="Count",
        title="Customer Segmentation by Account Type",
        labels={"Account_Type": "Account Type", "Count": "Number of Customers"}
    )
