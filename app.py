
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
from dash.dependencies import Input, Output


# Sample data
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] * 2,
    'Category': ['Food']*6 + ['Transport']*6,
    'Spending': [250, 200, 300, 220, 270, 240, 100, 120, 90, 130, 110, 150]
})


app = Dash(__name__)

server = app.server


app.layout = html.Div([
    html.H1("Monthly Spending Dashboard"),
    dcc.Dropdown(
        id='category-filter',
        options=[{'label': cat, 'value': cat} for cat in df['Category'].unique()],
        value='Food'
    ),
    dcc.Graph(id='line-chart'),
    dcc.Graph(id='bar-chart')
])

@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure')],
    [Input('category-filter', 'value')]
)

def update_charts(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    line_fig = px.line(filtered_df, x='Month', y='Spending', title='Spending Over Time')
    bar_fig = px.bar(filtered_df, x='Month', y='Spending', title='Monthly Spending Breakdown')
    return line_fig, bar_fig



if __name__ == "__main__":
    app.run_server(debug=True)
