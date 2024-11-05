import os
import cx_Oracle

dsn = '(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.sa-bogota-1.oraclecloud.com))(connect_data=(service_name=g665c212b48e929_a1u480usxkto5pr9_low.adb.oraclecloud.com))(security=(ssl_server_cert_dn="CN=adb.sa-bogota-1.oraclecloud.com, O=Oracle Corporation, L=Redwood City, ST=California, C=US")))'
username =  "Admin"
password = "PruebaModulo1-" 

instant_client_path = r"C:\Users\admin\oracle\instantclient_23_5" 

# Inicializa el cliente Oracle con la ruta definida
cx_Oracle.init_oracle_client(lib_dir=instant_client_path)

connection = cx_Oracle.connect(
    user=username,
    password=password,
    dsn=dsn
)

# Ejecutar una consulta
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM PARAISO")
# for row in cursor:
#     print(row)

# # Cerrar la conexión
# cursor.close()
connection.close()
