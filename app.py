from dash import Dash
from layout import create_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = Dash(__name__)
app.title = "Interactivate Financial Dashboard"

# Expose the Flask server object
server = app.server

# Set up the layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8050)
