import dash
from dash import dcc, html

# Initialize the app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Economic Indicators Dashboard"),
    dcc.Graph(id="example-chart")
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

