import dash 
from dash import html,dcc,Dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import dash_auth
from dash_iconify import DashIconify



application = Dash(__name__, plugins=[dl.plugins.pages],
                external_stylesheets=[dbc.themes.SLATE])
server=application.server
                
# app.layout = html.Div([html.Script(**{"data-url": "https://platform.linkedin.com/badges/js/profile.js"}, type="IN/Share")])

navbar = dbc.NavbarSimple(

    children=[
    
    # html.Link("linkdin",href='https://www.linkedin.com/in/sethu-gopalan-a8915367/'),
    dbc.NavItem(dbc.Button('Linkdin',style={
                'color': 'white', 'fontSize': 16, 'font-family': 'cursive'},href="https://www.linkedin.com/in/sethu-gopalan-a8915367/")),
    dbc.NavItem(dbc.Button('Github',style={
                'color': 'white', 'fontSize': 16, 'font-family': 'cursive'},href="https://github.com/SethuGopalan?tab=repositories")),
    
    
    
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page['name'], href=page["path"])
            for page in dash.page_registry.values()
            if page['module'] != "page .not_found_404"
        ],
        nav=True,
        label="Look for my projects",
    
    ),
    ],
   
    brand="SG",
    brand_style= {'color': 'white', 'fontSize': 20, 'font-family': 'Serif',"border": "0.5px white double","border-radius":"5px","background-image": "linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1))" },
    
    
    color="primary",
    dark=True,
    # links_left=True,
    className="mb-3"
  
    

)


application.layout = dbc.Container(

    [navbar, dl.plugins.page_container],
    fluid=True,
)
if __name__ == "__main__":
    application.run(debug=True,port=8000)