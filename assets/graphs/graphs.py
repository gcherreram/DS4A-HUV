from dash import dcc
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np
import seaborn as sns
import folium
import json
import plotly.graph_objects as go
from dash_bootstrap_templates import load_figure_template

#Set display options
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

#Import own functions
from assets.graphs.alertgenerator import create_alerts
from assets.maps.mapgenerator import generate_map

#Set graph template
load_figure_template("cosmo")

# Load the data
dfResLab = pd.read_csv("data/databases/RESULTADOS_LAB.csv", on_bad_lines='skip', delimiter =";")

#Define time variables
#Date of birth
dfResLab['FECHA DE NACIMIENTO'].replace({"SIN DATO":np.nan}, inplace=True) 
dfResLab['FECHA DE NACIMIENTO'] = dfResLab['FECHA DE NACIMIENTO'].astype(str)
dfResLab['FECHA DE NACIMIENTO'] = pd.to_datetime(dfResLab['FECHA DE NACIMIENTO'], dayfirst=True)
#Date of sample
dfResLab['FECHA DE TOMA DE MUESTRA'] = pd.to_datetime(dfResLab['FECHA DE TOMA DE MUESTRA'], dayfirst=True)

#Create additional features
#Patients' ages
dfResLab.sort_values(by="IDENTIFICACION")
dfResLab["EDAD"] = (dfResLab['FECHA DE TOMA DE MUESTRA'] - dfResLab['FECHA DE NACIMIENTO']).dt.days
dfResLab["EDAD"] = (dfResLab["EDAD"]/365).round(decimals=0)
dfResLab["EDAD"].value_counts()
#Year of sample
dfResLab['AÑO DE TOMA DE MUESTRA'] = dfResLab['FECHA DE TOMA DE MUESTRA'].dt.year

#Import dictionary functions
from data.dictionaries.dictionaryMicro import dictTransform
from data.dictionaries.dictionaryUnit import dictTransformUnit

#Update microorganism names and add classifications by family, order, fungus/bacteria/gram
dfResLab["MICROORGANISMO"] = dictTransform(dfResLab["MICROORGANISMO"], "dic_rename_micro")
#Elimate records of microorganisms that were not precisely identified
df_eliminate=dfResLab[dfResLab['MICROORGANISMO']=='Eliminar'].index
dfResLab=dfResLab.drop(df_eliminate)
dfResLab["BACTERIA_HONGO"] = dictTransform(dfResLab["MICROORGANISMO"], "dic_bacteria_fungus")
dfResLab['FAMILIA_MICROORGANISMO'] = dictTransform(dfResLab["MICROORGANISMO"], "dic_family_microorganism")
dfResLab['ORDEN_MICROORGANISMO'] = dictTransform(dfResLab["MICROORGANISMO"], "dic_order_microorganism")
dfResLab['GRAM_MICROORGANISMO'] = dictTransform(dfResLab["MICROORGANISMO"], "dic_gram_microorganism")

#Update medicament names and add classification by families
dfResLab['ANTIBIOTICO'] = dictTransform(dfResLab['ANTIBIOTICO'], "dic_rename_antibiotic")
#Eliminate records of antibiotics that were not precisely identified
df_eliminate2=dfResLab[dfResLab['ANTIBIOTICO']=='Eliminar'].index
dfResLab=dfResLab.drop(df_eliminate2)
dfResLab['FAMILIA_ANTIBIOTICO'] = dictTransform(dfResLab['ANTIBIOTICO'], "dic_family_antibiotic")
dfResLab['TIPO_ANTIBIOTICO'] = dictTransform(dfResLab['ANTIBIOTICO'], "dic_type_antibiotic")

#Standardize hospital units, add unit code and classify by floor 
dfResLab['SALA'] = dictTransformUnit(dfResLab['SALA'], "dic_rename_unit")
df_eliminate3=dfResLab[dfResLab['SALA']=='eliminar'].index
dfResLab=dfResLab.drop(df_eliminate3)
dfResLab['CODIGO_SALA'] = dictTransformUnit(dfResLab['SALA'], "dic_code_unit")
dfResLab['PISO'] = dictTransformUnit(dfResLab['SALA'], "dic_floor_unit")

#Simplify resistance level name
dfResLab["RESISTENCIA"] = dfResLab['SENSIBLE / RESISTENTE / INTERMEDIO']
dfResLab.drop('SENSIBLE / RESISTENTE / INTERMEDIO', axis=1, inplace=True)
#Standardize resistance level values
#dfResLab[dfResLab["RESISTENCIA"]=="SIN ESPECIFICAR"]["RESISTENCIA"] = "X"
#dfResLab[dfResLab["RESISTENCIA"]=="N"]["RESISTENCIA"] = "I"
dfResLab["RESISTENCIA"].replace({"SIN ESPECIFICAR":"X","N":"I"}, inplace=True)

#Create alert variable in accordance to hospital codings
alerts_count = create_alerts(dfResLab)

#Create dataframe to group alerts by sample
alerts = dfResLab.groupby("CODIGO DE LA MUESTRA")["ALERTA"].sum()
alerts = (alerts != 0)
alerts = alerts.to_frame()
dfResLab_alerts = dfResLab.copy()
dfResLab_alerts = dfResLab_alerts.drop(['FECHA DE NACIMIENTO', 'GENERO', 'TIPO DE MUESTRA', 'LA CONCENTRACION MINIMA O MAX',
       'HOSPILTAL', 'NUMERO DE AISLAMIENTO', 'ESBL (+ es blee )', 'THM', 'APB (boronico)', 'EDTA (si son positivas o negativas)', 'EDAD',
       'BACTERIA_HONGO', 'ORDEN_MICROORGANISMO', 'GRAM_MICROORGANISMO', 'FAMILIA_ANTIBIOTICO',
       'TIPO_ANTIBIOTICO'], axis=1)

#Dataframes for demograpichs graphs
dfDemo = dfResLab[["AÑO DE TOMA DE MUESTRA", "GENERO", "EDAD", "IDENTIFICACION"]].groupby(by=["AÑO DE TOMA DE MUESTRA", "GENERO", 
"EDAD"], dropna=False).nunique().reset_index()

#Function to generate demographics graphs
def demo_graph_generator(year, gender, age):
    dfDemo1 = dfDemo
    if year!= "Todos":
        dfDemo1 = dfDemo1[dfDemo1["AÑO DE TOMA DE MUESTRA"]==year]
    if gender!="Todos":
        dfDemo1 = dfDemo1[dfDemo1["GENERO"]==gender]
    dfDemo2 = dfDemo1[dfDemo1["EDAD"].isin(age)].copy()
    dfDemo2.rename({"EDAD":"Edad", "GENERO":"Género", "IDENTIFICACION":"Frecuencia"}, axis=1, inplace=True)
    dfDemo2 = dfDemo2.sort_values(by="Frecuencia", ascending=True)
    demo_graph = px.bar(
        dfDemo2,
        y = "Frecuencia",
        x = "Edad",
        color = "Género",    
    )
    demo_graph.update_layout(
        title="IAAS por Género y Edad",
        font = {"size":10}
    )
    return demo_graph

#Function to generate microorganisms graphs
def micro_graph_generator(variable):
    
    dfMicro = dfResLab[[variable, "CODIGO DE LA MUESTRA"]].groupby(variable).nunique().reset_index()
    dfMicro = dfMicro.sort_values("CODIGO DE LA MUESTRA", ascending=False).head(20)
    dfMicro.rename(columns={variable:variable.title(), "CODIGO DE LA MUESTRA":"Frecuencia"}, inplace=True)
    dfMicro.sort_values(by="Frecuencia", ascending=True, inplace=True)
        
    if variable == "MICROORGANISMO":
        micro_title = "Microorganismos más frecuentes en los laboratorios (top 20)"
    elif variable == "ANTIBIOTICO":
        micro_title = "Medicamentos más utilizados en los laboratorios (top 20)"
        dfMicro.rename(columns={"Antibiotico":"Medicamentos"}, inplace=True)
    elif variable == "FAMILIA_MICROORGANISMO":
        micro_title = "Familias de microorganismos más frecuentes en los laboratorios (top 20)"
        dfMicro.rename(columns={"Familia_Microorganismo":"Familias Microorganismos"}, inplace=True)
    elif variable == "FAMILIA_ANTIBIOTICO":
        micro_title = "Familias de antibiotico más frecuentes en los laboratorios (top 20)"
        dfMicro.rename(columns={"Familia_Antibiotico":"Familias Medicamentos"}, inplace=True)
    elif variable == "BACTERIA_HONGO":
        dfMicro.rename(columns={"Bacteria_Hongo":"Bacteria / Hongo"}, inplace=True)
        micro_title = "Bacterias vs. Hongos"
    else:
        micro_title = "Titulo"

    micro_graph = px.bar(
        dfMicro,
        y=dfMicro.columns[0],
        x=dfMicro.columns[1],
        orientation = "h",
        color = "Frecuencia",
    )
    micro_graph.update_layout(
        title = micro_title,
        font = {"size":10} 
    )
    
    return micro_graph

#Function to generate microorganisms heatmaps
def micro_map_generator(year, variable1, variable2):

    top20Micro = dfResLab[["MICROORGANISMO","CODIGO DE LA MUESTRA"]].groupby(by="MICROORGANISMO").nunique().sort_values(by="CODIGO DE LA MUESTRA", 
        ascending=False).head(20).index
          
    if year == "Todos":
        dfMicro1 = dfResLab[dfResLab["MICROORGANISMO"].isin(top20Micro)][["AÑO DE TOMA DE MUESTRA", variable1, variable2, "CODIGO DE LA MUESTRA"]].groupby(by=["AÑO DE TOMA DE MUESTRA", 
            variable1, variable2]).nunique().reset_index()

    else:
        dfMicro1 = dfResLab[dfResLab["MICROORGANISMO"].isin(top20Micro)]
        dfMicro1 = dfMicro1[dfMicro1["AÑO DE TOMA DE MUESTRA"] == year][[variable1, variable2, 
            "CODIGO DE LA MUESTRA"]].groupby(by=[variable1, variable2]).nunique().reset_index() 
    
    micro_map = go.Figure(data=go.Heatmap(
        x = dfMicro1[variable1],
        y = dfMicro1[variable2],
        z = pd.crosstab(index=dfMicro1[variable1], columns=dfMicro1[variable2], values=dfMicro1["CODIGO DE LA MUESTRA"], 
            aggfunc="sum", dropna=False).stack(),        
        colorscale='Purples'))
    
    micro_map.update_layout(
        font = {"size":10},
        xaxis={"categoryorder": "category ascending"},
    )
   
    return micro_map

#Function to update maps with alerts
def alert_in_map(floor):
    df_alerts = []
    df_alerts = dfResLab_alerts.join(alerts, lsuffix='_left', rsuffix='_right')
    df_alerts = df_alerts.reset_index()
    df_alerts.drop(["ALERTA_right"], axis=1, inplace = True)
    df_alerts.rename({"ALERTA_left":"ALERTA"}, axis=1, inplace=True)
    df_alerts_unit = df_alerts[["CODIGO_SALA", "SALA", "ALERTA", "CODIGO DE LA MUESTRA"]].groupby(by=["CODIGO_SALA", 
        "SALA", "ALERTA"]).nunique().reset_index()
    df_alerts_unit = df_alerts_unit[df_alerts_unit["ALERTA"]==1]
    df_alerts_unit.sort_values(by="CODIGO DE LA MUESTRA", ascending=False)
    df_alerts_unit.rename({"CODIGO_SALA":"ID", "SALA":"NAME", "CODIGO DE LA MUESTRA":"CASOS"}, axis=1, inplace=True)
    floor_map = generate_map(df_alerts_unit, floor)

    return floor_map

#Function to generate microorganisms heatmaps
def alert_heatmap_generator(year):
       
    df_alerts = []
    df_alerts = dfResLab_alerts.join(alerts, lsuffix='_left', rsuffix='_right')
    df_alerts = df_alerts.reset_index()
    df_alerts.drop(["ALERTA_right"], axis=1, inplace = True)
    df_alerts.rename({"ALERTA_left":"ALERTA"}, axis=1, inplace=True)
    df_alerts["MES DE LA MUESTRA"] = df_alerts["FECHA DE TOMA DE MUESTRA"].dt.month
        
    if year == "Todos":
        df_alerts_unit = df_alerts[["SALA", "ALERTA", "CODIGO DE LA MUESTRA", "AÑO DE TOMA DE MUESTRA"]].groupby(by=["SALA", 
            "ALERTA", "AÑO DE TOMA DE MUESTRA"]).nunique().reset_index()
        df_alerts_unit = df_alerts_unit[df_alerts_unit["ALERTA"]==1]
        table_alert_unit = pd.crosstab(index=df_alerts_unit["AÑO DE TOMA DE MUESTRA"], 
            columns=df_alerts_unit["SALA"], values=df_alerts_unit["CODIGO DE LA MUESTRA"], aggfunc="sum", dropna=False)
        
        alert_heatmap = go.Figure(data=go.Heatmap(
            z = table_alert_unit.stack(),
            x = df_alerts_unit["AÑO DE TOMA DE MUESTRA"],
            y = df_alerts_unit["SALA"],
            colorscale='Reds'))
        
        alert_heatmap.update_layout(
        font = {"size":10},
        yaxis={"categoryorder": "category descending"},
        )
        
    else:
        df_alerts_unit = df_alerts[df_alerts["AÑO DE TOMA DE MUESTRA"] == year][["SALA", "ALERTA", "CODIGO DE LA MUESTRA", "AÑO DE TOMA DE MUESTRA", 
            "MES DE LA MUESTRA"]].groupby(by=["SALA", "ALERTA", "AÑO DE TOMA DE MUESTRA", 
            "MES DE LA MUESTRA"]).nunique().reset_index()
        df_alerts_unit = df_alerts_unit[df_alerts_unit["ALERTA"]==1]
        table_alert_unit = pd.crosstab(index=df_alerts_unit["MES DE LA MUESTRA"], 
            columns=df_alerts_unit["SALA"], values=df_alerts_unit["CODIGO DE LA MUESTRA"], aggfunc="sum", dropna=False)
    
        alert_heatmap = go.Figure(data=go.Heatmap(
            z = table_alert_unit.stack(),
            x = df_alerts_unit["MES DE LA MUESTRA"],
            y = df_alerts_unit["SALA"],
            colorscale='Reds'))

        alert_heatmap.update_layout(
            font = {"size":10},
            yaxis={"categoryorder": "category descending"},
        )   
    
    return alert_heatmap

    