from dash import dcc
import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns

# Load the data
dfResLab = pd.read_csv("data/databases/RESULTADOS_LAB.csv", on_bad_lines='skip', delimiter =";")

#Define time variables
#Date of birth
dfResLab['FECHA DE NACIMIENTO'].replace({"SIN DATO":"NaN"}, inplace=True) 
dfResLab['FECHA DE NACIMIENTO'].unique()
dfResLab['FECHA DE NACIMIENTO'] = dfResLab['FECHA DE NACIMIENTO'].astype(str)
dfResLab['FECHA DE NACIMIENTO'] = pd.to_datetime(dfResLab['FECHA DE NACIMIENTO'], dayfirst=True)
#Date of sample
dfResLab['FECHA DE TOMA DE MUESTRA'] = pd.to_datetime(dfResLab['FECHA DE TOMA DE MUESTRA'], dayfirst=True)

#Create additional features
#Patients' ages
dfResLab["EDAD"] = (dfResLab['FECHA DE TOMA DE MUESTRA'] - dfResLab['FECHA DE NACIMIENTO']).dt.days
dfResLab["EDAD"] = (dfResLab["EDAD"]/365).round(decimals=0)
dfResLab["EDAD"].value_counts()
#Year of sample
dfResLab['AÑO DE TOMA DE MUESTRA'] = dfResLab['FECHA DE TOMA DE MUESTRA'].dt.year

#Grouping microorganisms in families
from data.dictionaries.dictionaryMicro import dictTransform
dfResLab["FAMILIAS MICROORGANISMOS"] = dictTransform(dfResLab["MICROORGANISMO"])

#Dataframes for demograpichs graphs
dfDemo = dfResLab[["AÑO DE TOMA DE MUESTRA", "GENERO", "EDAD", "IDENTIFICACION", "FECHA DE TOMA DE MUESTRA", 
"CODIGO DE LA MUESTRA"]].groupby(by=["AÑO DE TOMA DE MUESTRA", "GENERO", "EDAD", "IDENTIFICACION", 
"FECHA DE TOMA DE MUESTRA"]).count().reset_index()

#Function to generate demographics graphs
def demo_graph_generator(year, gender, age):
    dfDemo1 = dfDemo
    if year!= "Todos":
        dfDemo1 = dfDemo1[dfDemo1["AÑO DE TOMA DE MUESTRA"]==year]
    if gender!="Todos":
        dfDemo1 = dfDemo1[dfDemo1["GENERO"]==gender]
    dfDemo1 = dfDemo1[dfDemo1["EDAD"].isin(age)]
    dfDemo1 = dfDemo1["GENERO"].value_counts().to_frame().reset_index()
    dfDemo1.rename(columns={"index":"Género", "GENERO":"Frecuencia"}, inplace=True)
    dfDemo1.sort_values(by="Frecuencia", ascending=True, inplace=True)
    demo_graph = px.bar(
        dfDemo1,
        y="Frecuencia",
        x="Género",
    )
    demo_graph.update_layout(
        title="IAAS por Género y Edad",
        font = {"size":10}
    )
    return demo_graph

#Function to generate microorganisms graphs
def micro_graph_generator(variable):
    
    dfMicro = dfResLab[["FECHA DE TOMA DE MUESTRA", "IDENTIFICACION", "MICROORGANISMO", "FAMILIAS MICROORGANISMOS", "ANTIBIOTICO",
    "CODIGO DE LA MUESTRA"]].groupby(by=["FECHA DE TOMA DE MUESTRA", "IDENTIFICACION", "FAMILIAS MICROORGANISMOS", "ANTIBIOTICO",
    "MICROORGANISMO"]).count().reset_index()
    dfMicro = dfMicro[variable].value_counts().head(20).to_frame().reset_index()
    dfMicro.rename(columns={"index":variable.title(), variable:"Frecuencia"}, inplace=True)
    dfMicro.sort_values(by="Frecuencia", ascending=True, inplace=True)
        
    if variable == "MICROORGANISMO":
        micro_title = "Microorganismos más frecuentes en los laboratorios (top 20)"
    elif variable == "ANTIBIOTICO":
        micro_title = "Antibioticos más utilizados en los laboratorios (top 20)"
    elif variable == "FAMILIAS MICROORGANISMOS":
        micro_title = "Familias de microorganismos más frecuentes en los laboratorios (top 20)"
    else:
        micro_title = "Titulo"

    micro_graph = px.bar(
        dfMicro,
        y=dfMicro.columns[0],
        x=dfMicro.columns[1],
        orientation = "h",   
    )
    micro_graph.update_layout(
        title = micro_title,
        font = {"size":10} 
    )
    
    return micro_graph
"""def micro_graph_generator(variable):
    micro_title = "Titulo"
    if variable == "MICROORGANISMO":
        dfMicro = dfResLab[["FECHA DE TOMA DE MUESTRA", "IDENTIFICACION", "MICROORGANISMO", 
        "CODIGO DE LA MUESTRA"]].groupby(by=["FECHA DE TOMA DE MUESTRA", "IDENTIFICACION", "MICROORGANISMO"]).count().reset_index()
        dfMicro = dfMicro["MICROORGANISMO"].value_counts().head(20).to_frame().reset_index()
        dfMicro.rename(columns={"index":"Microorganismo", "MICROORGANISMO":"Frecuencia"}, inplace=True)
        dfMicro.sort_values(by="Frecuencia", ascending=True, inplace=True)
        micro_title = "Microorganismos más frecuentes en los laboratorios (top 20)"
    elif variable == "ANTIBIOTICO":
        dfMicro = dfResLab[["FECHA DE TOMA DE MUESTRA", "IDENTIFICACION", "ANTIBIOTICO", 
        "CODIGO DE LA MUESTRA"]].groupby(by=["FECHA DE TOMA DE MUESTRA", "IDENTIFICACION", "ANTIBIOTICO"]).count().reset_index()
        dfMicro = dfMicro["ANTIBIOTICO"].value_counts().head(20).to_frame().reset_index()
        dfMicro.rename(columns={"index":"Medicamento", "ANTIBIOTICO":"Frecuencia"}, inplace=True)
        dfMicro.sort_values(by="Frecuencia", ascending=True, inplace=True)
        micro_title = "Antibioticos más utilizados en los laboratorios (top 20)"
    elif variable == "FAMILIAs MICROORGANISMOS":
        dfMicro = dfResLab[["FECHA DE TOMA DE MUESTRA", "IDENTIFICACION", "FAMILIAs MICROORGANISMO", 
        "CODIGO DE LA MUESTRA"]].groupby(by=["FECHA DE TOMA DE MUESTRA", "IDENTIFICACION", "FAMILIAS MICROORGANISMOS"]).count().reset_index()                   
        dfMicro = dfResLab["FAMILIAS MICROORGANISMOS"].value_counts().head(20).to_frame().reset_index()
        dfMicro.rename(columns={"index":"Familia de Microorganismos", "FAMILIAS MICROORGANISMOS":"Frecuencia"}, inplace=True)
        dfMicro.sort_values(by="Frecuencia", ascending=True, inplace=True)
        micro_title = "Familias de microorganismos más frecuentes en los laboratorios (top 20)"
    else:
        dfMicro = dfResLab

    micro_graph = px.bar(
        dfMicro,
        y=dfMicro.columns[0],
        x=dfMicro.columns[1],
        orientation = "h",   
    )
    micro_graph.update_layout(
        title = micro_title,
        font = {"size":10} 
    )
    
    return micro_graph"""


#Generate dataframes for heatmaps
dfMicro1 = dfResLab[["AÑO DE TOMA DE MUESTRA", "FAMILIAS MICROORGANISMOS", "SALA", "FECHA DE TOMA DE MUESTRA", "ANTIBIOTICO", 
"SENSIBLE / RESISTENTE / INTERMEDIO", "CODIGO DE LA MUESTRA"]].groupby(by=["AÑO DE TOMA DE MUESTRA", "FAMILIAS MICROORGANISMOS", "SALA", 
"FECHA DE TOMA DE MUESTRA", "ANTIBIOTICO", "SENSIBLE / RESISTENTE / INTERMEDIO", "CODIGO DE LA MUESTRA"]).count().reset_index()

#Function to generate microorganisms heatmaps
def micro_map_generator(year, variable1, variable2):
    pd.set_option("display.max_rows", 100)
    if year == "Todos":
        table_micro_unit = pd.crosstab(index=dfMicro1[variable1], columns=dfMicro1[variable2], normalize="index")*100
        table_micro_unit.style.set_properties({"font-size":"24pt"})
    else:
        dfMicro2 = dfMicro1[dfMicro1["AÑO DE TOMA DE MUESTRA"] == year]
        table_micro_unit = pd.crosstab(index=dfMicro2[variable1], columns=dfMicro2[variable2], normalize="index")*100
        table_micro_unit.style.set_properties({"font-size":"24pt"})
    micro_map = px.imshow(
        table_micro_unit, 
        color_continuous_scale="blues"
        )
    
    return micro_map 
    