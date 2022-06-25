#Libraries
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard
from components.cards.infocard import infocard
from assets.graphs.graphs import micro_graph_generator
from assets.graphs.graphs import micro_map_generator

#Add infections to page registry
register_page(__name__, path="/infections", name="Infecciones", 
    title="Dashboard para el monitoreo de IAAS en el HUV - Infecciones", order=3)

#Side menu cards
demographics_card = sidecard("Demografía", "Pacientes afectados por IAAS en el hospital.", "/demographics")
infections_card = sidecard("Infecciones", "Microorganismos que están causando IAAS en el hospital", "/infections")
alerts_card = sidecard("Alertas", "Alertas por IAAS", "/alerts")
info_card = infocard("@DS4A Colombia\n Cohort 6\n Team 237", "/assets/images/DS4Alogo.png")

#Start microorganism graph
Microorganisms_fig = micro_graph_generator("MICROORGANISMO")

#Generate page content
content_infections1 = dbc.Container([                

    dbc.Col([                    
            dcc.Dropdown(['Microorganismos', 'Familias de Microorganismos', 'Medicamentos'], 
                "Microorganisms", id='fig2_dropdown', placeholder="Seleccione un gráfica"),
            dcc.Graph(figure=Microorganisms_fig, id='microorganisms_figure'),
            ], style={'textAlign': 'center'}),                      
])

content_infections2 = dbc.Container([
    dbc.Col([
            dbc.Col([   
                dbc.Row(dcc.Slider(min=2013, max=2022, step=1, value=2013, id='micro_map_slider2')),
                dbc.Row(dcc.Graph(figure=micro_map_generator("Todos", "FAMILIAS MICROORGANISMOS", 
                    "SENSIBLE / RESISTENTE / INTERMEDIO"), id='micro_map_figure2'))
            ])
    ], style={'textAlign': 'center'})
])

#Define layout
layout = html.Div([
    dbc.Row(
        [
         dbc.Col([
            dbc.Row(demographics_card),
            dbc.Row(infections_card),
            dbc.Row(alerts_card),
            ], width=2),
        dbc.Col([
            dbc.Row(html.H3("Caracterización de las IAAS en el HUV", 
            style={'textAlign': 'center', "font-weight":"bold"}, id="subtitle")),
            dbc.Row([
                dbc.Col(dbc.Row(content_infections1, justify="between"), width=7, align="center"),
                dbc.Col(dbc.Row(content_infections2, justify="between"), align="center"),
                ]),           
            ]),           
        ]
    ),
    dbc.Row(info_card, justify="between")    
])

#Callbacks

@callback(
    [Output('microorganisms_figure', 'children')], 
    [Input('fig2_dropdown', 'value')],
    prevent_initial_call=True)

def dropdown_interaction(dropdown_val):

    if dropdown_val == 'Microorganismos':
        variable = "MICROORGANISMO"
    elif dropdown_val == 'Familias de Microorganismos':
        variable = "FAMILIAS MICROORGANISMOS"
    else:
        variable = "ANTIBIOTICO"

    figure = micro_graph_generator(variable)

    return [figure]


"""@callback(
    [Output('micro_map_figure1', 'children')], 
    [Input('micro_map_slider1', 'value')],
    prevent_initial_call=True)

def slider1_interaction(slider_val):
    figure=micro_map_generator(slider_val,"FAMILIAS MICROORGANISMOS", "SALA")
    return [figure]"""


@callback(
    [Output('micro_map_figure2', 'children')], 
    [Input('micro_map_slider2', 'value')],
    prevent_initial_call=True)

def slider2_interaction(slider_val):
    figure = micro_map_generator(slider_val,"FAMILIAS MICROORGANISMOS", "SENSIBLE / RESISTENTE / INTERMEDIO")
    return [figure]

