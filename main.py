import pandas as pd
import matplotlib.pyplot as plt
from functions import *
import matplotlib.dates as mdates

# Data
fechas_datos = ['date', 'ID_ESTACION', 'FECHA_DATA', 'HORA_DATA']
parametros_met = ['TEMP', 'HR']
parametros_caseta = ['TEMP_INT_CASETA', 'HUM_INT_CASETA']

# Concatenar todas las columnas en una lista
cabecera = fechas_datos + parametros_met + parametros_caseta

# Leer el archivo Excel
df = pd.read_excel('paraiso.xlsx')

# Seleccionar solo las columnas especificadas en 'cabecera'
df = df[cabecera]

df['date'] = pd.to_datetime(df['date'])

df_filtrado = tukey_2visagra(df, 'TEMP_INT_CASETA')

# Graficar TEMP_INT_CASETA contra las fechas
plt.figure(figsize=(20, 6))  # Tamaño de la figura
plt.plot(df_filtrado['date'], df_filtrado['TEMP_INT_CASETA'])

plt.axhline(y=20, color='r', linestyle='--', label='Límite Inferior (20°C)')
plt.axhline(y=30, color='b', linestyle='--', label='Límite Superior (30°C)')

plt.xlim(df['date'].min(), df['date'].max())

# Añadir etiquetas y título
plt.xlabel('Fecha')
plt.ylabel('Temperatura Interna Caseta (°C)')
plt.title('Temperatura Interna de la Caseta a lo Largo del Tiempo')

# Formatear el eje X para mostrar cada 15 días
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=8))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y'))

# Añadir leyenda
plt.legend()

# Añadir la cuadrícula
plt.grid(True)

# Mostrar el gráfico
plt.tight_layout()  # Ajustar el gráfico para que no se solapen los elementos
plt.show()