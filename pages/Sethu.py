from numpy import equal, isin
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import dash
from dash import Dash, html, dcc, callback,dash_table


import numpy as np
import pandas as pd

import requests
import time
import datetime

import dash_bootstrap_components as dbc

from dash_iconify import DashIconify

from dash_labs.plugins.pages import register_page
My_list=["Python","Dash","Pandas","Numpy","Flask","Reactjs"]
Tech_List=["AWS","Azure","SQL","Selenium","shell script"]




# data section
register_page(__name__, path="/")




layout=dbc.Container([

    dbc.Row([
    dbc.Col([
    html.Br(),

    
   
    
    html.Div([
    
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.P("Hi, my  name  is ",style={
                'color': 'yellow', 'fontSize': 20, 'font-family': 'var(--font-mono)'}),
    html.H1("Sethu Gopalan.",style={
                'color': 'gray', 'fontSize': 62, 'font-family': 'Sans-serif'}),
    html.H1("I build web application with data visualization.",style={
                'color': 'gray', 'fontSize': 52, 'font-family': 'Sans-serif'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P("I am a software engineer specializing in building web application on data visualization",style={
                 'fontSize': 16, 'font-family': 'cursive',} ),
    html.P("with python ,dash and plotly."
            " Currently, I’m focused on building application with AI and ML ",style={
                 'fontSize': 16, 'font-family': 'cursive'} ),
    
    
    ])
    ],width={'size': 12, 'offset': 0}),

    
    ]),
    
    # header finish------------------------------------------------------------------------------------------------------------------------------------------------------------->
    
    dbc.Row([
    dbc.Col([
    html.Div([
    html.Br(),       
    DashIconify(icon="fa-solid:shield-alt"  ,style={
                'color': 'yellow', 'fontSize': 38,'display':'inline-block',"margin-right": "16px"}),html.H2("About me .",style={'display':'inline-block',"padding": "5px","margin-left": "5px"})
                   
     
    ])
    ], width={'size': 6, 'offset': 0}),dbc.Col([
    html.Br(),
    html.Div([
    
    html.P("Hello! My name is Sethu, and I enjoy working with technology and creating things related to technology software and data."
           'My interest in technology started with making computers, Building servers, databases and networks, cloud services.'
            "For the last few years, I have been working on creating a web application with python, statistics, and data.",style={
                 'fontSize': 16, 'font-family': 'cursive',} ),

    
    html.P("Here are a few technologies I’ve been working with recently:"),
    
    html.Ul([html.Li(x) for x in My_list],style={'display':'inline-block',"margin-right": "200px"}),
    html.Ul([html.Li(x) for x in Tech_List],style={'display':'inline-block'}),
    
    

    ]),

   
    ],width={'size': 7, 'offset': 0}),
   
    dbc.Col([html.Div([dbc.CardImg(src="assets\mypic.jpeg",style={"width": "18rem",'border': '5px solid yellow',"border-radius": "50%" },)])],width={'size': 2, 'offset': 0}),
    
    
    
    ]),

     html.Br(),

    dbc.Row([
    
    
    dbc.Col([html.Div([dbc.Button("Check my projects in Git",size="elg",outline=True,style={
                'color': 'gray', 'fontSize': 20, 'font-family': 'Serif','border': '2px solid yellow',"margin-left": "15px"},href="https://github.com/SethuGopalan?tab=repositories")]),],width={'size': 3, 'offset': 0}),
   
   
    ])
    
   
      
                
    
    

])
