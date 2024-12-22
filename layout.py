from dash import html, dcc
import pandas as pd

def create_layout():
    df = pd.read_csv("./data/banking_data.csv")

    return html.Div([
        # Dashboard Title
        html.H1("Banking Data Dashboard", style={"text-align": "center"}),

        # Filters with Checkboxes
        html.Div([
            html.Div([
                html.Label("Select Regions", style={"font-weight": "bold", "margin-bottom": "5px"}),
                dcc.Checklist(
                    id="region_selector",
                    options=[{"label": region, "value": region} for region in df["Region"].unique()],
                    value=[df["Region"].unique()[0]],  # Default selection
                    inline=True
                )
            ], style={"border": "1px solid #ccc", "border-radius": "5px", "padding": "10px", "margin-bottom": "10px"}),

            html.Div([
                html.Label("Select Account Types", style={"font-weight": "bold", "margin-bottom": "5px"}),
                dcc.Checklist(
                    id="account_selector",
                    options=[{"label": acc, "value": acc} for acc in df["Account_Type"].unique()],
                    value=[df["Account_Type"].unique()[0]],  # Default selection
                    inline=True
                )
            ], style={"border": "1px solid #ccc", "border-radius": "5px", "padding": "10px", "margin-bottom": "20px"})
        ], style={"width": "60%", "margin": "0 auto"}),

        # Charts Layout
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
