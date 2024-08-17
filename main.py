import pandas as pd
import matplotlib.pyplot as plt

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

# Verificar la selección de columnas
print(df.head())

df['date'] = pd.to_datetime(df['date'])

# Graficar TEMP_INT_CASETA contra las fechas
plt.figure(figsize=(10, 6))  # Tamaño de la figura
plt.plot(df['date'], df['TEMP_INT_CASETA'], marker='o')

# Añadir etiquetas y título
plt.xlabel('Fecha')
plt.ylabel('Temperatura Interna Caseta (°C)')
plt.title('Temperatura Interna de la Caseta a lo Largo del Tiempo')

# Rotar las etiquetas de fecha en el eje X para mejor legibilidad
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()  # Ajustar el gráfico para que no se solapen los elementos
plt.show()
