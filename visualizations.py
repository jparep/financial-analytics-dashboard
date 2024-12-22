import plotly.express as px

def create_balance_histogram(data):
    """
    Creates a histogram for balance distribution.
    """
    return px.histogram(data, x="Balance", nbins=20, title="Balance Distribution")

def create_loan_status_pie(data):
    """
    Creates a pie chart for loan status distribution.
    """
    return px.pie(data, names="Loan_Status", title="Loan Status Distribution")

def create_monthly_transaction_trend_line(data):
    """
    Creates a line chart for monthly transaction trends.
    """
    return px.line(
        data,
        x="Date",
        y="Transaction_Amount",
        title="Monthly Transactions Trend",
        labels={"Date": "Month", "Transaction_Amount": "Total Transactions"}
    )

def create_customer_segmentation_bar(data):
    """
    Creates a bar chart for customer segmentation by region.
    """
    return px.bar(
        data,
        x="Region",
        y="Customer_Count",
        color="Customer_Segment",
        title="Customer Segmentation by Region",
        labels={"Customer_Count": "Number of Customers"}
    )
