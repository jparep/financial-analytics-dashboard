from dash.dependencies import Input, Output
from data_loader import filter_data_by_criteria
from visualizations import create_balance_histogram, create_loan_status_pie, create_monthly_transaction_trend, create_customer_segmentation

def register_callbacks(app):
    @app.callback(
        [Output("balance_distribution", "figure"),
         Output("loan_status_chart", "figure"),
         Output("monthly_transactions_chart", "figure"),
         Output("customer_segmentation_chart", "figure")],
        [Input("region_selector", "value"),
         Input("account_selector", "value")]
    )
    def update_graphs(selected_regions, selected_accounts):
        # Filter data based on user inputs
        filtered_data = filter_data_by_criteria(selected_regions, selected_accounts)

        # Create visualizations
        balance_fig = create_balance_histogram(filtered_data)
        loan_fig = create_loan_status_pie(filtered_data)
        monthly_fig = create_monthly_transaction_trend(filtered_data)
        segmentation_fig = create_customer_segmentation(filtered_data)

        return balance_fig, loan_fig, monthly_fig, segmentation_fig
