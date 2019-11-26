# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:12 2019

@author: jonat
"""

import numpy as np
import pandas as pd


arr_pand = np.random.randint(0,10,6).reshape(2,3)

#instanciar un nuevo arreglo
#dataframe es un conjunto de series.

df1 = pd.DataFrame(arr_pand)
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

s1[0]

#guardar una serie en una nueva columna

lista_numeros = [20,30]
serie_nueva = pd.Series(lista_numeros)

df1[3] = serie_nueva

df1[4] = s1 * s2

datos_fisicos =pd.DataFrame(arr_pand, columns = ['Estructura (cm)','Peso (Kg)', 'edad (anios)'],index = ['Jona', 'Santia' ])

#cambiar nombre del indixe.
df1.index = ['Santiago','Santia']

#cambiar columnas
df1.columns = ['A','B','C','D','E']





