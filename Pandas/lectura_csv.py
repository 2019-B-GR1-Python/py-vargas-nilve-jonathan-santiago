# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:37 2019

@author: jonat
"""

import pandas as pd
import os

# 1) JSON, CSV, HTML, XML...... Primer grupo de archivos que se pueden leer con pandas
# 2) Binary files -> (!#mf-.1234'120')
# 3)    Relational datbases


path = 'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\art.csv'
df1 = pd.read_csv(path, nrows = 10)


#agregar columnas que solo necesitemos

columnas = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height','width','units']

df2 = pd.read_csv(path,nrows = 10, usecols = columnas, index_col = 'id')


#guardar los dateframes que ya fueron trabajados, realizados
df3 = pd.read_csv(path, nrows = 10)

path_guardado =  'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\art-df3'
df3.to_pickle(path_guardado)

#------------------
df4 = pd.read_csv(path)
path_guardado_bin =  'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\art-completo'
df4.to_pickle(path_guardado_bin)


#leer el pico guardado
df5 = pd.read_pickle(path_guardado)





