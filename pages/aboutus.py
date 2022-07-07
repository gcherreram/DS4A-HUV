#Libraries
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard

#from app import app

#Add home to page registry
register_page(__name__, path="/aboutus", name="Equipo 237", title="Sobre Nosotros", order=6)

#Define content
content_about1=  dbc.Container([
    dbc.Row(html.H3("Equipo 237",style={'textAlign': 'center', "font-weight":"bold"})),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    dbc.CardImg(src="assets/images/JohnBolaños.jpeg"),
                    dbc.CardBody("John Bolaños", style={'textAlign': 'center', "font-weight":"bold"}),
                    ], className="w-75 mb-3"),
                ], justify="center"),
            dbc.Row([
                dbc.Card([
                    dbc.CardImg(src="assets/images/MateoMadrigal.jpeg"),
                    dbc.CardBody("Mateo Madrigal", style={'textAlign': 'center', "font-weight":"bold"}),
                    ], className="w-75 mb-3"),
                ], justify="center"),
        ]),
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    dbc.CardImg(src="assets/images/CarlosChoconta.png"),
                    dbc.CardBody("Carlos Chocontá", style={'textAlign': 'center', "font-weight":"bold"}),
                    ], className="w-75 mb-3"),
                ], justify="center"),
            dbc.Row([
                dbc.Card([
                    dbc.CardImg(src="assets/images/KarlaMuñoz.jpeg"),
                    dbc.CardBody("Karla Muñoz", style={'textAlign': 'center', "font-weight":"bold"}),
                    ], className="w-75 mb-3"),
                ], justify="center"),
        ]),
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    dbc.CardImg(src="assets/images/GabrielHerrera.jpeg"),
                    dbc.CardBody("Gabriel Herrera", style={'textAlign': 'center', "font-weight":"bold"}),
                    ], className="w-75 mb-3"),
                ], justify="center"),
            dbc.Row([
                dbc.Card([
                    dbc.CardImg(src="assets/images/AngelaOlarte.jpeg"),
                    dbc.CardBody("Angela Olarte", style={'textAlign': 'center', "font-weight":"bold"}),
                    ], className="w-75 mb-3"),
                ], justify="center"),
            ]),
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    dbc.CardImg(src="assets/images/AnaLoaiza.jpeg"),
                    dbc.CardBody("Ana Loaiza", style={'textAlign': 'center', "font-weight":"bold"}),
                    ], className="w-75 mb-3"),
                ], justify="center"),
            dbc.Row([
                dbc.Card([
                    dbc.CardImg(src="assets/images/WilsonRangel.jpeg"),
                    dbc.CardBody("Wilson Rangel", style={'textAlign': 'center', "font-weight":"bold"}),
                    ], className="w-75 mb-3"),
                ], justify="center"),
        ]),    
    ]),
])

content_about2=dbc.Container([
    dbc.Row(html.H3("Agradecimientos", style={'textAlign': 'center', "font-weight":"bold"})),
    dbc.Row([
        dbc.Carousel(
            items = [
                {
                    "key": "1",
                    "src": "/assets/images/Background_Thanks_adobe.png",
                    "header": "A nuestros TAs Diana Rodríguez y Rodolfo Meza ",
                },
                {
                    "key": "2",
                    "src": "/assets/images/Background_Thanks_adobe.png",
                    "header": "A todo el equipo de Correlation One",
                },
                {
                    "key": "3",
                    "src": "/assets/images/Background_Thanks_adobe.png",
                    "header": "Al Hospital Universitario del Valle",
                },

                ],
                controls=False,
                indicators=False,
                interval=3000,
                ride="carousel",
                variant = "dark",
            ),
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
        dbc.Col([
            dbc.Row(content_about2),
            dbc.Row(content_about1),
            ]),
        ],
        align="start",
        justify="between"
        ),          
    ]
)