#Libraries
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidecard import sidecard
from assets.graphs.graphs import micro_graph_generator
from assets.graphs.graphs import micro_map_generator

#Add infections to page registry
register_page(__name__, path="/infections", name="Infecciones", 
    title="Dashboard para el monitoreo de IAAS en el HUV - Infecciones", order=3)

#Side menu cards
demographics_card = sidecard("Demografía", "Perfil de los Pacientes", "/demographics")
infections_card = sidecard("Infecciones", "Perfil de los Microorganismos", "/infections")
alerts_card = sidecard("Alertas", "Histórico de Alertas por IAAS", "/alerts")
earlyalerts_card = sidecard("Alertas Tempranas", "Modelo de Alertas Tempranas", "/modelalerts")

#Generate page content
content_infections1 = dbc.Card([
    dbc.CardBody([
        dcc.Dropdown(['Microorganismos', 'Familias de Microorganismos', 'Medicamentos', 'Bacteria/Hongo'], 
            "Microorganisms", id='fig2_dropdown', placeholder="Seleccione un gráfica"),
        dcc.Graph(figure=micro_graph_generator("MICROORGANISMO"), id='microorganisms_figure'),
    ])                                       
])

content_infections2 = dbc.Card([
    dbc.CardBody([
        html.H6("Top 20 Microorganismos por Piso", style={'textAlign': 'center', "font-weight":"bold"}),
        dbc.Row(dcc.Slider(min=2013, max=2021, step=1, value=2013, id='micro_map_slider1',
            marks={
                2013:{"label":"2013"}, 
                2015:{"label":"2015"},
                2017:{"label":"2017"},
                2019:{"label":"2019"},
                2021:{"label":"2021"},},
            tooltip={"placement": "bottom", "always_visible": True}
            )),
        dbc.Row(dcc.Graph(figure=micro_map_generator(2013, "MICROORGANISMO", 
            "PISO"), id='micro_map_figure1'
        )),
    ])
])
    
content_infections3 = dbc.Card([
    dbc.CardBody([
        html.H6("Top 20 Microorganismos por Resistencia Antibiótica", style={'textAlign': 'center', "font-weight":"bold"}),
        dbc.Row(dcc.Slider(min=2013, max=2021, step=1, id='micro_map_slider2',
            marks={
                2013:{"label":"2013"}, 
                2015:{"label":"2015"},
                2017:{"label":"2017"},
                2019:{"label":"2019"},
                2021:{"label":"2021"},},
            tooltip={"placement": "bottom", "always_visible": True}
            )),
        dbc.Row(dcc.Graph(figure=micro_map_generator(2013, "MICROORGANISMO", 
            "RESISTENCIA"), id='micro_map_figure2')
            ,justify="center"),
    ])
])
        

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
            dbc.Row(html.H3("Caracterización de las IAAS en el HUV", 
            style={'textAlign': 'center', "font-weight":"bold"}, id="subtitle")),  
            dbc.Tabs([
                dbc.Tab(content_infections1, label="Gráficas resumen"),           
                dbc.Tab(content_infections2, label="Tabla comparativa por piso y año"),
                dbc.Tab(content_infections3, label="Tabla comparativa por resistencia y año")
            ])                                    
        ])       
    ])
])

#Callbacks
    
@callback(
    [Output('microorganisms_figure', 'figure')], 
    [Input('fig2_dropdown', 'value')],
    )

def dropdown_interaction(dropdown_val):

    if dropdown_val == 'Medicamentos':
        variable = "ANTIBIOTICO"
    elif dropdown_val == 'Familias de Microorganismos':
        variable = "FAMILIA_MICROORGANISMO"
    elif dropdown_val == "Bacteria/Hongo":
        variable = "BACTERIA_HONGO"
    else:
        variable = "MICROORGANISMO"

    figure = micro_graph_generator(variable)

    return [figure]


@callback(
    [Output('micro_map_figure1', 'figure')], 
    [Input('micro_map_slider1', 'value')],
    prevent_initial_call=True)

def slider1_interaction(slider_val):
    figure=micro_map_generator(slider_val,"MICROORGANISMO", "PISO")
    return [figure]


@callback(
    [Output('micro_map_figure2', 'figure')], 
    [Input('micro_map_slider2', 'value')],
    prevent_initial_call=True)

def slider2_interaction(slider_val):
    
    figure = micro_map_generator(slider_val,"MICROORGANISMO", "RESISTENCIA")
    return [figure]

