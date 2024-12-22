from dash import html, dcc
from data_loader import get_data

# Shared styles
filter_style = {
    "border": "1px solid #ccc",
    "border-radius": "5px",
    "padding": "10px",
    "margin-bottom": "20px",
    "display": "inline-block",  # Ensures the filters are displayed inline
    "vertical-align": "top",    # Aligns the filters to the top
    "margin-right": "10px"      # Adds space between the filters
}
chart_style = {"flex": "1", "padding": "10px"}

def create_layout():
    # Load data for dropdown and checkbox options
    df = get_data()

    return html.Div([
        # Dashboard Title
        html.H1("Banking Data Dashboard", style={"text-align": "center"}),

        # Filters Section
        html.Div([
            html.Div([
                html.Label(
                    "Select Regions", 
                    style={"font-weight": "bold", "margin-bottom": "5px", "display": "block"}
                ),
                dcc.Checklist(
                    id="region_selector",
                    options=[{"label": region, "value": region} for region in df["Region"].unique()],
                    value=list(df["Region"].unique()),  # Default: Select all
                    labelStyle={"display": "inline-block", "margin-right": "10px"}  # Aligns checkboxes horizontally
                )
            ], style=filter_style),

            html.Div([
                html.Label(
                    "Select Account Types", 
                    style={"font-weight": "bold", "margin-bottom": "5px", "display": "block"}
                ),
                dcc.Checklist(
                    id="account_selector",
                    options=[{"label": acc, "value": acc} for acc in df["Account_Type"].unique()],
                    value=list(df["Account_Type"].unique()),  # Default: Select all
                    labelStyle={"display": "inline-block", "margin-right": "10px"}  # Aligns checkboxes horizontally
                )
            ], style=filter_style)
        ], style={"text-align": "center"}),  # Centers the filter section

        # Charts Layout
        html.Div([
            html.Div([dcc.Graph(id="balance_distribution")], style=chart_style),
            html.Div([dcc.Graph(id="loan_status_chart")], style=chart_style),
        ], style={"display": "flex", "flex-wrap": "wrap"}),  # Top row of charts

        html.Div([
            html.Div([dcc.Graph(id="monthly_transactions_chart")], style=chart_style),
            html.Div([dcc.Graph(id="customer_segmentation_chart")], style=chart_style),
        ], style={"display": "flex", "flex-wrap": "wrap"})  # Bottom row of charts
    ], style={"padding": "20px"})
