# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:04:08 2020

@author: shiva
"""


from application import app
import config



app.run_server(debug=config.debug, host=config.host, port=config.port)