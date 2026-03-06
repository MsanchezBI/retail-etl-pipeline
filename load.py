import sqlite3
import os
from transform import transformar_datos

DB_PATH = os.path.join("..", "database", "olist.db")  #es la ruta donde se va a crear el archivo olist.db dentro de tu carpeta database/. Todavía no existe, solo le estamos diciendo a Python dónde crearla.

def cargar_datos():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    #===========================================
    # INICIO DE LA CONEXION A LA BASE DE DATOS
    #===========================================

    conn = sqlite3.connect(DB_PATH)
    df = transformar_datos()

    df.to_sql("orders_full", conn, if_exists="replace", index=False)

    #CONSIDERACIONES:

    #if_exists="replace" → borra la tabla y la crea de nuevo cada vez que ejecutas el script. Siempre tienes datos frescos. ✅
    #if_exists="append" → agrega filas a la tabla existente sin borrarla. Si ejecutas dos veces, tendrías los datos duplicados.

    #En nuestro caso replace es correcto — cada vez que corras el ETL quieres datos actualizados, no duplicados.

    print("Tabla orders_full cargada correctamente")
    print(f"Total registros: {len(df)}")

    #===========================================
    # CIERRE DE LA CONEXIÓN
    #===========================================
    conn.close()
    print("Conexión cerrada correctamente")

if __name__ == "__main__":
    cargar_datos()