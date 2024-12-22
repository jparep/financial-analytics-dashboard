from dash.dependencies import Input, Output
from data_loader import filter_data, get_monthly_transaction_data, get_customer_segmentation
from visualizations import create_balance_histogram, create_loan_status_pie, create_monthly_transaction_chart, create_customer_segmentation_chart

def register_callbacks(app):
    @app.callback(
        [
            Output("balance_distribution", "figure"),
            Output("loan_status_chart", "figure"),
            Output("monthly_transactions_chart", "figure"),
            Output("customer_segmentation_chart", "figure")
        ],
        [Input("region_selector", "value"), Input("account_selector", "value")]
    )
    def update_graphs(selected_region, selected_account):
        # Filter data based on user inputs
        filtered_data = filter_data(region=selected_region, account_type=selected_account)

        # Generate visualizations
        balance_fig = create_balance_histogram(filtered_data)
        loan_fig = create_loan_status_pie(filtered_data)
        monthly_transactions_fig = create_monthly_transaction_chart(
            get_monthly_transaction_data(filtered_data)
        )
        customer_segmentation_fig = create_customer_segmentation_chart(
            get_customer_segmentation(filtered_data)
        )

        return balance_fig, loan_fig, monthly_transactions_fig, customer_segmentation_fig
