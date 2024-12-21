from dash import Dash, html, dcc
from callbacks import register_callbacks

app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Banking Data Dashboard", style={'text-align': 'center'}),
    # Add layout components here
])

# Register callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False)
