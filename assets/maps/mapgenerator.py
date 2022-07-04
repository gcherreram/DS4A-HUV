import pandas as pd
import folium
import json
import plotly.graph_objects as go

def generate_map(df, floor):
    if floor == "first":
        map_file = "data/geojson/HUV piso 1.geojson"
        map_title = "Piso 1 - Alertas"
    elif floor == "second":
        map_file = "data/geojson/HUV piso 2.geojson"
        map_title = "Piso 2 - Alertas"
    elif floor == "third":
        map_file = "data/geojson/HUV piso 3.geojson"
        map_title = "Piso 3 - Alertas"
    elif floor == "fourth":
        map_file = "data/geojson/HUV piso 4.geojson"
        map_title = "Piso 4 - Alertas"
    elif floor == "fifth":
        map_file = "data/geojson/HUV piso 5.geojson"
        map_title = "Piso 5 - Alertas"
    else:
        map_file = "data/geojson/HUV piso 6.geojson"
        map_title = "Piso 6 - Alertas"
    
    with open(map_file, encoding='utf-8') as json_file:
            areas = json.load(json_file)
    for i, each in enumerate(areas["features"]):
            areas["features"][i]['id']=areas["features"][i]['properties']['codigo']
    
    mapa = go.Choroplethmapbox(
            geojson=areas, 
            locations=df.ID, 
            z=df['CASOS'],
            colorscale="Rainbow",
            text=df.NAME,
            marker_opacity=0.9, 
            marker_line_width=0.5,
            colorbar_title = map_title,
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

    return fig