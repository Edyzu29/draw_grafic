import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px
from labels import *
from grafic import *

def plot_scatter(data, x_axis, y_axis, lit_min, lit_max):
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

def plot_simple(data: pd.DataFrame):

    flow_equitments = [x for x in data.columns if "FLOW" in x]

    fig = make_subplots(
        rows=len(flow_equitments), 
        cols=1, 
        vertical_spacing=0.12
    )

    for i, equiptment in enumerate(flow_equitments, start=1):
        fig.add_trace(
            go.Scatter(
                
                x= data['date'],
                y= data[equiptment],
                mode="lines"
            ) ,
            row=i, 
            col=1
        )


    fig.update_layout(
        height=100 * len(flow_equitments),  # Altura proporcional a la cantidad de equipos
        legend_title="Valores",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=50, r=50, t=50, b=50),
        
    )

     # Añadir el título del eje X solo en la última gráfica
    fig.update_xaxes(
        title_text="Flujo",
        row=len(flow_equitments), col=1
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
        row=(len(flow_equitments) + 1)/2, col=1
    )

    fig.show()

    return fig


def plot_dumbbell(data = pd.DataFrame):
    
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


plot_simple(df_filtrado)