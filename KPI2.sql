-- KPI 2: Top 10 categorías por ingreso
SELECT 
    product_category_name_english AS categoria,
    ROUND(SUM(revenue), 2) AS ingreso_total,
    COUNT(DISTINCT order_id) AS total_ordenes,
    ROUND(AVG(price), 2) AS precio_promedio
FROM orders_full
WHERE order_status = 'delivered'
    AND product_category_name_english IS NOT NULL
GROUP BY categoria
ORDER BY ingreso_total DESC
LIMIT 10;