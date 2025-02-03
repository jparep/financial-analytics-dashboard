from dash import html, dcc
from data_loader import get_data

# Shared styles
FILTER_STYLE = {
    "border": "1px solid #ccc",
    "border-radius": "5px",
    "padding": "10px",
    "margin-bottom": "20px",
    "display": "inline-block",
    "vertical-align": "top",
    "margin-right": "10px"
}
CHART_STYLE = {"flex": "1", "padding": "10px"}
CONTAINER_STYLE = {"display": "flex", "flex-wrap": "wrap"}  # Responsive layout for charts


def generate_options(values):
    """
    Generates Dash checklist options from a unique list of values.
    """
    return [{"label": val, "value": val} for val in sorted(values)]


def create_layout():
    """
    Creates the layout for the Dash banking dashboard.
    """
    df = get_data()  # Load data once

    # Extract unique values
    regions = df["Region"].dropna().unique()
    account_types = df["Account_Type"].dropna().unique()

    return html.Div([
        html.H1("Banking Data Dashboard", style={"text-align": "center"}),

        # Filters Section
        html.Div([
            html.Div([
                html.Label("Select Regions", className="filter-label"),
                dcc.Checklist(
                    id="region_selector",
                    options=generate_options(regions),
                    value=list(regions),  # Default: Select all
                    labelStyle={"display": "inline-block", "margin-right": "10px"}
                )
            ], style=FILTER_STYLE),

            html.Div([
                html.Label("Select Account Types", className="filter-label"),
                dcc.Checklist(
                    id="account_selector",
                    options=generate_options(account_types),
                    value=list(account_types),  # Default: Select all
                    labelStyle={"display": "inline-block", "margin-right": "10px"}
                )
            ], style=FILTER_STYLE)
        ], style={"text-align": "center"}),

        # Charts Layout
        html.Div([
            html.Div([dcc.Graph(id="balance_distribution")], style=CHART_STYLE),
            html.Div([dcc.Graph(id="loan_status_chart")], style=CHART_STYLE),
        ], style=CONTAINER_STYLE),

        html.Div([
            html.Div([dcc.Graph(id="monthly_transactions_chart")], style=CHART_STYLE),
            html.Div([dcc.Graph(id="customer_segmentation_chart")], style=CHART_STYLE),
        ], style=CONTAINER_STYLE)

    ], style={"padding": "20px"})
