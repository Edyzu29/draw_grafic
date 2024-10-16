from shiny import App, Inputs, Outputs, ui, reactive, Session
from shinywidgets import output_widget, render_plotly

from datetime import date, timedelta

from data_tratement import *
from plotting import *

from labels import *



app_ui = ui.page_fluid(
    # Cambiar el color de fondo (opcional)
    ui.tags.style("""
        body {
            background-color: #B7E0FF;  /* Color de fondo de toda la página */
        }
        h1 {
            font-family: 'Arial', sans-serif;  /* Cambiar la fuente a Arial */
            font-size: 48px;  /* Tamaño de la fuente */
            font-weight: bold;  /* Negrita */
            color: #333333;  /* Color del texto */
            text-align: center;  /* Alineación centrada */
        }
    """),

    ui.h1("Modulo 1"),
    ui.layout_columns(
        # Colocar los selectores y el rango de fechas en la parte superior
        ui.layout_columns(
            ui.div(
                ui.input_select(
                    "Selector",
                    "Estación",
                    choices=Estaciones
                ),
                ui.tags.style("""
                #daterange .form-control {
                    font-size: 12px;
                }""")
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
            ),
            col_widths=[2, 10],  # Ocupa toda la parte superior
        ),
        
        # Tarjetas con los widgets a continuación
        ui.layout_columns(    
            ui.card(ui.card_header("Temperatura Interna de la Caseta"), output_widget("TEMP_INT")),
            ui.card(ui.card_header("Humedad Relativa Interna de la caseta"), output_widget("HR_INT")),
            col_widths=[6, 6],
        ),
        
        ui.layout_columns(
            ui.card(ui.card_header("PM10"), output_widget("PM10")),
            ui.card(
                ui.navset_tab(
                    ui.nav_panel("Variación del Flujo", output_widget("Variacion_flujo")),
                    ui.nav_panel("Datos del Flujo", output_widget("Datos_flujo")),
                ),
            ),
            ui.card(ui.card_header("PM25"), output_widget("PM25")),
            ui.card(ui.card_header("Parámetros Meteorológicos"), output_widget("Datos_meteorologicos")),
            col_widths=[8, 4, 8, 4],
        ),
        
        # Más tarjetas
        ui.layout_columns(
            ui.card(ui.card_header("SO2"), output_widget("SO2")),
            ui.card(ui.card_header("NO"), output_widget("NO")),
            ui.card(ui.card_header("NO2"), output_widget("NO2")),
            ui.card(ui.card_header("NOX"), output_widget("NOX")),
            ui.card(ui.card_header("H2S"), output_widget("H2S")),
            ui.card(ui.card_header("CO"), output_widget("CO")),
            col_widths=[6, 6, 6, 6, 6, 6],
        ),
        col_widths=[12, 12, 12]
    ),
    title="Módulo 1",
    class_="bslib-page-dashboard"
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