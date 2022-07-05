#Libraries
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard

#from app import app

#Add home to page registry
register_page(__name__, path="/", name="Inicio", title="Dashboard para el monitoreo de IAAS en el HUV - Inicio", order=1)

#Define content
content_home=  dbc.Container([

    dbc.Row(html.H3("Infecciones por Atención en Salud Hospital Universitario Evaristo García E.S.E.", 
        style={'textAlign': 'center', "font-weight":"bold"})),
    dbc.Row(
        html.P("""En el sector de la salud, los pacientes pueden desarrollar infecciones mientras reciben atención por otras condiciones. 
        Estas infecciones, que incluso pueden provocar la muerte, se conocen comúnmente como infecciones asociadas a la atención de salud
        (IAAS) y pueden ocurrir en cualquier lugar de atención médica, incluidos hospitales y otros centros médicos. 
        Las IAAS más comunes son infecciones en sitios de procedimientos quirúrgicos, infecciones asociadas con el uso de ventiladores 
        mecánicos o catéteres urinarios e infecciones en los puntos de acceso venoso.""")
    ),
    dbc.Row(html.Img(src="assets/images/HospitalLogoWhite.png")),

])

#Side menu cards
demographics_card = sidecard("Demografía", "Perfil de los Pacientes", "/demographics")
infections_card = sidecard("Infecciones", "Perfil de los Microorganismos", "/infections")
alerts_card = sidecard("Alertas", "Histórico de Alertas por IAAS", "/alerts")
earlyalerts_card = sidecard("Modelo", "Modelo de Alertas Tempranas", "/modelalerts")

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
        dbc.Col(content_home),
        ],
        align="start",
        justify="between"
        ),          
    ]
)

