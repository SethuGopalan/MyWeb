from numpy import equal, isin
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from dash import Dash, html, dcc, callback
import dash
from dash import Input, Output, dash_table,State
import numpy as np
import pandas as pd

import requests
import time
import datetime
# import pdfkit

import dash_bootstrap_components as dbc

from dash_iconify import DashIconify

from dash_labs.plugins.pages import register_page

# data section

register_page(__name__)

layout=dbc.Container([

    dbc.Row([
    
    dbc.Col([
    
    html.Div([
    
    html.P("My Articles",style={'textAlign': 'middle','fontSize': 28,'font-family': 'cursive'}),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Card(
    [
        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H6("Host Web Appilication on AWS  ElasticBeanstack with dash and Python Part1", style={"color":"green",'fontSize': 28,'font-family': 'cursive'},className="card-title"),
                html.P(
                    "If you are a developer, wish to make a portfolio website," 
                    "or want to share your knowledge with the world what is the easy and cost effective way? The Answer which I found is Python, dash, and Aws, Walk you through Step By Step",
                    className="card-text",
                    style={"color":"yellow",'fontSize': 16,'font-family': 'cursive'}
                ),
                dbc.Button("Open Article", id="open", n_clicks=0),
                dbc.Modal(
      
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Host a Web Appilication on" 
                                                       " AWS ElasticBeanstack with dash and Python Part1",style={"color":"gray",'fontSize': 28,'font-family': 'cursive'})),
                        dbc.ModalBody(html.Iframe(src='assets/Articles/How to diploy a web application with dash aws python.pdf',style={'width':2080,'height':4000})),
                        dbc.ModalFooter([
                            html.H6("Sethu Gopalan / "),html.Br(),
                            html.H6("Date : March 30 2023"),
      
                            dbc.Button(
                                "Close", id="close", className="ms-auto", n_clicks=0
                            )
                    ]),
                    ],
                    id="pdf_modal",
                    keyboard=False,
                    fullscreen=True,
                    scrollable=True,
                    is_open=False,
                    size="lg",
                    # centered=True,
                    
                    backdrop="static"
                ),
                # html.Iframe(src='assets\Articles\How to diploy a web application with dash aws python.pdf'),
                
                # pdfkit.from_url("assets\Articles\How to diploy a web application with dash aws python.pdf",'out.pdf')
                # (html.ObjectEl(data='assets\Articles\How to diploy a web application with dash aws python.pdf',type='application/pdf'),
                
            # # To my recollection you need to put your static files in the 'assets' folder
            # html.Article("assets/Articles/How to diploy a web application with dash aws python.pdf",type="application/pdf"),
                    
            #         # style={"width": "800px", "height": "600px"}
            #     ),
        
                # dbc.Button(href="assets\Articles\How to diploy a web application with dash aws python.pdf", color="primary"),
            ]
        ),
    ],
    style={"width": "36rem"},
)
    
    ])
    
    ])
    ])
])

@callback(
    Output("pdf_modal", "is_open"),
    [Input("open", "n_clicks"),
    Input("close", "n_clicks")],
    [State("pdf_modal", "is_open")],

)

def toggle_modal(n1, n2, is_open):
        # sourcery skip: assign-if-exp, reintroduce-else
        if n1 or n2:

            return not is_open
        return is_open