# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:41 2019

@author: jonat
"""

import pandas as pd
import numpy as np
import os
import sqlite3



path_guardado_bin =  'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\art-completo'
df5 = pd.read_pickle(path_guardado_bin)

df = df5.iloc[49800:50019,:].copy()#copiar cierta seccion del dataframe


# Tipos archivos
# JSON
# EXCEL
# SQL

path_guardado = 'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\mi_df_completo.xlsx'

df.to_excel(path_guardado, index = False)

columas = ['artist','title','year']
df.to_excel(path_guardado,columns = columas)


### Multiples hojas de trabajo ###
path_multiple = 'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\mi_df_multiples.xlsx'
writer = pd.ExcelWriter(path_multiple,engine = 'xlsxwriter')
#motor importante xlsxwriter
df.to_excel(writer,sheet_name = 'Primera')
df.to_excel(writer,sheet_name = 'Segunda',index = False)
df.to_excel(writer,sheet_name = 'Tercera', columns = columas)
writer.save()


#obtener el numero de registros de cierta columna
#Numero de artistas
num_artist = df['artist'].value_counts()

path_colores = 'C:\\Users\\jonat\\Documents\\GitHub\\py-vargas-nilve-jonathan-santiago\\Pandas\\data\\mi_df_colores.xlsx'
writer = pd.ExcelWriter(path_colores,engine = 'xlsxwriter')

#sheet_name : nombre de la hoja
num_artist.to_excel(writer,sheet_name = 'Artistas')

#tenemos la hoja de los artistas
hoja_de_artistas = writer.sheets['Artistas']


formato_artistas = {'type':'2_color_scale',
                    'min_value':'10',
                    'min_type':'percentile',
                    'max_value':'',
                    'max_type':'percentile'}

rango_celdas = 'B2:B{}'.format(len(num_artist.index) + 1) #meter una variable en un string

#crear formato en sii
hoja_de_artistas.conditional_format(rango_celdas,formato_artistas)
writer.save()




import xlsxwriter
workbook = xlsxwriter.Workbook(path_colores)
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = num_artist.values
worksheet.write_column('A1', data)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

# Insert the chart into the worksheet.
worksheet.insert_chart('C1', chart)

workbook.close()



################################ --> SQL #################################################################







with sqlite3.connect('bdd_artist1.db') as conexion: df5.to_sql('py_artistas1',conexion) #nombre de la tabla



#### JSON ##########

df5.to_json('artistas.json')

df5.to_json('artistas_tabla.json',orient='table')


























