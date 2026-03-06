-- KPI 4: Tiempo promedio de entrega por estado
SELECT 
    customer_state AS estado,
    ROUND(AVG(JULIANDAY(order_delivered_customer_date) - 
              JULIANDAY(order_purchase_timestamp)), 1) AS dias_entrega_promedio,
    COUNT(DISTINCT order_id) AS total_ordenes
FROM orders_full
WHERE order_status = 'delivered'
    AND order_delivered_customer_date IS NOT NULL
GROUP BY estado
ORDER BY dias_entrega_promedio DESC;