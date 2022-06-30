from dash import dcc
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np
import seaborn as sns
from dash_bootstrap_templates import load_figure_template

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
dfResLab['FAMILIA_ANTIBIOTICO'] = dictTransform(dfResLab['ANTIBIOTICO'], "dic_family_antibiotic")
dfResLab['TIPO_ANTIBIOTICO'] = dictTransform(dfResLab['ANTIBIOTICO'], "dic_type_antibiotic")

#Standardize hospital units and classify by floor
dfResLab['SALA'] = dictTransformUnit(dfResLab['SALA'], "dic_rename_unit")
df_eliminate=dfResLab[dfResLab['SALA']=='eliminar'].index
dfResLab=dfResLab.drop(df_eliminate)
dfResLab['PISO'] = dictTransformUnit(dfResLab['SALA'], "dic_floor_unit")

#Simplify resistance level name
dfResLab["RESISTENCIA"] = dfResLab['SENSIBLE / RESISTENTE / INTERMEDIO']
dfResLab["RESISTENCIA"].rename({"SIN ESPECIFICAR":"X","N":"R"}, axis=0, inplace=True)

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
    dfDemo1 = dfDemo1[dfDemo1["EDAD"].isin(age)]
    dfDemo1.rename({"EDAD":"Edad", "GENERO":"Género", "IDENTIFICACION":"Frecuencia"}, axis=1, inplace=True)
    dfDemo1.sort_values(by="Frecuencia", ascending=True, inplace=True)
    demo_graph = px.bar(
        dfDemo1,
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
    )
    micro_graph.update_layout(
        title = micro_title,
        font = {"size":10} 
    )
    
    return micro_graph

#Generate dataframes for heatmaps

#Function to generate microorganisms heatmaps
def micro_map_generator(year, variable1, variable2):

    
    dfMicro1 = dfResLab[["AÑO DE TOMA DE MUESTRA", variable1, variable2, "CODIGO DE LA MUESTRA"]].groupby(by=["AÑO DE TOMA DE MUESTRA", 
    variable1, variable2]).nunique().reset_index()
        
    if year == "Todos":
        table_micro_unit = pd.crosstab(index=dfMicro1[variable1], columns=dfMicro1[variable2], normalize="index", dropna=False)*100
        
    else:
        dfMicro2 = dfMicro1[dfMicro1["AÑO DE TOMA DE MUESTRA"] == year]
        table_micro_unit = pd.crosstab(index=dfMicro2[variable1], columns=dfMicro2[variable2], normalize="index", dropna=False)*100
            
    micro_map = px.imshow(
        table_micro_unit, 
        color_continuous_scale="purples"
        )
    
    return micro_map
    