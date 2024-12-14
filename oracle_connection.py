import os
import cx_Oracle

from detalle_bd import *

# # Definir los parámetros de conexión
# dsn =  cx_Oracle.makedsn("10.6.0.15", 1532, service_name="dvssobd")
# # Para Service Name: cx_Oracle.makedsn("hostname", 1521, service_name="nombre_service")

# try:
#     # Crear la conexión
#     connection = cx_Oracle.connect(user="VIGAMB", password="desarrollo", dsn=dsn)
#     print("Conexión exitosa a la base de datos Oracle")

#     # Crear un cursor
#     cursor = connection.cursor()

#     # Ejecutar una consulta
#     cursor.execute("SELECT * FROM pm10_horas")
#     for row in cursor:
#         print(row)

# finally:
#     # Cerrar la conexión
#     if connection:
#         connection.close()
        
tabla = "cabecera"
tablas = list(tabla_trama.keys())

columns = list(tabla_trama["cabecera"].keys())
print(tablas)

print(columns)

query = "from " + tabla + "." + 