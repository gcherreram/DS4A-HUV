#Import Libraries
import dash
from dash import html
import dash_labs as dl
import dash_bootstrap_components as dbc
import pandas as pd

#Own functions
from components.cards.infocard import infocard

#Create App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO], plugins=[dl.plugins.pages],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

app.config.suppress_callback_exceptions=True

app.title = "Dashboard para el monitoreo de IAAS en el HUV"

# Create Navigation bar
navbar = dbc.NavbarSimple(
    children = [
        dbc.Row(
            [
                dbc.Col(dbc.DropdownMenu
                    (
                        children=[
                            dbc.DropdownMenuItem(page["name"], href=page["path"])
                            for page in dash.page_registry.values()
                            if page["module"] != "pages.not_found_404"],
                        nav=True,
                        in_navbar=True,
                        label="Menu",          
                    )
                ),
                dbc.Col(dbc.NavItem(html.Img(src="assets/images/HospitalLogoHorizontal.png", height="50px"))),
            ]
        )
    ],
    brand="Dashboard para el monitoreo de IAAS en el HUV",
    brand_href="#",
    color="primary",
    dark=True,
    class_name="mb-2"
)

#Branding row
info_card = infocard("@DS4A Colombia\n Cohort 6\n Team 237", "assets/images/DS4Alogo.png")

#Main layout
app.layout = dbc.Container(
    [
        dbc.Row(navbar),
        dbc.Row(dl.plugins.page_container),
        dbc.Row(info_card, justify="between")
    ],
    class_name="dbc",
    fluid=True,
)


# Call to external function to register all callbacks
#register_callbacks(app)

# This call will be used with Gunicorn server
server = app.server

# Testing server
if __name__ == "__main__":
    app.run_server(debug=True, port=8050, host="0.0.0.0")
