# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 00:46:44 2020

@author: shiva
"""


import os



## App settings
name = "COVID-Forecaster"

host = "127.0.0.1"

port = int(os.environ.get("PORT", 8000))

debug = False

contacts = "https://www.linkedin.com/in/shivali-gakhar-35b222172/"

code = "https://github.com/shivaligakhar-123/COVID-FORECATOR"


fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'



## File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"
