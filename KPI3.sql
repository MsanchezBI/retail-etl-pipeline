-- KPI 3: Ticket promedio por estado del cliente
SELECT 
    customer_state AS estado,
    ROUND(AVG(revenue), 2) AS ticket_promedio,
    COUNT(DISTINCT order_id) AS total_ordenes
FROM orders_full
WHERE order_status = 'delivered'
GROUP BY estado
ORDER BY ticket_promedio DESC;