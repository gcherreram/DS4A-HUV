#Libraries
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard
from assets.graphs.graphs import alert_heatmap_generator
from assets.graphs.graphs import alert_in_map

#Add alerts to page registry
register_page(__name__, path="/alerts", name= "Alertas", 
    title="Dashboard para el monitoreo de IAAS en el HUV - Alertas", order=2)

#Side menu cards
demographics_card = sidecard("Demografía", "Perfil de los Pacientes", "/demographics")
infections_card = sidecard("Infecciones", "Perfil de los Microorganismos", "/infections")
alerts_card = sidecard("Alertas", "Histórico de Alertas por IAAS", "/alerts")
earlyalerts_card = sidecard("Modelo", "Modelo de Alertas Tempranas", "/modelalerts")

#Generate page content

content_alerts1 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("Alertas por piso", style={'textAlign': 'center', "font-weight":"bold"}),
        dbc.Row(dcc.Dropdown(["Primer Piso", "Segundo Piso", "Tercer Piso", "Cuarto Piso", "Quinto Piso", "Sexto Piso"], 
            value='Perimer Piso', id="alert_map_dropdown")),
        dbc.Row(dcc.Graph(figure=alert_in_map("Primer Piso"), id='alert_map_figure1')
            ,justify="center"),
        ])
    ])
])

content_alerts2 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("Histórico de Alertas", style={'textAlign': 'center', "font-weight":"bold"}),
        dbc.Row(dcc.Graph(figure=alert_heatmap_generator("Todos"), id='alert_map_figure2')
            ,justify="center"),
        ])
    ])
])

content_alerts3 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("Alertas por año y mes", style={'textAlign': 'center', "font-weight":"bold"}),
        dbc.Row(dcc.Slider(min=2013, max=2021, step=1, value=2013, id='alert_map_slider',
            marks={
                2013:{"label":"2013"}, 
                2015:{"label":"2015"},
                2017:{"label":"2017"},
                2019:{"label":"2019"},
                2021:{"label":"2021"},},
            tooltip={"placement": "bottom", "always_visible": True}
            )),
        dbc.Row(dcc.Graph(figure=alert_heatmap_generator(2013), id='alert_map_figure2')
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
        dbc.Col([
            dbc.Row(html.H4("Alertas por IAAS en el HUV", 
            style={'textAlign': 'center', "font-weight":"bold"}, id="subtitle")),  
            dbc.Tabs([
                dbc.Tab(content_alerts1, label="Mapa por piso"),           
                dbc.Tab(content_alerts2, label="Histórico"),
                dbc.Tab(content_alerts3, label="Por año y mes"),
                ])                                    
        
        ]),
    ],
    align="start",
    justify="between"
    ),            
]
)

#Callbacks
@callback(
    [Output('alert_map_figure1', 'figure')], 
    [Input('alert_map_dropdown', 'value')],
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
    elif dropdown_val == "Sexto Piso":
        selected_floor = "sixth"    
    else:
        selected_floor = "first"

    figure=alert_in_map(selected_floor)

    return [figure]


@callback(
    [Output('alert_map_figure2', 'figure')], 
    [Input('alert_map_slider', 'value')],
    prevent_initial_call=True)

def map_slider_interaction(slider_val):
    figure=alert_heatmap_generator(slider_val)
    return [figure]
