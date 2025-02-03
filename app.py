from dash import Dash
from layout import create_layout
from callbacks import register_callbacks

def create_app():
    """
    Initializes and configures the Dash application.
    Returns:
        Dash: Configured Dash application instance.
    """
    app = Dash(
        __name__,
        suppress_callback_exceptions=True,  # Prevents errors on callbacks referencing hidden elements
        update_title="Loading...",  # Shows a loading message in the tab when the app is updating
    )
    app.title = "Interactive Dashboard"

    # Expose the Flask server object for deployment
    server = app.server

    # Set up the layout
    app.layout = create_layout()

    # Register callbacks
    register_callbacks(app)

    return app, server

# Run the app only if executed directly
if __name__ == "__main__":
    app, _ = create_app()
    app.run_server(debug=False, host="0.0.0.0", port=8050)
