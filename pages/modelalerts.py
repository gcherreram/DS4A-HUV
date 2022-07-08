#Libraries
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard
from assets.graphs.graphs import demo_graph_generator

#Add alerts to page registry
register_page(__name__, path="/modelalerts", name= "Modelo", 
    title="Dashboard para el monitoreo de IAAS en el HUV - Alertas Tempranas", order=5)

#Side menu cards
demographics_card = sidecard("Demografía", "Perfil de los Pacientes", "/demographics")
infections_card = sidecard("Infecciones", "Perfil de los Microorganismos", "/infections")
alerts_card = sidecard("Alertas", "Histórico de Alertas por IAAS", "/alerts")
earlyalerts_card = sidecard("Modelo", "Modelo de Alertas Tempranas", "/modelalerts")

#Generate page content
content_model = dbc.Container([
    dbc.Row(html.H4("Modelos Predictivos", style={'textAlign': 'center', "font-weight":"bold"})),
    dbc.Row([
        dbc.Carousel(
            items = [
                {
                    "key": "1",
                    "src": "/assets/images/Decision_tree_model1.png",
                    
                },
                {
                    "key": "2",
                    "src": "/assets/images/Decision_tree_model2.png",

                },                ],
                controls=False,
                indicators=False,
                interval=5000,
                ride="carousel",
                variant = "dark",
            ),
        ]),
])

#Define layout
layout = html.Div(
[
    dbc.Row(
    [
        dbc.Col(
        [
            dbc.Row(demographics_card),
            dbc.Row(infections_card),
            dbc.Row(alerts_card),
            dbc.Row(earlyalerts_card),
        ], width=2,
        ),
        dbc.Col(content_model),
    ],
    align="start",
    justify="between"
    ),            
]
)
