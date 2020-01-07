# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:34 2019

@author: jonat
"""

import pandas as pd
import numpy as np
import os
import sqlite3



path_guardado_bin =  'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\art-completo'
df = pd.read_pickle(path_guardado_bin)


serie_artistas_reoetidos = df['artist']

artistas = pd.unique(serie_artistas_reoetidos)

artistas.size
len(artistas)

blake = df['artist'] == 'Blake, William' #obtener solo el artistas blake william
df['artist'].value_counts() # numero de artistas con cuantas obras tiene

df_blake = df[blake] #obtener solo las obras de blake

