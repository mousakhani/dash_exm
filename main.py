import dash
from  dash import  html, Input, Output, dcc
import plotly.graph_objs as go
from random import randint

app = dash.Dash(__name__)

default_slider = 14 
fig={
       'data': [{
            'type': 'bar',
            "x":[int(i) for i in range(0, 20)],
            "y":[randint(0,int(default_slider)) for i in range(0, 20)], 
            'marker': {
               'color': ['blue'] * 20
            }
       }],
       'layout': {
           'title': 'click a bar'
       }
    }
app.layout = html.Div([
   dcc.Graph(id='graph', figure =fig),
   html.H1(id='bar_id'),
           dcc.Slider(
        id='slider',
        min=0,
        max=20,
        value=default_slider,
        marks={i: str(i) for i in range(20)},
    )
])

@app.callback([Output('graph', 'figure'),
              Output('bar_id', 'children')],
             [Input('graph', 'clickData'),
              Input('slider', 'value')]
             )
def update_image(clickData, v):
    color = ['blue'] * 20
    global fig 
    fig = {
       'data': [{
            'type': 'bar',
            "x":[int(i) for i in range(0, 20)] if dash.callback_context.triggered_id =='slider' else fig['data'][0]['x'] ,
            "y":[randint(0,int(v)) for i in range(0, 20)] if dash.callback_context.triggered_id =='slider' else fig['data'][0]['y'], 
            'marker': {
               'color': color
            }
       }],
       'layout': {
           'title': 'click a bar'
       }
    }
    selected_bar_id='None'
    if clickData is not None:
        selected_bar_id = clickData['points'][0]['pointNumber']
        fig['data'][0]['marker']['color'][selected_bar_id] = 'red'
    return fig, selected_bar_id

if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='127.0.0.1')