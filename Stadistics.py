import pandas as pd
import numpy as np
import scipy.stats as stats

def tukey_2visagra(data = pd.DataFrame(), camp = str()):
    Q1 = data[camp].quantile(0.25) # type: ignore
    Q3 = data[camp].quantile(0.75)

    # Calcular el rango intercuartílico (IQR)
    IQR = Q3 - Q1

    # Calcular los límites inferior y superior usando el método de Tukey
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    data_filtrado = data[(data[camp] >= limite_inferior) & (data[camp] <= limite_superior)]

    return data_filtrado

def tukey_outliders(data = pd.DataFrame(), camp = str()):
    Q1 = data[camp].quantile(0.25) # type: ignore
    Q3 = data[camp].quantile(0.75)

    # Calcular el rango intercuartílico (IQR)
    IQR = Q3 - Q1

    # Calcular los límites inferior y superior usando el método de Tukey
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    data_filtrado = data[(data[camp] < limite_inferior) | (data[camp] > limite_superior)]

    return data_filtrado

# Función para calcular el intervalo de confianza
def intervalo_confianza(data_set, nivel_confianza=0.95):
    n = len(data_set)
    media = np.mean(data_set)
    desviacion_estandar = np.std(data_set, ddof=1)  # ddof=1 para muestra
    error_estandar = desviacion_estandar / np.sqrt(n)
    z = stats.norm.ppf(1 - (1 - nivel_confianza) / 2)  # Valor crítico Z para el nivel de confianza

    # Calcular el rango del intervalo de confianza
    margen_error = z * error_estandar
    intervalo = (media - margen_error, media + margen_error)
    return intervalo

def Limite_inf_sup(data, parametro):
    
    # df_filtered = tukey_2visagra(data, parametro)
    df_filtered = data
    
    # Calcular el promedio general
    promedio_general = np.mean(df_filtered[parametro])

    # Separar datos superiores e inferiores al promedio general
    data_superior = [x for x in df_filtered[parametro] if x > promedio_general]
    data_inferior = [x for x in df_filtered[parametro] if x < promedio_general]
    
    # liites
    Limt_sup = intervalo_confianza(data_superior)
    Limt_inf = intervalo_confianza(data_inferior)
    
    return Limt_inf[0], Limt_sup[1]
