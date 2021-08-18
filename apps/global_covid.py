import plotly.express as px
import pandas as pd
 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
from app import app #change this line
 
# Data Preprocessing
df = pd.read_csv('time_series_covid_19_confirmed.csv')
df.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)
df.set_index('Country/Region', inplace=True)
dfT = df.T
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("COVID-19 Worldwide at a glance"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualising trends across the different stages of the COVID-19 outbreak Worldwide'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_country',
                    options=[
                       {'label': country, 'value': country} for country in dfT.columns.unique()
                    ],
                    value='Indonesia',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main-graph'
                )
            )
        ])
    ])
])
 
@app.callback(
    Output('main-graph', 'figure'),
    Input('selected_country', 'value')
)
def update_covid_chart(country):
    fig = px.line(dfT, x=dfT.index, y=country, title=f'{country} Covid Confirmed Case')
    return fig
 
# remove the main things