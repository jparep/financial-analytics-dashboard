from dash import html, dcc
import pandas as pd

def create_layout():
    df = pd.read_csv("./data/banking_data.csv")

    return html.Div([
        html.H1("Banking Data Dashboard", style={"text-align": "center"}),

        # Dropdown filters
        html.Div([
            dcc.Dropdown(
                id="region_selector",
                options=[{"label": region, "value": region} for region in df["Region"].unique()],
                value=df["Region"].unique()[0],
                multi=False,
                style={"width": "45%", "display": "inline-block", "margin-right": "10px"}
            ),
            dcc.Dropdown(
                id="account_selector",
                options=[{"label": acc, "value": acc} for acc in df["Account_Type"].unique()],
                value=df["Account_Type"].unique()[0],
                multi=False,
                style={"width": "45%", "display": "inline-block"}
            )
        ], style={"text-align": "center", "margin-bottom": "20px"}),

        # Chart container with Flexbox
        html.Div([
            html.Div([
                dcc.Graph(id="balance_distribution")
            ], style={"flex": "1", "padding": "10px"}),

            html.Div([
                dcc.Graph(id="loan_status_chart")
            ], style={"flex": "1", "padding": "10px"})
        ], style={"display": "flex", "flex-direction": "row"}),  # Top row of charts

        html.Div([
            html.Div([
                dcc.Graph(id="monthly_transactions_chart")
            ], style={"flex": "1", "padding": "10px"}),

            html.Div([
                dcc.Graph(id="customer_segmentation_chart")
            ], style={"flex": "1", "padding": "10px"})
        ], style={"display": "flex", "flex-direction": "row"})  # Bottom row of charts
    ], style={"padding": "20px"})
