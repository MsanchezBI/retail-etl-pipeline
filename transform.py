import pandas as pd
from extract import extraer_datos    #del archivo extract.py que yo creé, trae solo la función extraer_datos

dataframes=extraer_datos()

orders = dataframes["olist_orders_dataset"]
customers = dataframes["olist_customers_dataset"]
order_items = dataframes["olist_order_items_dataset"]
payments = dataframes["olist_order_payments_dataset"]
reviews = dataframes["olist_order_reviews_dataset"]
products = dataframes["olist_products_dataset"]
sellers = dataframes["olist_sellers_dataset"]
geolocation = dataframes["olist_geolocation_dataset"]
category_translation = dataframes["product_category_name_translation"]

#print(orders.info())
#print(orders.isnull().sum())  Validamos los nulos en las columnas

#========================================================================================
# ANALIZAMOS LA TABLA ORDERS                                                            #
#========================================================================================
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col])

orders = orders.dropna(subset=["order_purchase_timestamp"])  #si alguna orden no tiene fecha de compra, es inválida y no la queremos

orders["year"] = orders["order_purchase_timestamp"].dt.year
orders["month"] = orders["order_purchase_timestamp"].dt.month
orders["year_month"] = orders["order_purchase_timestamp"].dt.to_period("M").astype(str)

#========================================================================================
# ANALIZAMOS LA TABLA PRODUCTS                                                          #
#========================================================================================

products = products.merge(
    category_translation,
    on="product_category_name",
    how="left"
)

#Ahora verifica el resultado
#print(products.columns.tolist())
#print(products.shape)

#========================================================================================
# ANALIZAMOS LA TABLA DE HECHOS                                                         #
#========================================================================================

#cada fila de orders_full va a representar: "Un producto vendido, con toda su información"

orders_full = orders.merge(order_items, on="order_id", how="left")               
orders_full = orders_full.merge(customers, on="customer_id", how="left")          
orders_full = orders_full.merge(products, on="product_id", how="left")
orders_full = orders_full.merge(sellers, on="seller_id", how="left")

#print(orders_full.shape)
#print(orders_full.columns.tolist())

#product_category_name_translation: 71 filas, 2 columnas
#(113425, 33)    ===>  ahora tiene mas filas porque una 
#                      orden puede tener varios productos,La misma orden se repite una vez por cada producto que contenía

#print(orders_full.columns.tolist())

#========================================================================================
# LIMPIEZA FINAL                                                                        #
#========================================================================================
columnas_a_eliminar = [
    "customer_zip_code_prefix",
    "seller_zip_code_prefix",
    "product_name_lenght",
    "product_description_lenght",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

orders_full = orders_full.drop(columns=columnas_a_eliminar)

orders_full["revenue"] = orders_full["price"] + orders_full["freight_value"]  # Agregamos la columna del ingreso total por que es lo que realmente pagó el cliente, incluyendo el costo de envío

def transformar_datos():
    return orders_full

if __name__ == "__main__":
    df = transformar_datos()
    print(df.shape)
    print(df.head())