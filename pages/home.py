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

    dbc.Row(html.H3("Infecciones por Atención en el Salud Hospital Universitario Evaristo García E.S.E.", 
        style={'textAlign': 'center', "font-weight":"bold"})),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(),
                dbc.CardHeader("Sobre las IAAs", style={'textAlign': 'center', "font-weight":"bold"}),
                dbc.CardBody(
                    html.P("""Una infección asociada a la atención de la salud (IAAs) es aquella que ocurre en un paciente en un escenario de atención 
                    de salud y que no estaba presente en el momento de la admisión."""),
                ),
            ]),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardImg(),
                dbc.CardHeader("Sobre este dashboard", style={'textAlign': 'center', "font-weight":"bold"}),
                dbc.CardBody(
                        html.P("""Este dashboard presenta una caracterización de la IAAs en el HUV del valle entre 2013 (septiembre) y 2021.
                        Fue desarrollado por el Equipo 237 con la intencón de ofrecer una herramienta para la toma de decisiones en el HUV"""),
                ),
            ]),
        ]),   
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src="assets/images/HospitalLogoWhite.png"),
                dbc.CardBody(
                    html.P("Las bases de datos empleadas para este análisis son propiedad del HUV", style={'textAlign': 'center'}),
                ),
            ]),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src="assets/images/DS4AColombiaLogo.png", class_name="w-50"),
                dbc.CardBody(
                    html.P("""Esta aplicación es es resultado de nuestros aprendizajes en el curso DS4A Colombia 
                    ofrecido por Correlation One, en asocio con MinTIC""", style={'textAlign': 'center'})
                )
            ]),
        ]),
    ]),
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

