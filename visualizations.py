import plotly.express as px

def create_balance_histogram(data):
    return px.histogram(data, x="Balance", nbins=20, title="Balance Distribution")

def create_loan_status_pie(data):
    return px.pie(data, names="Loan_Status", title="Loan Status Distribution")

def create_monthly_transaction_chart(data):
    return px.line(data, x="Month", y="Transaction_Amount", title="Monthly Transactions")

def create_customer_segmentation_chart(data):
    return px.bar(
        data, x="Balance_Category", y="Customer_Count", title="Customer Segmentation by Balance"
    )
