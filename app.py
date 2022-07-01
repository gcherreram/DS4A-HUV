#Import Libraries
import dash
from dash import html
import dash_labs as dl
import dash_bootstrap_components as dbc

#from callbacks import register_callbacks

#Images
HUV_logoI = "https://huv.gov.co/wp-content/uploads/2020/06/logo-HU_Horizontal_Blanco.png"


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
                dbc.Col(dbc.NavItem(html.Img(src=HUV_logoI, height="50px"))),
            ]
        )
    ],
    brand="Dashboard para el monitoreo de IAAS ",
    brand_href="#",
    color="primary",
    dark=True,
    class_name="mb-2"
)

#Main layout
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
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
    app.run_server(debug=True)
