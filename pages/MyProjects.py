from numpy import equal, isin
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from dash import Dash, html, dcc, callback
import dash
from dash import Input, Output, dash_table
import numpy as np
import pandas as pd

import requests
import time
import datetime

import dash_bootstrap_components as dbc

from dash_iconify import DashIconify

from dash_labs.plugins.pages import register_page

# data section
register_page(__name__)
application=Dash(__name__,meta_tags=[{'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])



layout=dbc.Container([

    dbc.Row([
    dbc.Col([
    
    html.Br(),
    html.Br(),
    html.Br(),
    
    DashIconify(icon="fa-solid:shield-alt"  ,style={
                'color': 'yellow', 'fontSize': 38,'display':'inline-block',"margin-right": "16px"}),html.H2("What I have made",style={'display':'inline-block',"padding": "5px","margin-left": "15px"})
    ],width={'size': 4, 'offset': 0})
     
    ],justify="left"),

    dbc.Row([
    
    dbc.Col([
     
    html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    # html.Br(),
    
    
    html.H4("Covid Data Vuialization with Live data with dash plotly and python",style={'textAlign': 'left','fontSize': 18,"margin-left": "24px",'font-family': 'cursive'}),
    
    
    dbc.Button("find this code here",outline=True,style={
                'color': 'yellow', 'fontSize': 16,'font-family': 'cursive',"margin-left": "30px"},href="https://github.com/SethuGopalan/covid_multi_page_app")
    ]),
    
    

    ],width={'size': 4, 'offset': 0}),



    dbc.Col([
    html.Br(),
    html.Div([
    
    dbc.Carousel(
    
        items=[
            {"key": "1", "src": "/assets/Project1/Pic1.png"},
            {"key": "2", "src": "/assets/Project1/Pic2.png"},
            {"key": "3", "src": "/assets/Project1/Pic3.png"},
            {"key": "4", "src": "/assets/Project1/Pic4.png"},
            {"key": "5", "src": "/assets/Project1/Pic5.png"},
            {"key": "6", "src": "/assets/Project1/Pic6.png"},
            {"key": "7", "src": "/assets/Project1/Pic7.png"},
            {"key": "8", "src": "/assets/Project1/Pic8.png"},
            {"key": "9", "src": "/assets/Project1/Pic9.png"},
            {"key": "10", "src": "/assets/Project1/Pic10.png"},
            {"key": "11", "src": "/assets/Project1/Pic11.png"},
            {"key": "12", "src": "/assets/Project1/Pic12.png"},
        ],
        controls=False,
        indicators=False,
        interval=2000,
        ride="carousel",
        style={'width': 600,'border': '2px solid yellow'},
        ),
    ])
    
    ],width={'size': 3, 'offset': 2})
    

    ]),

    dbc.Row([
    
    dbc.Col([
     
    html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    # html.Br(),
    
    
    html.H4("ChatBot application with dash and python  ",style={'textAlign': 'left','fontSize': 18,"margin-left": "24px",'font-family': 'cursive'}),
    
    
    dbc.Button("find this code here",outline=True,style={
                'color': 'yellow', 'fontSize': 16,'font-family': 'cursive',"margin-left": "30px"},href="https://github.com/SethuGopalan/covid_multi_page_app")
    ]),
    
    

    ],width={'size': 4, 'offset': 0}),



    dbc.Col([
    html.Br(),
    html.Div([
    
    dbc.Carousel(
    
        items=[
            {"key": "1", "src": "/assets/Project2/Pic1.png"},
            {"key": "2", "src": "/assets/Project2/Pic2.png"},
            {"key": "3", "src": "/assets/Project2/Pic3.png"},
            
        ],
        controls=False,
        indicators=False,
        interval=2000,
        ride="carousel",
        style={'width': 600,'border': '2px solid yellow'},
        ),
    ])
    
    ],width={'size': 3, 'offset': 2})
    

    ])
     
    
    
    ])

