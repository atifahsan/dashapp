# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas
import base64

df = pandas.read_csv('E:\\Aircom\\Stats\\3G Cell_May.csv', index_col=['Date'])


app = dash.Dash()
app.title = 'KPI Dashboard'
app.title = 'new'

image_filename = './logo.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


app.layout = html.Div([
    # Title - Row
    html.Div([
            html.H1('Etisalat Dashboard', style={'font-family': 'Helvetica',
                                                "margin-top": "10",
                                                "margin-bottom": "0"
                                                },className='eight columns'
            ),
            html.Img(
                src='data:image/png;base64,{}'.format(encoded_image.decode()),
                className='two columns',
                style={
                    'height': '8%',
                    'width': '8%',
                    'float': 'right',
                    'position': 'relative',
                    'padding-top': 0,
                    'padding-right': 50
                },
            ),
    ], className='row'),

    html.Div([
        html.P([
                html.B("Enter CellId:  "),
                dcc.Input(
                    id="input",
                    value="")
        ]),
    ], className='row'),

    html.Div(id='output-graph', className='six columns'),


    
], className='ten columns offset-by-one')




@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')])
def update_graph(input_data):
    data = df[df['CELLNAME'] == input_data]

    return dcc.Graph(id='example',
            figure={
                'data': [
                    {'x': data.index, 'y': data['RRC SSR (CELL) %'], 'type': 'line', 'name':'RRC SSR'},
                    ],
                'layout' : {
                    'title' : 'RRC SSR'
                }
            })

# Boostrap CSS.
app.css.append_css({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
})

# Extra Dash styling.
app.css.append_css({
    "external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# JQuery is required for Bootstrap.
app.scripts.append_script({
    "external_url": "https://code.jquery.com/jquery-3.2.1.min.js"
})

# Bootstrap Javascript.
app.scripts.append_script({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
})

if __name__ == '__main__':
    app.run_server(debug=True)
