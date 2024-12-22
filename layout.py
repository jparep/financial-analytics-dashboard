from dash import html, dcc
import pandas as pd

def create_layout():
    # Load a sample of the dataset to populate dropdown options
    df = pd.read_csv("./data/banking_data.csv")

    return html.Div([
        html.H1("Banking Data Dashboard", style={"text-align": "center"}),

        # Dropdown Filters
        html.Div([
            dcc.Dropdown(
                id="region_selector",
                options=[{"label": region, "value": region} for region in df["Region"].unique()],
                value=df["Region"].unique()[0],
                multi=False,
                style={"width": "50%"}
            ),
            dcc.Dropdown(
                id="account_selector",
                options=[{"label": acc, "value": acc} for acc in df["Account_Type"].unique()],
                value=df["Account_Type"].unique()[0],
                multi=False,
                style={"width": "50%"}
            )
        ], style={"display": "flex", "justify-content": "space-between"}),

        # Row 1: Balance Distribution and Loan Status Charts
        html.Div([
            dcc.Graph(id="balance_distribution", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="loan_status_chart", style={"width": "48%", "display": "inline-block"})
        ], style={"display": "flex", "justify-content": "space-between"}),

        # Row 2: Monthly Transactions Trend and Customer Segmentation by Region
        html.Div([
            dcc.Graph(id="monthly_transactions_trend", style={"width": "48%", "display": "inline-block"}),
            dcc.Graph(id="customer_segmentation", style={"width": "48%", "display": "inline-block"})
        ], style={"display": "flex", "justify-content": "space-between"})
    ])
