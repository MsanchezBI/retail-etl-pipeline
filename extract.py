# Librerías necesarias para el ETL
import pandas as pd
import zipfile
import os

DATA_INPUT=os.path.join("..","Data-inputs")          #la carpeta de datos está en ../Data-inputs
archivos=os.listdir(DATA_INPUT)                      # devuelve solo los nombres de los archivos

#Realizamos un recorre a cada archivo, y 

dataframes={}                                       #Almacenamos en un diccionario

for archivo in archivos:
    ruta_completa=os.path.join(DATA_INPUT,archivo)
    if archivo.endswith(".zip"):
        with zipfile.ZipFile(ruta_completa, "r") as z:
            nombre_csv = z.namelist()[0]
            with z.open(nombre_csv) as f:
                df = pd.read_csv(f)
    else:
        df = pd.read_csv(ruta_completa)
    nombre = archivo.replace(".csv.zip", "").replace(".csv", "")
    dataframes[nombre] = df
    print(f"{nombre}: {df.shape[0]} filas, {df.shape[1]} columnas")

def extraer_datos():
    return dataframes

if __name__ == "__main__":                          #solo ejecuta esto si estoy corriendo este archivo directamente
    extraer_datos()

