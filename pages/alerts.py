#Libraries
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard
from assets.graphs.graphs import alert_in_map

#Add alerts to page registry
register_page(__name__, path="/alerts", name= "Alertas", 
    title="Dashboard para el monitoreo de IAAS en el HUV - Alertas", order=4)

#Side menu cards
demographics_card = sidecard("Demografía", "Perfil de los Pacientes", "/demographics")
infections_card = sidecard("Infecciones", "Perfil de los Microorganismos", "/infections")
alerts_card = sidecard("Alertas", "Histórico de Alertas por IAAS", "/alerts")
earlyalerts_card = sidecard("Alertas Tempranas", "Modelo de Alertas Tempranas", "/modelalerts")

#Generate page content

content_alerts = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("Alertas por piso"),
        dbc.Row(dcc.Dropdown(["Primer Piso", "Segundo Piso", "Tercer Piso", "Cuarto Piso", "Quinto Piso", "Sexto Piso"], 
            value='Perimer Piso', id="map_dropdown")),
        dbc.Row(dcc.Graph(figure=alert_in_map("Primer Piso"), id='alert_map_figure2')
            ,justify="center"),
        ])
    ])
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
        dbc.Col(content_alerts),
    ],
    align="start",
    justify="between"
    ),            
]
)

#Callbacks
@callback(
    [Output('alert_map_figure2', 'figure')], 
    [Input('map_dropdown', 'value')],
    prevent_initial_call=True)

def map_dropdown_interaction(dropdown_val):

    if dropdown_val == "Primer Piso":
        selected_floor = "first"
    elif dropdown_val == "Segundo Piso":
        selected_floor = "second"
    elif dropdown_val == "Tercer Piso":
        selected_floor = "third"
    elif dropdown_val == "Cuarto Piso":
        selected_floor = "fourth"
    elif dropdown_val == "Quinto Piso":
        selected_floor = "fifth"
    else:
        selected_floor = "sixth"

    figure=alert_in_map(selected_floor)
    return [figure]
