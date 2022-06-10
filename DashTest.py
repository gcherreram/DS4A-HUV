#Import Libraries
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

#Images
HUV_logo = "https://huv.gov.co/wp-content/uploads/2020/06/logo-HU_Horizontal_Blanco.png"

#Figures
from Graphics import Microorganisms_fig, Families_fig, Antibiotics_fig

#Create App

app = Dash(__name__,external_stylesheets=[dbc.themes.COSMO], 
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

#Create Side Bar Cards
demographics_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H6("Demographics", style={"font-weight":"bold"}, className="card-title"),
                html.P(
                    "Profile of patients affected by HAIs in the hospital.",
                    className="card-text",
                ),
                dbc.Button("Learn More", color="primary", href="/page-1", active="exact", size="sm"),
            ]
        ),
    ],
    style={"color":"#838383"}
)

infections_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H6("Infections", style={"font-weight":"bold"}, className="card-title"),
                html.P(
                    "Profile of microorganisms which are causing HAIs in the hospital.",
                    className="card-text",
                ),
                dbc.Button("Learn More", color="primary", href="/page-2", active="exact", size="sm"),
            ]
        ),
    ],
    style={"color":"#838383"} 
)

hospital_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H6("Hospital", style={"font-weight":"bold"}, className="card-title"),
                html.P(
                    "Geographical distribution of HAIs in the hospital",
                    className="card-text",
                ),
                dbc.Button("Learn More", color="primary", href="/page-3", active="exact", size="sm"),
            ]
        ),
    ],
    style={"color":"#838383"},
)

info_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.P(
                    "@DS4A Colombia\n Cohort 6\n Team 237",
                    className="card-text",
                ),
            ]
        ),
        dbc.CardImg(src="/assets/DS4Alogo.png", bottom=True),
    ],
    style={"color":"#838383"},
)


# Create Navigation bar
navbar = dbc.NavbarSimple(
    children = [
        dbc.Row(
            [
                dbc.Col(dbc.DropdownMenu
                    (
                        children=[
                        dbc.DropdownMenuItem("Home", href="/", active="exact"),    
                        dbc.DropdownMenuItem("Demographics", href="/page-1", active="exact"),
                        dbc.DropdownMenuItem("Infections", href="/page-2", active="exact"),
                        dbc.DropdownMenuItem("Hospital View", href="/page-3", active="exact"),
                        ],
                        nav=True,
                        in_navbar=True,
                        label="Menu",          
                    )
                ),
                dbc.Col(dbc.NavItem(html.Img(src=HUV_logo, height="50px"))),
            ]
        )
    ],
    brand="Dashboard for Monitoring Evolution of HAIs",
    brand_href="#",
    color="primary",
    dark=True,
)
 
    
#Create Content
content_home = [
    html.H3("Home", style={'textAlign': 'center'}),
    html.H4("This is the Home Page")
]

content_page1 = [
    html.H3("Demographics", style={'textAlign': 'center'}),
    html.H4("This is the content of page 1. Yay!")
]

content_page2 = [
    dbc.Row(
        html.Div(
            [
                html.H2("Infections", style={'textAlign': 'center'}, id="subtitle"), 
                dcc.Dropdown(['Microorganisms', 'Microorganisms Family', 'Antibiotics'], 
                                    "Microorganisms", id='fig-dropdown'),
                dcc.Graph(figure=Microorganisms_fig,id='microorganisms-figure'),
                          
            ],
            style={'textAlign': 'center'}
        )
    )
]
    
content_page3 = [
    html.H3("Hospital View", style={'textAlign': 'center'}),
    html.Img(src="/assets/HospitalMap.jpeg")
]

#Create app layout

content = html.Div(id="page-content")

app.layout = html.Div(
        [
            dcc.Location(id="url"),
            dbc.Row(navbar),
            dbc.Row(
                [
                    dbc.Col(
                            [
                            dbc.Row(demographics_card),
                            dbc.Row(infections_card),
                            dbc.Row(hospital_card),
                            dbc.Row(info_card),
                            ]
                        ),
                    dbc.Col(content, width=10),
                 ],
                 align="start",
                 justify="between"
            )            
    ]
)

#Callbacks

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(content_home)
    elif pathname == "/page-1":
        return html.P(content_page1)
    elif pathname == "/page-2":
        return html.P(content_page2)
    elif pathname == "/page-3":
        return html.P(content_page3)
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(Output('microorganisms-figure', 'figure'), [Input('fig-dropdown', 'value')])
def dropdown_interaction(dropdown_val):
    if dropdown_val == "Microorganisms":
        fig = Microorganisms_fig
    elif dropdown_val=='Microorganisms Family':
        fig = Families_fig
    else:
        fig = Antibiotics_fig

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)