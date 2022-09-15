import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_ui as dui
import simulate_match as sm
import time
app = dash.Dash()

random_odds = [[0.40, 0.30, 0.30] for i in range(12)]
x = list(range(25))
y = sm.simulate_match(random_odds)

app.layout = html.Div(children=[
    html.H1(children='Win Probability'),

    dcc.RangeSlider(
        id='my-range-slider',
        min=0,
        max=100,
        step=0.01,
        value=[30, 70]
    ),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),



    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'bar', 'name': 'WCC Odds'},
            ],
            'layout': {
                'title': 'Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
