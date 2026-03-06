-- KPI 5: Performance de vendedores
SELECT 
    seller_state AS estado_vendedor,
    COUNT(DISTINCT seller_id) AS total_vendedores,
    ROUND(SUM(revenue), 2) AS ingreso_total,
    ROUND(SUM(revenue) / COUNT(DISTINCT seller_id), 2) AS ingreso_por_vendedor
FROM orders_full
WHERE order_status = 'delivered'
GROUP BY estado_vendedor
ORDER BY ingreso_por_vendedor DESC
LIMIT 10;