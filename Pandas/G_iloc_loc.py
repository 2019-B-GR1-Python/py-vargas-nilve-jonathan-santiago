# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:26 2019

@author: jonat
"""


import pandas as pd
import numpy as np
import os
import sqlite3



path_guardado_bin =  'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\art-completo'
df = pd.read_pickle(path_guardado_bin)


## funcion loc

 primero = df.loc[1035,'artist']
 
  primero = df.loc[1035] # nos devuelve una serie, pero no devuelve la serie del index correcto
  
  primero_loc = df.loc[0]
  
  primero_iloc = df.iloc[0]
  
  
# nuevo dataframe con id como index
df2 = df.set_index('id')

primero_loc_df2 = df2.loc[1035]
primero_iloc_df2 = df2.iloc[1035]



diccionario_ninos = {
        "nota 1 ":{
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}
                }
        



df3 = pd.DataFrame(diccionario_ninos)

df3.loc['Pepito'] # se filtra con los labels de los indexes
df3.iloc['Pepito'] # solamente se filtra con indexes


df3.loc["Pepito","disciplina"] # devuelve la disciplina de pepito

df3.loc["Pepito",["disciplina","nota 1 "]]
  

df3.loc[["Pepito","Juanita"],["nota 1 "]]  


df3.loc[["Pepito","Juanita"],["nota 1 ","disciplina"]]


df3.loc[[True,False,True]]

condicion = df3["nota 1 "] > 7
condicion_dis =  df3["disciplina"] > 7

mayores_siete = df3.loc[condicion] ##notas mayores a siete
mayores_siete[condicion_dis] ## notas y disciplina mayor a 7




# solo a pepito 10 en notas y disciplina

df3.loc['Pepito'] = 10

# estudiantes menores a 7 wn disciplina si=uben a 7

condicion_menores_siete = df3["disciplina"] < 7
df3.loc[condicion_menores_siete,"disciplina"] = 7


# disciplina se les baje a 7

df3.loc[:,"disciplina"] = 7 

#aniadir la columna promedio nota 1 y disciplina

promedio = df3['nota 1 ']+df3['disciplina']/2  
df3['promedio'] = promedio





  
