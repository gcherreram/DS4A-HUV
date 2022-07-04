import pandas as pd
import folium
import json
import plotly.graph_objects as go

def generate_map(df, floor):

    with open('/content/drive/MyDrive/Grupo 237 DS4A/Mapas/Mapas pisos HUV/HUV piso 6.geojson', encoding='utf-8') as json_file:
            areas = json.load(json_file)
for i, each in enumerate(areas["features"]):
            areas["features"][i]['id']=areas["features"][i]['properties']['codigo']

mapa = go.Choroplethmapbox(
            geojson=areas, 
            locations=dfhuvaa.ID, 
            z=dfhuvaa['CASOS'],
            colorscale="Rainbow",
            text=dfhuvaa.NAME,
            marker_opacity=0.9, 
            marker_line_width=0.5,
            colorbar_title = "Piso 6 - Alertas",
            )

annotations = [
        dict(
            showarrow=False,
            align="right",
            text="",
            font=dict(color="#000000"),
            bgcolor="#f9f9f9",
            x=0.95,
            y=0.95,
             )
]
fig = go.Figure(data=mapa)

fig.update_layout(
            geo_scope='south america',
            mapbox_style="carto-positron",
            mapbox_zoom=17, 
            mapbox_center = {"lat": 3.429944590706824, "lon": -76.54480174183846},
            annotations=annotations,
            height=600),

        
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})