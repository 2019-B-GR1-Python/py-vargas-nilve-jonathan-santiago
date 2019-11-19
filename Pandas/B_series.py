# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:38 2019

@author: jonat
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)

np_numeros = np.array((1,2,3,4))

#serie es una estructura de datos mas simples que tiene pandas

#creamos unas series con lo que tenemos
serie_a = pd.Series(lista_numeros) #primera estructura de datos

serie_b = pd.Series(tupla_numeros)

serie_c = pd.Series(np_numeros)

serie_d = pd.Series(
            [True,
             False,
             12,
             12.12,
             "1",
             None,
             (),
             [],
             {"nombre":"Jonathan"}
            ]
        
            )

#acceder alos datos de la serie por medio de indixes
serie_d[3]

lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]

serie_ciudad = pd.Series(lista_ciudades,index = ["A","C","L","Q"])

serie_ciudad["Q"]
serie_ciudad[3]


valores_ciudad = {"ibarra": 9500,"Guayaquil":10000,"Cuenca":8000,"Loja":3000}

#crear con una serie de pandas con un diccionario
serie_valor_ciudad = pd.Series(valores_ciudad)

serie_valor_ciudad['Cuenca']

#ciudades menores a 5000
ciudades_menores_5000 = serie_valor_ciudad < 5000
s5 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad*1.10

serie_valor_ciudad['Loja'] = serie_valor_ciudad['Loja'] - 50


#buscar algun ciudad en la serie
print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)


#elevar al cuadrado con la funcion universal square de numpy
rsquare = np.square(serie_valor_ciudad)
radianes = serie_valor_ciudad * np.pi / 180
rseno = np.sin(radianes)


ciudades_uno = pd.Series({"Montañita":300,
                          "Guayaquil":10000,
                          "Quito":2000
                        }
                        )

ciudades_dos = pd.Series({
                          "Loja":300,
                          "Guayaquil":10000
                    
                        }
                        )
#suma de series. solo suma las que tenga el mismo indixe.
print(ciudades_uno + ciudades_dos)

#para crear un nuevo registro solo se debe dar un indixe y un valor
ciudades_uno["Loja"] = 0

ciudades_dos["Montañita"] = 0
ciudades_dos["Quito"] = 0


#funcion add. es similar a la suma
ciud_add = ciudades_uno.add(ciudades_dos)

#concatenar. se unen las dos series, pero se utiliza el comando verify_integrity = true
ciu_concatenadas = pd.concat([ciudades_uno,ciudades_dos])
ciu_concatenadas_con_vi = pd.concat([ciudades_uno,ciudades_dos], verify_integrity = True)

#funcion append
ciud_append = ciudades_uno.append(ciudades_dos, verify_integrity = True)

#conclusion concat y append son las mismas funciones.

#mayor valor
maximo_valor = ciudades_uno.max()
pd.Series.max(ciudades_uno)
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)
np.max(ciudades_uno)


#Estadisticas
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)
pd.Series.median(ciudades_uno)

#obtener los 2 primeros datos
ciudades_uno.head(2)

#obtener los 2 ultimos datos
ciudades_uno.tail(2)

#ordenamiento
pd.Series.sort_values(ciudades_uno).head(2)
ciudades_uno.sort_values(ascending = False).head(2)
ciudades_uno.sort_values(ascending = False).tail(2)





