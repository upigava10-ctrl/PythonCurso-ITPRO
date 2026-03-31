import pandas as pd
import numpy as np
import json
import html as htmlLib





#Proyecto Final AVENCE 1 Curso Python IT-PRO
#Predicción de precio de Vivienda en la Benito Juarez

#Nombre: Aura del Carmen García Vázquez


#Origen de JSON, datos de la Alcadia Benito Juarez
#http://www.economia.gob.mx/datamexico/es/profile/geo/benito-juarez#population-pyramid
#http://www.economia.gob.mx/datamexico/es/profile/geo/benito-juarez#empleo-ocupaciones
#geoJSON
#https://datos.cdmx.gob.mx/dataset/crecimiento-habitacional-tasa-de-crecimiento-media-anual-2000-2010-y-marginalidad-urbana


df_salario = pd.read_json("Distribucion-fuerza-laboral-CDMX-por-salario-promedio-mensual.json")
df_poblacion = pd.read_json("Piramide-poblacional-total-de-Benito-Juarez-2020.json")

with open("creci-habi-tasa-de-crecimiento-media-anual-2000-2010.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#print(df_crecimiento.columns)

#print(df_salario_min_viable["Monthly Wage"])
#print(df_poblacion[["Age Range ID","Age Range"]])

TCMA_col_BJ = []
for feature in data["features"]:
    if feature["properties"]["alcaldia"] == "BENITO JUAREZ":
        TCMA_col_BJ.append(feature["properties"]["TCMA_VIV"])


df_salario_min_viable = df_salario[df_salario["Monthly Wage"] >= 15000]
df_salario_min_viable = df_salario_min_viable.reset_index(drop=True)

df_rango_edad_30_44 = df_poblacion[(df_poblacion["Age Range ID"] == 7) | (df_poblacion["Age Range ID"] == 8) | (df_poblacion["Age Range ID"] == 9)]
df_rango_edad_30_44 = df_rango_edad_30_44.reset_index(drop=True)

prom_salario_objetivo= np.mean(df_salario_min_viable["Monthly Wage"])
suma_poblacion_objetivo = np.sum(df_rango_edad_30_44["Population"])
prom_tasa_habi = np.mean(TCMA_col_BJ)

print(f"Prom salario en rango: {prom_salario_objetivo}")
print(f"Total poblacion en rango: {suma_poblacion_objetivo}")
print(f"Promedio de la tasa de crecimiento habitacional en la alcaldia {prom_tasa_habi}")

##############Crecimiento exponencial de población##############
# t= float(input("¿A cuántos años desea estimar? "))
# pob_fut = suma_poblacion_objetivo*(1+prom_tasa_habi)**t
# print(pob_fut)

###############Extraer valores del html de una página guardada ##############
with open("Prec_Casas_Dep_Venta_BJ _Vivanuncios.html", "r", encoding="utf-8") as f:
    html = f.read()

##############Precio de vivienda promedio 2016-2021###############
inicio = html.find('data-chart="') + len('data-chart="')
fin = html.find('">', inicio)
data_raw = html[inicio:fin]

data_clean = htmlLib.unescape(data_raw)
data_json = json.loads(data_clean)

# print(data_json["statistics"])

for item in data_json["statistics"]:
    print(item["label"], item["value"])

partes = html.split('c-table__table-column-3">')
valores_m2 = []

#############Precio promedio por m^2 en la Benito Juarez##############
for parte in partes[2:]:
    valor = parte.split("</td>")[0]
    valores_m2.append(valor)
# print(valores_m2)

valores_limpios = [
    int(v.replace("$", "").replace(",", ""))
    for v in valores_m2
]

print(valores_limpios)



#precio_vivienda = precio_m2 * metros
#pago_maximo = salario * 0.30
#1 obtener_datos_api ?
#2 limpiar_datos 
#3 modelo_demanda
#4 graficas



## --- Parámetros de simulación ---
#poblacion_total = 434153
#media_edad = 39

## Generar datos de ejemplo (¡esto es una simulación!)
#np.random.seed(42) # Para que los resultados sean reproducibles
#edades = np.random.normal(media_edad, 12, poblacion_total).astype(int)
#ingresos = np.random.exponential(20000, poblacion_total).astype(int) # Simulación simple

#df_benito_juarez = pd.DataFrame({'edad': edades, 'ingreso_mensual': ingresos})
## Limpiar datos (edades negativas, ingresos muy bajos, etc.)
#df_benito_juarez = df_benito_juarez[(df_benito_juarez['edad'] >= 18) & (df_benito_juarez['ingreso_mensual'] > 6000)]
#print(df_benito_juarez.head())

## Ejemplo de filtro
#condicion_edad_hombre = (df_benito_juarez['edad'] <= 40) # 40 + 30 = 70
#condicion_edad_mujer = (df_benito_juarez['edad'] <= 45) # 45 + 30 = 75

#condicion_ingreso = df_benito_juarez['ingreso_mensual'] > 15000 # Ingreso mínimo para un crédito digno

#df_compradores_potenciales = df_benito_juarez[condicion_ingreso] # Aplicar filtros
#print(f"Total de compradores potenciales: {len(df_compradores_potenciales)}")
