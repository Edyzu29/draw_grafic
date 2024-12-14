base = "vigamb_t_aire_"
    
tabla_trama = {
  "cabecera": {
    "id_correlativo": "id_correlativa",
    "id_estacion": "id_estacion",
    "des_nombre_estacion": "nombre_estacion",
    "des_fecha_data": "fecha_data",
    "des_hora_data": "hora_data",
    "fecha_data_logger_timestamp": "fecha_datalogger",
    "ind_calidad_datos": "ind_calidad_datos"
  },
  "metereologia": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD1": "EQUIPO_MET",
    "DBL_FD2": "PBAR_HPA",
    "DBL_FD3": "PP_MM",
    "DBL_FD4": "TEMP_CELC",
    "DBL_FD5": "HR_PORC",
    "DBL_FD6": "WS_MS",
    "DBL_FD7": "WD_SEXA",
    "DBL_FD8": "RS",
    "DBL_FD9": "TEMPERATURA_CASETA",
    "DBL_FD15": "SERIE_MET"
  },
  "pm10": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD16": "EQUIPO_PM10",
    "DBL_FD17": "PM10_UGM3",
    "DES_FD18": "PM10_ESTADO",
    "DES_FD30": "SERIE_PM10"
  },
  "pm25": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD31": "EQUIPO_PM25",
    "DBL_FD32": "PM25_SHARP_UGM3",
    "DES_FD33": "PM25_ESTADO",
    "DBL_FD34": "PM25_BETA_UGM3",
    "DBL_FD35": "PM25_OPTICO_UGM3",
    "DBL_FD37": "PM25_HUMEDAD_MUESTRA",
    "DBL_FD38": "PM25_TEMP_EQUIPO",
    "DBL_FD39": "PM25_PRESION_FLOW",
    "DBL_FD40": "PM25_PRESION_VACIO",
    "DBL_FD41": "PM25_FLOW_MUESTRA",
    "DBL_FD42": "PM25_ESTADO",
    "DES_FD44": "PM25_CONTADOR_CINTA",
    "DES_FD45": "SERIE_PM25"
  },
  "so2": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD46": "EQUIPO_SO2",
    "DBL_FD47": "SO2_PPB",
    "DES_FD48": "SO2_ESTADO",
    "DBL_FD49": "SO2_FLOW",
    "DBL_FD50": "SO2_LAMP_INT",
    "DBL_FD51": "SO2_INTERNAL_TEMP",
    "DBL_FD52": "SO2_PMT_VOLTAGE",
    "DBL_FD53": "SO2_CONV_TEMP",
    "DBL_FD54": "SO2_COEF_BG",
    "DBL_FD55": "SO2_COEF_SPAN",
    "DES_FD59": "SO2_ESTADO",
    "DES_FD60": "SERIE_SO2"
  },
  "h2s": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD61": "EQUIPO_H2S",
    "DBL_FD62": "H2S_PPB",
    "DES_FD63": "H2S_ESTADO",
    "DBL_FD64": "H2S_FLOW",
    "DBL_FD65": "H2S_LAMP_INT",
    "DBL_FD66": "H2S_INTERNAL_TEMP",
    "DBL_FD67": "H2S_REACTOR_TEMP",
    "DBL_FD68": "H2S_PMT_VOLTAGE",
    "DBL_FD69": "H2S_COEF_BG",
    "DBL_FD70": "H2S_COEF_SPAN",
    "DES_FD74": "H2S_ESTADO",
    "DES_FD75": "SERIE_H2S"
  },
  "co": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD76": "EQUIPO_CO",
    "DBL_FD77": "CO_PPB",
    "DES_FD78": "CO_ESTADO",
    "DBL_FD79": "CO_FLOW",
    "DBL_FD80": "CO_INTERNAL_TEMP",
    "DBL_FD81": "CO_SPEED_MOTOR",
    "DBL_FD82": "CO_VIAS_VOLTAGE",
    "DBL_FD83": "CO_CAMERA_TEMP",
    "DBL_FD84": "CO_COEF_BG",
    "DBL_FD85": "CO_COEF_SPAN",
    "DES_FD89": "CO_ESTADO",
    "DES_FD90": "SERIE_CO"
  },
  "no2": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD91": "EQUIPO_NO2",
    "DBL_FD92": "NO2_PPB",
    "DES_FD93": "NO2_ESTADO",
    "DBL_FD94": "NO_PPB",
    "DBL_FD95": "NOX_PPB",
    "DBL_FD96": "NO2_FLOW",
    "DBL_FD97": "NO2_CONV_TEMP",
    "DBL_FD98": "NO_COEF_BG",
    "DBL_FD99": "NOX_COEF_BG",
    "DBL_FD100": "NO_COEF_SPAN",
    "DBL_FD101": "NO2_COEF_SPAN",
    "DBL_FD102": "NOX_COEF_SPAN",
    "DES_FD104": "NO2_ESTADO",
    "DES_FD105": "SERIE_NO2"
  },
  "o3": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "DBL_FD109": "Temperatura_INT_CASETA",
    "DBL_FD110": "Humedad_INT_CASETA"
  },
  "hg": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD121": "EQUIPO_HG",
    "DBL_FD122": "MGT_NGM3",
    "DES_FD123": "MGT_ENVIDAS",
    "DES_FD135": "SERIE_HG"
  },
  "benceno": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD136": "ID_BENCENO",
    "DBL_FD137": "CONCENTRACION",
    "DES_FD150": "NUMERO DE SERIE"
  },
  "adi1": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD151": "ID_EQUIPO",
    "DBL_FD152": "CONCENTRACION",
    "DES_FD153": "ESTADO",
    "DES_FD165": "NUMERO DE SERIE"
  },
  "adi2": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD166": "ID_EQUIPO",
    "DBL_FD167": "CONCENTRACION",
    "DES_FD168": "ESTADO",
    "DES_FD180": "NUMERO DE SERIE"
  },
  "adi3": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD181": "ID_EQUIPO",
    "DBL_FD182": "CONCENTRACION",
    "DES_FD183": "ESTADO",
    "DES_FD195": "NUMERO DE SERIE"
  },
  "adi4": {
    "ID_CORRELATIVO": "ID_CORRELATIVO",
    "NUM_FD196": "ID_EQUIPO",
    "DBL_FD197": "CONCENTRACION",
    "DES_FD198": "ESTADO",
    "DES_FD210": "NUMERO DE SERIE"
  }
}


