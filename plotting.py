import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px
from labels import *
from data_tratement import *
from Stadistics import *

def plot_scatter(data, x_axis, y_axis, lit_min = 0, lit_max = 0,  Eca = 0,switch_limit_manual = True):
    figu = px.line(data, 
                      x=x_axis, 
                      y=y_axis, 
                      labels= {x_axis: "Fecha", y_axis : rename_colum[y_axis]},
                      )
    
    if switch_limit_manual:
        min_val = lit_min
        min_name = "Limit Inferior"
        
        max_val = lit_max
        max_name = "Limit Superior"
        
    else:
        min_val, max_val = Limite_inf_sup(df, y_axis)
        min_name = "Limit Inferior Historico"
        max_name = "Limit Superior Historico"
        
    if Eca != 0:
        figu.add_shape(
        type="line",
        x0=data["date"].min(),  # Fecha inicial
        x1=data["date"].max(),  # Fecha final
        y0=Eca,  # Valor en Y donde comienza la línea
        y1=Eca,  # Valor en Y donde termina la línea
        line=dict(color="green", width=2, dash="dash"),  # Personaliza el color, grosor y estilo de la línea
        )
    
    figu.add_trace(
    go.Scatter(
        x=[data["date"].min(), data["date"].max()],  # Define los puntos inicial y final en X
        y=[max_val, max_val],  # Define los puntos inicial y final en Y
        mode="lines",  # Modo de la traza, solo líneas
        name=max_name,  # Nombre que aparecerá en la leyenda
        line=dict(color="red", width=2, dash="dash")  # Personaliza la línea
    ))
    
    figu.add_trace(
    go.Scatter(
        x=[data["date"].min(), data["date"].max()],  # Define los puntos inicial y final en X
        y=[min_val, min_val],  # Define los puntos inicial y final en Y
        mode="lines",  # Modo de la traza, solo líneas
        name=min_name,  # Nombre que aparecerá en la leyenda
        line=dict(color="blue", width=2, dash="dash")  # Personaliza la línea
    ))
    
    figu.update_layout(
    legend=dict(
        x=1,       # Mueve la leyenda ligeramente fuera del gráfico a la derecha
        y=1,          # Posición Y de la leyenda (1 es parte superior)
        xanchor='right',  # Ancla de la leyenda para la posición X
        yanchor='top',
        bgcolor="rgba(255, 255, 255, 0.7)",  # Fondo blanco semi-transparente para la leyenda
        bordercolor="black",  # Color del borde del marco de la leyenda
        borderwidth=2 ,        # Grosor del borde del marco# Ancla de la leyenda para la posición Y
        orientation='v'  # Orientación vertical de la leyenda
      ) 
    )

    
    return figu

def plot_simple_flow(data: pd.DataFrame):

    flow_equitments = [x for x in data.columns if "FLOW" in x]

    fig = make_subplots(
        rows=len(flow_equitments), 
        cols=1, 
        vertical_spacing=0.075
    )

    for i, equiptment in enumerate(flow_equitments, start=1):
        fig.add_trace(
            go.Scatter(
                
                x= data['date'],
                y= data[equiptment],
                mode="lines",
                showlegend=False
            ) ,
            row=i, 
            col=1
        )
        fig.update_yaxes(
            title_text=f"{rename_colum[equiptment]}", 
            title_standoff=20,  # Ajusta la distancia del título al eje
            tickangle=0,  # Mantiene el título en horizontal
            row=i,
            col=1,
            )


    fig.update_layout(
        height=130 * len(flow_equitments),  # Altura proporcional a la cantidad de equipos
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=0, r=0, t=0, b=0),
        
    )

    # Ajustar el estilo del eje Y para todos los subplots
    fig.update_yaxes(
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    )

    return fig
  
def plot_meteorologica(data: pd.DataFrame):
    
    fig = make_subplots(
        rows=len(parametros_met), 
        cols=1, 
        vertical_spacing=0.075
    )
    
    for i, data_sensor in enumerate(parametros_met, start=1):
        fig.add_trace(
            go.Scatter(
                
                x= data['date'],
                y= data[data_sensor],
                mode="lines",
                showlegend=False
            ) ,
            row=i, 
            col=1
        )
        fig.update_yaxes(
             title_text=f"{rename_colum[data_sensor].replace(' ', '<br>')}",  # Inserta un salto de línea en lugar de espacios
            title_standoff=20,  # Ajusta la distancia del título al eje
            tickangle=0,  # Mantiene el título en horizontal
            row=i,
            col=1,
            )
    
    fig.update_layout(
        height=130 * len(parametros_met),  # Altura proporcional a la cantidad de equipos
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=0, r=0, t=0, b=0),
        
    )

    # Ajustar el estilo del eje Y para todos los subplots
    fig.update_yaxes(
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    )

    return fig

def plot_dumbbell_flow(data: pd.DataFrame):
    
    flow_table = {
        "equipments": [],
        "flow_min": [],
        "flow_max": [],
        "last_value": [],
    }
    
    for equiptment in data.columns: 
        if "FLOW" in equiptment:
            data[equiptment] = data[equiptment].fillna(0)
            flow_table["equipments"].append(rename_colum[equiptment])
            flow_table["flow_min"].append(float(data[equiptment].min()))
            flow_table["flow_max"].append(float(data[equiptment].max()))
            flow_table["last_value"].append(float(data[equiptment].iloc[-1]))
    
    # Crear subplots; las filas se basan en la cantidad de equipos
    fig = make_subplots(
        rows=len(flow_table["equipments"]), 
        cols=1, 
        shared_xaxes=False,  # No compartir eje X entre subplots
        vertical_spacing=0.075
    )
    
    for i in range(len(flow_table["equipments"])):
        equipment = flow_table["equipments"][i]
        min_flow = flow_table["flow_min"][i]
        max_flow = flow_table["flow_max"][i]
        last_value = flow_table["last_value"][i]
        
        fig.add_trace(
            go.Scatter(
                x=[min_flow, max_flow],
                y=[equipment, equipment],
                mode="lines",
                line=dict(color="grey"),
                showlegend=False,
            ),
            row=i+1, col=1
        )

        fig.add_trace(
            go.Scatter(
                x=[min_flow],
                y=[equipment],
                mode="markers",
                name="Min Flujo",
                marker=dict(color="red", size=10),
                showlegend=(i == 0),  # Solo mostrar la leyenda una vez
            ),
            row=i+1, col=1
        )

        fig.add_trace(
            go.Scatter(
                x=[max_flow],
                y=[equipment],
                mode="markers",
                name="Max Flujo",
                marker=dict(color="blue", size=10),
                showlegend=(i == 0)  # Solo mostrar la leyenda una vez
            ),
            row=i+1, col=1
        )

        fig.add_annotation(
            x=(min_flow + max_flow)/2, y=equipment, 
            text=f"Último: {last_value:.2f}",
            showarrow=False,
            xanchor='left',
            yanchor='bottom',
            xshift=5,
            yshift=10,
            font=dict(size=12, color="black"),
            row=i+1, col=1
        )
    
        # Ajustar el rango y estilo del eje X para cada subplot
        fig.update_xaxes(
            range=[min_flow - 0.001, max_flow + 0.001],  # Rango individual para cada subplot
            row=i+1, col=1,
            showline=True,
            linewidth=2,
            linecolor='black',
            mirror=True
        )
    
    # Ajustar el layout del gráfico
    fig.update_layout(
        height=100 * len(flow_table["equipments"]),  # Altura proporcional a la cantidad de equipos
        legend_title="Valores",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=50, r=50, t=50, b=50),
        
    )

     # Añadir el título del eje X solo en la última gráfica
    fig.update_xaxes(
        title_text="Flujo",
        row=len(flow_table["equipments"]), col=1
    )
    
    # Ajustar el estilo del eje Y para todos los subplots
    fig.update_yaxes(
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    )
    fig.update_yaxes(
        title_text="Equipos",
        row=(len(flow_table["equipments"]) + 1)/2, col=1
    )
    
    return fig

