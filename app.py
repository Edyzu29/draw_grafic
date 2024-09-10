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
        ui.layout_columns(    
            ui.card(ui.card_header("Temperatura"), output_widget("TEMP_INT"),),
            ui.card(ui.card_header("Humedad"), output_widget("HR_INT"),),
            col_widths=[6, 6],
            ),
        
        ui.layout_columns(
            ui.card(ui.card_header("PM10"), output_widget("PM10"),),
            ui.card(
                
                    ui.navset_tab(
                        ui.nav_panel(
                            "Variacion del Flujo",
                            output_widget("Variacion_flujo"),
                        ),
                        ui.nav_panel(
                            "Datos del Flujo",
                            output_widget("Datos_flujo"),
                        ),
                    ),
                
            ),
            ui.card(ui.card_header("PM25"), output_widget("PM25"),),
            ui.card(ui.card_header("Parametros Meteorologicos"), output_widget("Datos_meteorologicos"),),
            col_widths=[8,4,8,4],
            ),
        ui.card(ui.card_header("SO2"), output_widget("SO2"),),
        ui.card(ui.card_header("NO"), output_widget("NO"),),
        ui.card(ui.card_header("NO2"), output_widget("NO2"),),
        ui.card(ui.card_header("NOX"), output_widget("NOX"),),
        ui.card(ui.card_header("H2S"), output_widget("H2S"),),
        ui.card(ui.card_header("CO"), output_widget("CO"),),
        col_widths=[12,12,6,6,6,6,6,6],
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
        return plot_dumbbell_flow(data())
    
    @render_plotly
    def Datos_flujo():
        return plot_simple_flow(data())
    
    @render_plotly
    def Datos_meteorologicos():
        return plot_meteorologica(data())
    
    @render_plotly
    def SO2():
        date = "date"
        parametro = "SO2_CONC"
        return plot_scatter(data(), date, parametro, switch_limit_manual=False)
    
    @render_plotly
    def H2S():
        date = "date"
        parametro = "H2S_CONC"
        return plot_scatter(data(), date, parametro, switch_limit_manual=False)
    
    @render_plotly
    def CO():
        date = "date"
        parametro = "CO_CONC"
        return plot_scatter(data(), date, parametro, switch_limit_manual=False)
    
    @render_plotly
    def NO():
        date = "date"
        parametro = "NO_CONC"
        return plot_scatter(data(), date, parametro, switch_limit_manual=False)
    
    @render_plotly
    def NO2():
        date = "date"
        parametro = "NO2_CONC"
        return plot_scatter(data(), date, parametro, switch_limit_manual=False)
    
    @render_plotly
    def NOX():
        date = "date"
        parametro = "NOX_CONC"
        return plot_scatter(data(), date, parametro, switch_limit_manual=False)
           

app = App(app_ui,server)