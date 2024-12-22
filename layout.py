from dash import html, dcc
import pandas as pd
import os

def create_layout():
    try:
        # Load a sample of the dataset to populate dropdown options
        data_path = os.path.join(os.getcwd(), "data", "banking_data.csv")
        df = pd.read_csv(data_path)

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
    except FileNotFoundError:
        raise FileNotFoundError("The file banking_data.csv is not found.")
    except Exception as e:
        raise RuntimeError(f"Error in layout creation: {e}")
