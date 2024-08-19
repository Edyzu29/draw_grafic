from plotnine import aes, geom_path, geom_hline, ggplot, theme_light, labs

from shiny import App, Inputs, Outputs, render, ui, reactive

from datetime import date, timedelta

from grafic import *

magenta = "#9E2F68"
magenta_light = "#E5C8D6"

def plot_path(df):
    plot = (
        ggplot(
            df,
            aes(x="date", y="TEMP_INT_CASETA"))
        + geom_path(colour="#ff69b4", size=0.8)
        + geom_hline(yintercept=[20,30], 
                    color = [magenta, magenta_light],
                    linetype="dashed",
                    size=1)
        + labs(x="Fechas", y="Temperatura (°C)")
        + theme_light()
        )
    return plot


app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select(
            "Selector_Estacion",
            "Estacion",
            choices=[
                "Paraiso",
                "Nieveria",
                "Roj",
                "Amarillo"
            ]
        ),
        ui.input_date_range("daterange", "Rango de Tiempo", language="es", start=(date.today()- timedelta(days=10)))),
    ui.card(
            ui.card_header("Temperatura"),
            ui.output_plot("Temperatura_plot"),),
    
    title="Temperatura Interna de la caseta",
    class_="bslib-page-dashboard",
)
    

def server(input: Inputs):
    @reactive.calc()
    def data() -> pd.DataFrame:
        return df_filtrado


    @render.plot
    def Temperatura_plot():
        return plot_path(data())
       

app = App(app_ui,server)