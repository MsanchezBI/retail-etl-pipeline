# 🛒 Pipeline ETL + Análisis de Ventas Retail — Olist E-Commerce

## 📌 Descripción
Pipeline ETL automatizado que procesa 113,425 registros reales de ventas 
del e-commerce brasileño Olist (2016-2018). Transforma 9 fuentes de datos 
crudos en una base de datos analítica lista para Power BI.

## 🛠️ Tecnologías
- **Python** (pandas, sqlite3) — ETL pipeline
- **SQLite** — Base de datos analítica
- **SQL** — KPIs de negocio
- **Power BI** — Dashboard de 3 páginas con data storytelling,indicadores KPI, análisis geográfico y tendencia de ventas
- **DBeaver** — Exploración de datos

## 📁 Estructura del Proyecto
```
Proyecto ETL/
├── Data-inputs/     → 9 fuentes de datos crudos (Olist)
├── etl/
│   ├── extract.py   → Lectura automática de CSV y ZIP
│   ├── transform.py → Limpieza, joins y enriquecimiento
│   └── load.py      → Carga a SQLite
├── sql/
│   └── kpis.sql     → 5 KPIs comerciales
├── database/
│   └── olist.db     → Base de datos final
└── README.md
```

## 📊 KPIs Desarrollados
| KPI | Descripción |
|-----|-------------|
| Ingresos por mes | Evolución mensual de ventas 2016-2018 |
| Top 10 categorías | Categorías con mayor ingreso |
| Ticket promedio | Gasto promedio por cliente según estado |
| Lead time de entrega | Días promedio de entrega por estado |
| Performance vendedores | Ingreso generado por vendedor según estado |

## 🔍 Insights Principales
- **health_beauty** es la categoría #1 en ingresos
- **Roraima (RR)** tiene el mayor tiempo de entrega: 28 días promedio
- **Maranhão (MA)** tiene el vendedor más eficiente: $48,169 por vendedor
- Crecimiento sostenido de ventas de $127K (ene-2017) a $751K (oct-2017)

## ▶️ Cómo ejecutar
```bash
# 1. Clonar el repositorio
git clone https://github.com/MsanchezBI/retail-etl-pipeline

# 2. Instalar dependencias
pip install pandas

# 3. Ejecutar el pipeline completo
cd etl
python load.py
```

## 📂 Datos
Dataset público de Kaggle: 

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
