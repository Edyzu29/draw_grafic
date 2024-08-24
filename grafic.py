import pandas as pd
import matplotlib.pyplot as plt
from functions import *
import matplotlib.dates as mdates
import plotly.express as px

# Data
fechas_datos = ['date', 'ID_ESTACION', 'FECHA_DATA', 'HORA_DATA']
parametros_met = ['PBAR', 'PP', 'TEMP', 'HR', 'ws', 'wd']
parametros_caseta = ['TEMP_INT_CASETA', 'HUM_INT_CASETA']
parametros_pm = ['PM10_CONC', 'PM10_FLOW', 'PM25_CONC']
parametros_so2 = ['SO2_CONC', 'SO2_FLOW']
parametros_h2s = ['H2S_CONC', 'H2S_FLOW']
parametros_co = ['CO_CONC', 'CO_FLOW']
parametros_no = ['NO2_CONC', 'NO_CONC', 'NOX_CONC', 'NOX_FLOW']

rename_colum = {
    'PBAR': "Presion Atmosferica (mmhg)", 
    'PP': "Precipitacion",
    'TEMP' : "Temperatura Ambiental (°C)",
    'HR': "Humedad Relativa (%)",
    'ws': "Velocidad del Viento (ms)",
    'wd': "Direccion de Viento",
    'TEMP_INT_CASETA': "Temperatura Interna (°C)",
    'HUM_INT_CASETA': "Humedad Interna (%)",
    'PM10_CONC': "Concentración PM10 (μg/m³)",
    'PM10_FLOW': "Flujo GRIMM (L/min)",
    'PM25_CONC': "Concentración PM2.5 (μg/m³)",
    'SO2_CONC': "Concentración SO2 (μg/m³)", 
    'SO2_FLOW': "Flujo SO2 (L/min)",
    'H2S_CONC': "Concentración H2S (μg/m³)",
    'H2S_FLOW': "Flujo H2S (L/min)",
    'CO_CONC': "Concentración CO (μg/m³)",
    'CO_FLOW': "Flujo H2S (L/min)",
    'NO2_CONC': "Concentración NO2 (μg/m³)", 
    'NO_CONC': "Concentración NO (μg/m³)", 
    'NOX_CONC': "Concentración NOX (μg/m³)",
    'NOX_FLOW' :     "Flujo H2S (L/min)"
}

Estaciones = {
    "41" : "Huachipa - Paraiso",
    "42" : "Huachipa - Nievería",
    "40" : "Huachipa - Santa María"
    }

# Concatenar todas las columnas en una lista
cabecera = fechas_datos + parametros_met + parametros_caseta + parametros_pm + parametros_so2 + parametros_h2s + parametros_co + parametros_no

# Leer el archivo Excel
df = pd.read_excel('paraiso.xlsx')

# Seleccionar solo las columnas especificadas en 'cabecera'
df = df[cabecera]

df['date'] = pd.to_datetime(df['date'])

df_filtrado = tukey_2visagra(df, 'TEMP_INT_CASETA')

#PLOT
def ploteando(data, x_axis, y_axis, lit_min, lit_max):
    figu = px.line(data, 
                      x=x_axis, 
                      y=y_axis, 
                      labels= {x_axis: "Fecha", y_axis : rename_colum[y_axis]},
                      )


    figu.add_shape(
        type="line",
        x0=data["date"].min(),  # Fecha inicial
        x1=data["date"].max(),  # Fecha final
        y0=lit_min,  # Valor en Y donde comienza la línea
        y1=lit_min,  # Valor en Y donde termina la línea
        line=dict(color="blue", width=2, dash="dash")  # Personaliza el color, grosor y estilo de la línea
    )
    figu.add_shape(
        type="line",
        x0=data["date"].min(),  # Fecha inicial
        x1=data["date"].max(),  # Fecha final
        y0=lit_max,  # Valor en Y donde comienza la línea
        y1=lit_max,  # Valor en Y donde termina la línea
        line=dict(color="red", width=2, dash="dash")  # Personaliza el color, grosor y estilo de la línea
    )
    return figu


