#Libraries
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard
from components.cards.infocard import infocard
from assets.graphs.graphs import demo_graph_generator

#Add alerts to page registry
register_page(__name__, path="/alerts", name= "Alertas", 
    title="Dashboard para el monitoreo de IAAS en el HUV - Alertas", order=4)

#Side menu cards
demographics_card = sidecard("Demografía", "Pacientes afectados por IAAS en el hospital.", "/demographics")
infections_card = sidecard("Infecciones", "Microorganismos que están causando IAAS en el hospital", "/infections")
alerts_card = sidecard("Alertas", "Alertas por IAAS", "/alerts")
info_card = infocard("@DS4A Colombia\n Cohort 6\n Team 237", "/assets/images/DS4Alogo.png")

#Generate page content
content_alerts = dbc.Container([])

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
                            ]
                        ),
                    dbc.Col(content_alerts, width=10),
                 ],
                 align="start",
                 justify="between"
            ),
            dbc.Row(info_card)            
    ]
)
