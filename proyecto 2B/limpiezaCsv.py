# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 20:22:26 2020

@author: jonat
"""

import pandas as pd

path_iphone =  'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\proyecto 2B\\\proyecto2B\\datosApple.csv'
df5 = pd.read_csv(path_iphone)


df5.loc[df5['RAM'] == '4 GB', 'RAM'] = '4'

df5.loc[df5['RAM'] == '3 GB', 'RAM'] = '3'
df5.loc[df5['RAM'] == '2 GB', 'RAM'] = '2'
df5.loc[df5['RAM'] == '1 GB', 'RAM'] = '1'
df5.loc[df5['RAM'] == '0.512 MB', 'RAM'] = '0.000512'
df5.loc[df5['RAM'] == '0.256 MB', 'RAM'] = '0.000256'

df5.rename(columns={'RAM': 'RAM (GB)'}, inplace=True)


df5.loc[df5['CAMARA FRONTAL'] == 'Oui 12 MP', 'CAMARA FRONTAL'] = '12'
df5.loc[df5['CAMARA FRONTAL'] == 'Oui 7 MP', 'CAMARA FRONTAL'] = '7'
df5.loc[df5['CAMARA FRONTAL'] == 'Oui 1.2MP', 'CAMARA FRONTAL'] = '1.2'
df5.loc[df5['CAMARA FRONTAL'] == 'Oui 2 MP', 'CAMARA FRONTAL'] = '2'
df5.loc[df5['CAMARA FRONTAL'] == 'Oui 1.2 MP', 'CAMARA FRONTAL'] = '1.2'
df5.loc[df5['CAMARA FRONTAL'] == 'Oui 0.3 MP', 'CAMARA FRONTAL'] = '0.3'
df5.loc[df5['CAMARA FRONTAL'] == 'Oui 5 MP', 'CAMARA FRONTAL'] = '5'
df5.loc[df5['CAMARA FRONTAL'] == 'Oui 5MP', 'CAMARA FRONTAL'] = '5'

df5.rename(columns={'CAMARA FRONTAL': 'CAMARA FRONTAL (MP)'}, inplace=True)


df5.loc[df5['PESO'] == '135 g', 'PESO'] = '135'
df5.loc[df5['PESO'] == '174 g', 'PESO'] = '174'
df5.loc[df5['PESO'] == '202 g', 'PESO'] = '202'
df5.loc[df5['PESO'] == '148 g', 'PESO'] = '148'
df5.loc[df5['PESO'] == '177 g', 'PESO'] = '177'
df5.loc[df5['PESO'] == '208 g', 'PESO'] = '208'
df5.loc[df5['PESO'] == '192 g', 'PESO'] = '192'
df5.loc[df5['PESO'] == '143 g', 'PESO'] = '143'

df5.rename(columns={'PESO': 'PESO (g)'}, inplace=True)


df5.loc[df5['BATERIA'] == '1570 mAh', 'BATERIA'] = '1570'

df5.rename(columns={'BATERIA': 'BATERIA (mAh)'}, inplace=True)

df5.loc[df5['MICROSD'] == 'Non', 'MICROSD'] = 'No'
df5.loc[df5['MICROSD'] == 'Non non disponible', 'MICROSD'] = 'No'


df5.loc[df5['TAMAÑO PANTALLA'] == '4 in', 'TAMAÑO PANTALLA'] = '4'
df5.loc[df5['TAMAÑO PANTALLA'] == '4 pouces', 'TAMAÑO PANTALLA'] = '4'

df5.rename(columns={'TAMAÑO PANTALLA': 'TAMAÑO PANTALLA (in)'}, inplace=True)

df5.loc[df5['ROM'] == '16 GB - 32 GB', 'ROM'] = '16, 32'

df5.loc[df5['ROM'] == '16 GB , 64 GB, 128 GB', 'ROM'] = '16, 64, 128'
df5.loc[df5['ROM'] == '16 GB, 64 GB', 'ROM'] = '16, 64'


df5.rename(columns={'ROM': 'ROM (GB)'}, inplace=True)



path_guardado = './datosIphoneF.csv'
df_datos = df5.copy()
df_datos.to_csv(path_guardado, index = False)





def llenar_vacios_vacion(series,tipo):
    
    lista_valores = series.value_counts()
    if(lista_valores.empty == True):
        return series
    
    else:
        if(tipo == 'promedio'):
            suma = 0
            numero_valores = 0    
            for valor_serie in series:        
                if(isinstance(valor_serie,str)):
                    valor = float(valor_serie)
                    numero_valores += 1
                    suma += valor
                else:
                    pass
            promedio = suma/numero_valores
            print(f"promedio :  {promedio}")
            #busca los Nan y pone ese valor
            serie_valores_llenos = series.fillna(promedio)            
        return serie_valores_llenos
    
    
    
def transformar_df(df):
    df_camara = df.groupby('PROCESADOR')
    lista_df = []
    
    for camara,df in df_camara:
        copia = df.copy()
        
        serie_w = copia['CAMARA FRONTAL']

        
        copia.loc[:,'CAMARA FRONTAL'] = llenar_vacios_vacion(serie_w,'promedio')

        
        lista_df.append(copia)
        
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores
    

df6 = transformar_df(df5)
