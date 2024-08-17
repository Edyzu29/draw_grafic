import pandas as pd

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
