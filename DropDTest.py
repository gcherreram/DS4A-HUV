from unittest.mock import MagicProxy
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
 
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
sns.set_style(style = 'whitegrid')

# Load the data
dfResLab = pd.read_csv("data/RESULTADOS_LAB.csv", on_bad_lines='skip', delimiter =";",low_memory=False)
dfNotObl = pd.read_csv("data/EVENTOS_NOTIFICACION_OBLIGATORIA.csv",on_bad_lines='skip', delimiter =";",low_memory=False)
dfRuaf = pd.read_csv("data/RUAF_ND.csv",on_bad_lines='skip', delimiter =";",low_memory=False)

#Grouping microorganisms in families
import dictionaryMicro
dfResLab["FAMILIAS_MICROORGANISMOS"] = dictionaryMicro.dictTransform(dfResLab["MICROORGANISMO"])

#Merge of lab results and death certificates keeping all patients
#dfRuaf.rename(columns={"NÚMERO DOCUMENTO ":"IDENTIFICACION"}, inplace = True)
#dfMergeLabRuafI = pd.merge(dfResLab, dfRuaf, how= "left", on='IDENTIFICACION', indicator=True)
#dfMergeLabRuafI["FALLECIO"] = dfMergeLabRuafI["_merge"]
#dfMergeLabRuafI["FALLECIO"].replace({"left_only":"No", "both":"Si"}, inplace=True)

#Append compulsory notification keeping all patients
#dfNotObl.rename(columns={"IDENTIFICACIÓN":"IDENTIFICACION"}, inplace=True)
#dfMergeAll = pd.merge(dfMergeLabRuafI, dfNotObl, how="left", on='IDENTIFICACION', indicator=True)
#dfMergeAll["NOTIFICADO"] = dfMergeAll["_merge"]
#dfMergeAll["NOTIFICADO"].replace({"left_only":"No", "both":"Si"}, inplace=True)
#dfMergeAll.drop("_merge")


#Create the relevant graphs
dfMicroorganisms = dfResLab["MICROORGANISMO"].value_counts().head(20).to_frame().reset_index()
dfMicroorganisms.rename(columns={"index":"Microorganism", "MICROORGANISMO":"Frequency"}, inplace=True)

dfAntibiotics = dfResLab["ANTIBIOTICO"].value_counts().head(20).to_frame().reset_index()
dfAntibiotics.rename(columns={"index":"Antibiotic", "ANTIBIOTICO":"Frequency"}, inplace=True)

dfFamilies = dfResLab["FAMILIAS_MICROORGANISMOS"].value_counts().to_frame().reset_index()
dfFamilies.rename(columns={"index":"Microorganism Family", "FAMILIAS_MICROORGANISMOS":"Frequency"}, inplace=True)

#Microorganisms
Microorganisms_fig = px.bar(
    dfMicroorganisms,
    y="Microorganism",
    x="Frequency",
    orientation = "h"    
)
Microorganisms_fig.update_layout(
    title="Top 20 Microorganisms"
)

#Microorganisms families
Families_fig = px.bar(
    dfFamilies,
    x="Microorganism Family",
    y="Frequency",
)
Families_fig.update_layout(
    title="Microorganism Family"
)

#Antibiotics
Antibiotics_fig = px.bar(
    dfAntibiotics,
    y="Antibiotic",
    x="Frequency",
    orientation = "h"
)
Antibiotics_fig.update_layout(
    title="Top 20 Antibiotics"
)

# Create the app
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
    
# Create Layout
app.layout = html.Div([
    html.H1(children='Dashboard - Hospital Universitario del Valle',
        style={'textAlign': 'center'}, id="title"), #Creates the title of the app
    html.H2("Microorganisms", style={'textAlign': 'center'}, id="subtitle"), 
    dcc.Dropdown(['Microorganisms', 'Microorganisms Family', 'Antibiotics'], "Microorganisms", id='fig-dropdown'),
    dcc.Graph(figure=Microorganisms_fig,id='microorganisms-figure'),
])

@app.callback(Output('microorganisms-figure', 'figure'), [Input('fig-dropdown', 'value')])
def dropdown_interaction(dropdown_val):
    if dropdown_val == "Microorganisms":
        fig = Microorganisms_fig
    elif dropdown_val=='Microorganisms Family':
        fig = Families_fig
    else:
        fig = Antibiotics_fig

    return fig

#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port='8050',debug=True)