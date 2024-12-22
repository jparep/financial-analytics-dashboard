from dash import html, dcc
import pandas as pd

def create_layout(data):
    """Creates the layout for the dashboard."""
    # Load unique values for dropdowns and checkboxes
    regions = data["Region"].unique()
    account_types = data["Account_Type"].unique()

    return html.Div([
        html.H1("Banking Data Dashboard", style={"text-align": "center"}),

        html.Div([
            html.Div([
                dcc.Checklist(
                    id="region_filter",
                    options=[{"label": region, "value": region} for region in regions],
                    value=[],
                    style={"font-size": "16px", "margin": "5px"}
                ),
                html.Label("Filter by Region", style={"font-size": "18px", "font-weight": "bold"})
            ], style={"border": "1px solid #ccc", "padding": "10px", "margin": "10px"}),

            html.Div([
                dcc.Checklist(
                    id="account_filter",
                    options=[{"label": acc, "value": acc} for acc in account_types],
                    value=[],
                    style={"font-size": "16px", "margin": "5px"}
                ),
                html.Label("Filter by Account Type", style={"font-size": "18px", "font-weight": "bold"})
            ], style={"border": "1px solid #ccc", "padding": "10px", "margin": "10px"})
        ], style={"display": "flex", "flex-wrap": "wrap", "justify-content": "space-around"}),

        html.Div([
            dcc.Graph(id="balance_distribution", style={"height": "45vh"}),
            dcc.Graph(id="loan_status_chart", style={"height": "45vh"}),
        ], style={"display": "flex", "justify-content": "space-between"}),

        html.Div([
            dcc.Graph(id="monthly_transaction_trend", style={"height": "45vh"}),
            dcc.Graph(id="customer_segmentation", style={"height": "45vh"})
        ], style={"display": "flex", "justify-content": "space-between"})
    ])
