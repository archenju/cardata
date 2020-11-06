import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('carData.csv')


app.layout = html.Div([
    dcc.Graph(
        id='Year-vs-Price',
        figure={
            'data': [
                go.Scatter(
                    x=df['Year'],
                    y=df['Selling_Price'],
                    text=df['Car_Name'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=""
                ) #for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Year'},
                yaxis={'title': 'Selling_Price'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()