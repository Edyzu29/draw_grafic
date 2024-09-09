import pandas as pd
import matplotlib.pyplot as plt
from Stadistics import *
import matplotlib.dates as mdates


# Data
fechas_datos = ['date', 'ID_ESTACION', 'FECHA_DATA', 'HORA_DATA']
parametros_met = ['PBAR', 'PP', 'TEMP', 'HR', 'ws', 'wd']
parametros_caseta = ['TEMP_INT_CASETA', 'HUM_INT_CASETA']
parametros_pm = ['PM10_CONC', 'PM10_FLOW', 'PM25_CONC']
parametros_so2 = ['SO2_CONC', 'SO2_FLOW']
parametros_h2s = ['H2S_CONC', 'H2S_FLOW']
parametros_co = ['CO_CONC', 'CO_FLOW']
parametros_no = ['NO2_CONC', 'NO_CONC', 'NOX_CONC', 'NOX_FLOW']



# Concatenar todas las columnas en una lista
cabecera = fechas_datos + parametros_met + parametros_caseta + parametros_pm + parametros_so2 + parametros_h2s + parametros_co + parametros_no

# Leer el archivo Excel
df = pd.read_excel('paraiso.xlsx')

# Seleccionar solo las columnas especificadas en 'cabecera'
df = df[cabecera]

df['date'] = pd.to_datetime(df['date'])

