from dash import Dash, html

# Create the Dash app
app = Dash(__name__)
server = app.server  # expose the Flask server for Render

# Define a simple layout
app.layout = html.Div([
    html.H1("Hello, Gay Har Win Myar!"),
    html.P("Mingalarbarbyar.")
])

if __name__ == "__main__":
    app.run_server(debug=True)
