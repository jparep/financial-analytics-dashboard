from dash.dependencies import Input, Output
from data_loader import load_filtered_data, get_monthly_transaction_trend, get_customer_segmentation
from visualizations import (
    create_balance_histogram,
    create_loan_status_pie,
    create_monthly_transaction_trend_line,
    create_customer_segmentation_bar
)

def register_callbacks(app):
    @app.callback(
        [Output("balance_distribution", "figure"),
         Output("loan_status_chart", "figure"),
         Output("monthly_transactions_trend", "figure"),
         Output("customer_segmentation", "figure")],
        [Input("region_selector", "value"),
         Input("account_selector", "value")]
    )
    def update_graphs(selected_region, selected_account):
        # 1. Filter data
        filtered_data = load_filtered_data(selected_region, selected_account)
        if filtered_data.empty:
            print("Filtered data is empty! Returning empty graphs.")
            return {}, {}, {}, {}

        # 2. Process data for additional visualizations
        monthly_trend_data = get_monthly_transaction_trend(filtered_data)
        customer_segmentation_data = get_customer_segmentation(filtered_data)

        # 3. Generate visualizations
        balance_fig = create_balance_histogram(filtered_data)
        loan_fig = create_loan_status_pie(filtered_data)
        monthly_trend_fig = create_monthly_transaction_trend_line(monthly_trend_data)
        customer_segmentation_fig = create_customer_segmentation_bar(customer_segmentation_data)

        # 4. Return figures
        return balance_fig, loan_fig, monthly_trend_fig, customer_segmentation_fig
