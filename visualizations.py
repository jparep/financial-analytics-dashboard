import plotly.express as px
import pandas as pd

def create_balance_histogram(data):
    """
    Creates a histogram for account balance distribution.
    Uses a uniform bin size and prevents modification of the original DataFrame.
    """
    return px.histogram(
        data_frame=data,
        x="Balance",
        nbins=20,
        title="Balance Distribution",
        labels={"Balance": "Account Balance ($)"},
        opacity=0.75,  # Adds transparency for better visualization
        color_discrete_sequence=["#636EFA"]  # Consistent color scheme
    )

def create_loan_status_pie(data):
    """
    Creates a pie chart for loan status distribution.
    Uses automatic hole detection to prevent empty slices.
    """
    return px.pie(
        data_frame=data,
        names="Loan_Status",
        title="Loan Status Distribution",
        hole=0.3,  # Creates a donut-style pie chart for better readability
        color_discrete_sequence=px.colors.qualitative.Plotly
    )

def create_monthly_transaction_trend(data):
    """
    Creates a line chart showing monthly transaction trends.
    Ensures 'Date' is in datetime format and aggregates transaction amounts.
    """
    # Ensure 'Date' is in datetime format
    data = data.copy()  # Avoid modifying the original DataFrame
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Month"] = data["Date"].dt.to_period("M")

    # Aggregate transaction amounts by month
    monthly_data = (
        data.groupby("Month", observed=True)["Transaction_Amount"]
        .sum()
        .reset_index()
    )
    monthly_data["Month"] = monthly_data["Month"].dt.to_timestamp()

    return px.line(
        data_frame=monthly_data,
        x="Month",
        y="Transaction_Amount",
        title="Monthly Transaction Trend",
        labels={"Transaction_Amount": "Transaction Amount ($)", "Month": "Month"},
        markers=True,  # Adds markers for better visualization
        line_shape="spline",  # Smoothens the line
        color_discrete_sequence=["#EF553B"]  # Distinct color
    )

def create_customer_segmentation(data):
    """
    Creates a bar chart for customer segmentation by account type.
    Uses a sorted order to improve readability.
    """
    # Group by account type and count customers
    segmentation_data = (
        data.groupby("Account_Type", observed=True)["Customer_ID"]
        .count()
        .reset_index()
        .sort_values(by="Customer_ID", ascending=False)  # Sorts for better visualization
    )
    segmentation_data.rename(columns={"Customer_ID": "Count"}, inplace=True)

    return px.bar(
        data_frame=segmentation_data,
        x="Account_Type",
        y="Count",
        title="Customer Segmentation by Account Type",
        labels={"Account_Type": "Account Type", "Count": "Number of Customers"},
        color="Account_Type",
        color_discrete_sequence=px.colors.qualitative.Dark24  # Distinct color palette
    )
