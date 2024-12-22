from dash import html, dcc
import pandas as pd

def create_layout():
    # Load a sample of the dataset to populate dropdown options
    df = pd.read_csv("synthetic_banking_data.csv")

    return html.Div([
        html.H1("Banking Data Dashboard", style={"text-align": "center"}),

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
        ]),

        dcc.Graph(id="balance_distribution"),
        dcc.Graph(id="loan_status_chart")
    ])
