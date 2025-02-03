from dash.dependencies import Input, Output
from data_loader import filter_data_by_criteria
from visualizations import (
    create_balance_histogram,
    create_loan_status_pie,
    create_monthly_transaction_trend,
    create_customer_segmentation
)

def register_callbacks(app):
    """
    Registers callbacks to update the visualizations dynamically based on user input.
    """
    @app.callback(
        output=[
            Output("balance_distribution", "figure"),
            Output("loan_status_chart", "figure"),
            Output("monthly_transactions_chart", "figure"),
            Output("customer_segmentation_chart", "figure")
        ],
        inputs=[
            Input("region_selector", "value"),
            Input("account_selector", "value")
        ],
        prevent_initial_call=False  # Ensures initial rendering
    )
    def update_graphs(selected_regions, selected_accounts):
        """
        Updates all dashboard visualizations when filter selections change.
        """
        # Ensure selections are lists to prevent errors
        selected_regions = selected_regions or []
        selected_accounts = selected_accounts or []

        # Filter dataset based on user-selected criteria
        filtered_data = filter_data_by_criteria(selected_regions, selected_accounts)

        # Generate updated figures
        return (
            create_balance_histogram(filtered_data),
            create_loan_status_pie(filtered_data),
            create_monthly_transaction_trend(filtered_data),
            create_customer_segmentation(filtered_data)
        )
