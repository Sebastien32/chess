import dash
import dash_core_components as dcc
import dash_html_components as html
import itertools as it
app = dash.Dash()

weighted_die = [2, 2, 2, 2, 2, 2]
final_probs = [0 for i in range(16)]


for i in it.product(range(1, 7), repeat = 3):
    final_probs[sum(i) - 3] += 1 / 216

app.layout = html.Div(children=[

    html.H1(children='Die Testing'),

    dcc.Slider(
    id='my-slider',
    min = -3,
    max = 3,
    value = 0,
    step = 1,
    marks = {
        -3: '-3',
        -2: '-2',
        -1: '-1',
        0: '0',
        1: '-3',
        2: '-3',
        3: '-3'
    }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': list(range(1, 7)), 'y': weighted_die,
                'type': 'bar', 'name': 'Weighted die'},
            ],
            'layout': {
                'title': 'Weighted die'
            }
        }
    ),

     dcc.Graph(
         id='final-graph',
         figure={
             'data': [
                 {'x': list(range(3, 19)), 'y': final_probs,
                 'type': 'bar', 'name': 'Weighted die'},
             ],
             'layout': {
                 'title': 'Final distribution'
             }
         }
     ),

    html.Div(id='output-container', style={'margin-top': 20}),
])

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    if (value == -3):
        weighted_die = [3, 3, 3, 1, 1, 1]
    elif (value == -2):
        weighted_die = [3, 3, 2, 2, 1, 1]
    elif (value == -1):
        weighted_die = [3, 2, 2, 2, 2, 1]
    elif (value == 0):
        weighted_die = [2, 2, 2, 2, 2, 2]
    elif (value == 1):
        weighted_die = [1, 2, 2, 2, 2, 3]
    elif (value == 2):
        weighted_die = [1, 1, 2, 2, 3, 3]
    elif (value == 3):
        weighted_die = [1, 1, 1, 3, 3, 3]
    return {
        'data': [
            {'x': list(range(1, 7)), 'y': weighted_die,
            'type': 'bar', 'name': 'Weighted die'},
        ],
        'layout': {
            'title': 'Weighted die'
        }
    }

@app.callback(
    dash.dependencies.Output('final-graph', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    if (value == -3):
        weighted_die = [3, 3, 3, 1, 1, 1]
    elif (value == -2):
        weighted_die = [3, 3, 2, 2, 1, 1]
    elif (value == -1):
        weighted_die = [3, 2, 2, 2, 2, 1]
    elif (value == 0):
        weighted_die = [2, 2, 2, 2, 2, 2]
    elif (value == 1):
        weighted_die = [1, 2, 2, 2, 2, 3]
    elif (value == 2):
        weighted_die = [1, 1, 2, 2, 3, 3]
    elif (value == 3):
        weighted_die = [1, 1, 1, 3, 3, 3]
    final_probs = [0 for i in range(16)]
    for i in it.product(range(1, 7), repeat = 3):
        final_probs[sum(i) - 3] += (1 / 36) * weighted_die[i[2] - 1] / 12
    return {
        'data': [
            {'x': list(range(3, 19)), 'y': final_probs,
            'type': 'bar', 'name': 'Weighted die'},
        ],
        'layout': {
            'title': 'Final distribution'
        }
    }



if __name__ == '__main__':
    app.run_server(debug=True)
