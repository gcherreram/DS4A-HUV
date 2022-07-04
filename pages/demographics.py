#Libraries
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard
from assets.graphs.graphs import demo_graph_generator

#Add demographics to page registry
register_page(__name__, path="/demographics", name="Demografia", 
    title="Dashboard para el monitoreo de IAAS en el HUV - Demografía", order=2)

#Logos
HUV_logoII = "https://huv.gov.co/wp-content/uploads/2020/06/logo-HU_Horizontal_Azul.png"


#Generate page content
content_demo1 = dbc.Container([
    dbc.Row(dcc.Dropdown(options=['Todos', 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
        placeholder="Año", id="year_dropdown")),
    dbc.Row(dcc.Dropdown(["Todos", "Femenino", "Masculino", "Sin Especificar"], placeholder="Género", id="gender_dropdown")),
    dbc.Row(dcc.Dropdown(["Todos", "Menores de 5 años", "Entre 5 y 17 años", "Entre 18 y 60 años", "Mayores de 60"], 
        placeholder="Edad", id="age_dropdown")),
    dbc.Row(dbc.Button("Generar", id="demographics_button", class_name="me-2", n_clicks=0))
])

#Start graphs
demographics_fig = demo_graph_generator("Todos", "Todos", list(range(0,120,1)))

content_demo2 = dbc.Container([
    dbc.Row(dcc.Graph(figure=demographics_fig, id="demographics_fig")),
])

#Side menu cards
demographics_card = sidecard("Demografía", "Perfil de los Pacientes", "/demographics")
infections_card = sidecard("Infecciones", "Perfil de los Microorganismos", "/infections")
alerts_card = sidecard("Alertas", "Histórico de Alertas por IAAS", "/alerts")
earlyalerts_card = sidecard("Alertas Tempranas", "Modelo de Alertas Tempranas", "/modelalerts")

#Define layout
layout = html.Div([
    dbc.Row(
        [
         dbc.Col([
            dbc.Row(demographics_card),
            dbc.Row(infections_card),
            dbc.Row(alerts_card),
            dbc.Row(earlyalerts_card),
            ], width=2),
        dbc.Col([
            dbc.Row(html.H3("Caracterización de los pacientes afectados por IAAS en el HUV", 
            style={'textAlign': 'center', "font-weight":"bold"}, id="subtitle")),
            dbc.Row([
                dbc.Col(dbc.Row(content_demo1, justify="between"), width=2, align="center"),
                dbc.Col(dbc.Row(content_demo2, justify="between"), align="center"),
            ]),           
            ]),           
        ]
    ),       
])

#Callbacks      
@callback(
        [Output("demographics_fig", "figure")], 
        [State("year_dropdown", "value"), 
         State("gender_dropdown","value"),
         State("age_dropdown","value"),
         Input("demographics_button", "n_clicks"),
        ]
    )

def update_demographics(selector_year, selector_gender, selector_age, n_clicks):

    if selector_gender == "Sin Especificar":
        selector_gender = "SIN ESPECIFICAR"

    if selector_age == "Todos":
        selector_age = list(range(0,120,1))
    elif selector_age == "Menores de 5 años":
        selector_age = list(range(0,5,1))
    elif selector_age == "Entre 5 y 17 años":
        selector_age = list(range(5,18,1))
    elif selector_age == "Entre 18 y 60 años":
        selector_age = list(range(18,60,1))
    else:
        selector_age = list(range(60,120,1))

    if n_clicks is not None:
        new_demographics_fig = demo_graph_generator(selector_year, selector_gender, selector_age)
        return [new_demographics_fig]