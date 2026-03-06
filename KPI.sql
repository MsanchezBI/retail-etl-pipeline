-- KPI 1: Ingresos totales por mes
SELECT 
    year_month,
    ROUND(SUM(revenue), 2) AS ingreso_total,
    COUNT(DISTINCT order_id) AS total_ordenes
FROM orders_full
WHERE order_status = 'delivered'
GROUP BY year_month
ORDER BY year_month;