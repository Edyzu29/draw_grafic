import pandas as pd
import numpy as np
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

import plotly.graph_objects as go

flujos = [x for x in rename_colum.keys() if "FLOW" in x]

def flugenado(data = pd.DataFrame, end_date = str(), start_date = str()):
    data_filtered = data[(data['date'] >= str('2024-08-14')) & (data['date'] <= str('2024-08-15'))]
    
    flow_table = {
        "equipments": [],
        "flow_min": [],
        "flow_max": [],
    }
    
    flow_table_columns = list(flow_table.keys())
    
    for equiptment in data_filtered.columns: 
        if "FLOW" in equiptment:
            flow_table["equipments"].append(equiptment)
            flow_table["flow_min"].append(float(data_filtered[equiptment].min()))
            flow_table["flow_max"].append(float(data_filtered[equiptment].max()))
    
    lines = []
    for i in range(len(flow_table["equipments"])):
        lines.append(go.Scatter(
            x=[flow_table["flow_min"][i], flow_table["flow_max"][i]],
            y=[flow_table["equipments"][i], flow_table["equipments"][i]],
            mode="lines",
            line=dict(color="grey"),
            showlegend=False
        ))
    
    fig = go.Figure(
        data=lines + [
            # Lineas que conectan los valores mínimo y máximo (dumbbell)
            # Puntos para los valores mínimos
            go.Scatter(
                x=flow_table["flow_min"],
                y=flow_table["equipments"],
                mode="markers",
                name="Min Flow",
                marker=dict(color="red", size=10),
            ),
            # Puntos para los valores máximos
            go.Scatter(
                x=flow_table["flow_max"],
                y=flow_table["equipments"],
                mode="markers",
                name="Max Flow",
                marker=dict(color="blue", size=10),
            ),
        ]
    )
    
     # Crear valores intermedios entre flow_min y flow_max
    all_ticks = []
    for min_val, max_val in zip(flow_table["flow_min"], flow_table["flow_max"]):
        if min_val != max_val:
            intermediate_ticks = np.linspace(min_val, max_val, num=20)  # Genera 5 valores, incluyendo min y max
            all_ticks.extend(intermediate_ticks)
        else:
            all_ticks.append(min_val)
            
    unique_ticks = sorted(set(all_ticks))
    tick_spacing = (max(unique_ticks) - min(unique_ticks)) /10
    
    tick_texts = [f"{tick:1f}" for tick in unique_ticks]

    # Ajustar el layout para eliminar espacio vacío
    fig.update_layout(
        title="Flujos de Equipos (Dumbbell Plot)",
        height=600,
        xaxis_title="Flujo",
        yaxis_title="Equipos",
        legend_title="Valores",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=50, r=50, t=50, b=50),
    )
    
    # Definir los valores de ticks en el eje x con valores intermedios
    fig.update_xaxes(
        #tickvals=unique_ticks,  # Set tick values manually
        ticktext=tick_texts,  # Corresponding text for ticks
        dtick=tick_spacing,  # Space between ticks
        range=[min(flow_table["flow_min"]) - 0.05, max(flow_table["flow_max"]) + 0.05],  # Añadir margen para espacio
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    )
    
    fig.update_yaxes(
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    )
    
    fig.show()
    
flugenado(df_filtrado)