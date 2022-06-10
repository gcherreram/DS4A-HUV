
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
dfMicroorganisms.sort_values(by="Frequency", ascending=True, inplace=True)

dfAntibiotics = dfResLab["ANTIBIOTICO"].value_counts().head(20).to_frame().reset_index()
dfAntibiotics.rename(columns={"index":"Antibiotic", "ANTIBIOTICO":"Frequency"}, inplace=True)
dfAntibiotics.sort_values(by="Frequency", ascending=True, inplace=True)

dfFamilies = dfResLab["FAMILIAS_MICROORGANISMOS"].value_counts().to_frame().reset_index()
dfFamilies.rename(columns={"index":"Microorganism Family", "FAMILIAS_MICROORGANISMOS":"Frequency"}, inplace=True)
dfFamilies.sort_values(by="Frequency", ascending=True, inplace=True)

dfCauseDeath = dfRuaf["CAUSA DIRECTA"].value_counts().head(20).to_frame().reset_index()
dfCauseDeath.rename(columns={"index":"Direct Cause of Death", "CAUSA DIRECTA":"Frequency"}, inplace=True)
dfCauseDeath.sort_values(by="Frequency", ascending=True, inplace=True)

dfSex = dfRuaf["SEXO "].value_counts().to_frame().reset_index()
dfSex.rename(columns={"index":"Sex", "SEXO ":"Frequency"}, inplace=True)
 
dfTypeDeath = dfRuaf["TIPO DEFUNCIÓN"].value_counts().to_frame().reset_index()
dfTypeDeath.rename(columns={"index":"Type of Death", "TIPO DEFUNCIÓN":"Frequency"}, inplace=True)

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
    y="Microorganism Family",
    x="Frequency",
    orientation = "h"
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

#Cause of Death
CauseDeath_fig = px.bar(
    dfCauseDeath,
    y="Direct Cause of Death",
    x="Frequency",
    orientation = "h"
)
CauseDeath_fig.update_layout(
    title="Top 20 Cause of Death"
)

#Sex
Sex_fig = px.bar(
    dfSex,
    y="Frequency",
    x="Sex",
)
Sex_fig.update_layout(
    title="Mortality by Sex"
)

#Type of Death
TypeDeath_fig = px.bar(
    dfTypeDeath,
    y="Frequency",
    x="Type of Death",
)
TypeDeath_fig.update_layout(
    title="Top Type of Death"
)