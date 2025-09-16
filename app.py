from dash import Dash, html

# Create the Dash app
app = Dash(__name__)
server = app.server  # expose the Flask server for Render

# Define a simple layout
app.layout = html.Div([
    html.H1("Hello, Dash!"),
    html.P("This is a test app running on Render.")
])

if __name__ == "__main__":
    app.run_server(debug=True)
