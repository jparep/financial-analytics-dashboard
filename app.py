from dash import Dash
from layout import create_layout
from callbacks import register_callbacks
from data_loader import load_data

# Initialize the Dash app
app = Dash(__name__)
app.title = "Banking Data Dashboard"

# Expose the Flask server object
server = app.server

# Load data once
data = load_data()

# Set up the layout with the loaded data
app.layout = create_layout(data)

# Register callbacks with the loaded data
register_callbacks(app, data)

if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8050)
