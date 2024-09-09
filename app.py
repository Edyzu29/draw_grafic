from shiny import App, Inputs, Outputs, render, ui, reactive, Session
from shinywidgets import output_widget, render_plotly

from datetime import date, timedelta

from grafic import *
from plotting import *
import plotly.express as px

from labels import *


def filter_data(data, station, fechas = tuple()):

    data_filtered = data[(data['date'] >= str(fechas[0])) & (data['date'] <= str(fechas[1]))]
    data_filtered = data_filtered[data_filtered['ID_ESTACION'] == station]

    return data_filtered

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select(
            "Selector",
            "Estacion",
            choices=Estaciones
        ),
        ui.div(
            ui.input_date_range(
                "daterange", 
                "Rango de Tiempo", 
                language="es", 
                start=(date.today() - timedelta(days=5)),
                format="d/m/yy",
            ),
            ui.tags.style("""
            #daterange .form-control {
                font-size: 12px;
            }""")
        )),
    ui.layout_columns(    
        ui.card(ui.card_header("Temperatura"), output_widget("TEMP_INT"),),
        ui.card(ui.card_header("Humedad"), output_widget("HR_INT"),),
        ui.card(ui.card_header("PM10"), output_widget("PM10"),),
        ui.card(
            ui.card_header("Flujos"), 
            ui.nav_panel(
              "Variacion",
                output_widget("Flujos"),),
            ui.nav_panel(
              "Datos",
                output_widget("Flujos"),),
            ),
        ui.card(ui.card_header("PM25"), output_widget("PM25"),),
        col_widths=[6, 6, 8,4,8],
        ),

    
    title="Temperatura Interna de la caseta",
    class_="bslib-page-dashboard",
)
    

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def data() -> pd.DataFrame:
        dates = input.daterange()
        station = input.Selector()
        return  filter_data(df, int(station), dates)
    
    @render_plotly
    def TEMP_INT():
        date = "date"
        parametro = "TEMP_INT_CASETA"
        return plot_scatter(data(), date, parametro, 20, 30)
    
    @render_plotly
    def HR_INT():
        date = "date"
        parametro = "HUM_INT_CASETA"
        return plot_scatter(data(), date, parametro, 0, 95)

    @render_plotly
    def PM10():
        date = "date"
        parametro = "PM10_CONC"
        return plot_scatter(data(), date, parametro, switch_limit_manual=False)
    
    @render_plotly
    def PM25():
        date = "date"
        parametro = "PM25_CONC"
        return plot_scatter(data(), date, parametro, switch_limit_manual=False)
    
    @render_plotly
    def Variacion_flujo():
        return plot_dumbbell(data())
    
    def Datos_flujos():
        date = "date"
        parametro = ""
        return plot_simple(data(), date, )
           

app = App(app_ui,server)