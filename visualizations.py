import plotly.express as px

def create_balance_histogram(data):
    return px.histogram(data, x='Balance', nbins=20, title='Balance Distribution')

def create_loan_status_pie(data):
    return px.pie(data, names='Loan_Status', title='Loan Status Distribution')
