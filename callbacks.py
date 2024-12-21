from dash.dependencies import Input, Output
from data_loader import load_filtered_data
from visualizations import create_balance_histogram, create_loan_status_pie

def register_callbacks(app):
    @app.callback(
        [Output("balance_distribution", "figure"),
         Output("loan_status_chart", "figure")],
        [Input("region_selector", "value"),
         Input("account_selector", "value")]
    )
    def update_graphs(selected_region, selected_account):
        # Filter data based on user inputs
        filtered_data = load_filtered_data(selected_region, selected_account)

        # Create visualizations
        balance_fig = create_balance_histogram(filtered_data)
        loan_fig = create_loan_status_pie(filtered_data)

        return balance_fig, loan_fig
