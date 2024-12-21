import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load synthetic dataset
data_url = "synthetic_banking_data.csv"
df = pd.read_csv(data_url)

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Banking Data Dashboard", style={'text-align': 'center'}),
    
    # Filters
    html.Div([
        dcc.Dropdown(
            id="region_selector",
            options=[{"label": region, "value": region} for region in df['Region'].unique()],
            value=df['Region'].unique()[0],
            multi=False,
            style={'width': "50%"}
        ),
        dcc.Dropdown(
            id="account_selector",
            options=[{"label": acc, "value": acc} for acc in df['Account_Type'].unique()],
            value=df['Account_Type'].unique()[0],
            multi=False,
            style={'width': "50%"}
        )
    ]),
    
    # Visualizations
    dcc.Graph(id='balance_distribution'),
    dcc.Graph(id='loan_status_chart')
])

# Callbacks
@app.callback(
    [Output('balance_distribution', 'figure'),
     Output('loan_status_chart', 'figure')],
    [Input('region_selector', 'value'),
     Input('account_selector', 'value')]
)
def update_graphs(selected_region, selected_account):
    filtered_df = df[(df['Region'] == selected_region) & (df['Account_Type'] == selected_account)]
    
    balance_fig = px.histogram(filtered_df, x='Balance', nbins=20, title='Balance Distribution')
    loan_fig = px.pie(filtered_df, names='Loan_Status', title='Loan Status Distribution')
    
    return balance_fig, loan_fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
