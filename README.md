
Enterprise E-Commerce Sales, Cloud Data Warehouse & Predictive Analytics Platform

An end-to-end data platform architecture that synchronizes a local transactional database ecosystem, routes automated extract-transform-load (ETL) network data bridges, hosts an optimized cloud data warehouse layer, applies machine learning predictive models, and surfaces data analytics metrics on an executive presentation dashboard.

---

Technology Stack & Platform Infrastructure
*   Operational Database (OLTP): Local MySQL Server containing relational analytical structures.
*   Cloud Data Warehouse (OLAP): Snowflake Cloud Data Warehousing environment (`ECOMMERCE_ANALYTICS_DW`).
*   Data Pipeline Layer (ETL): Python (`Pandas`, `SQLAlchemy`, native `snowflake-connector-python` streaming utilities).
*   Advanced Analytics Core: Snowflake SQL Engine utilizing Window Functions and Common Table Expressions (CTEs).
*   Predictive Analytics (Data Science): XGBoost Classifier Model built via the `Scikit-Learn` optimization framework.
*   Business Intelligence Reporting: Power BI Desktop importing live integrated datasets.

---

 System Pipeline Architecture Map

```text
[Local MySQL OLTP] 
       ⬇  (Python ETL Engine via SQLAlchemy + write_pandas)
[Snowflake Cloud DW - RAW Layer] 
       ⬇  (Snowflake SQL Aggregations via CTEs & Window Functions)
[Snowflake Analytical Core] 
       ⬇ 
       ➔ [Python Feature Pipeline] ➔ [XGBoost ML Classifier Engine] ➔ (97.00% Churn Accuracy Logs)
       ➔ [Local Flat File Export] ➔ [Power BI Executive Visualization Canvas Dashboard]
```

---

 Core Repository Manifest & Blueprints

1. Data Definition & Ingestion Layer
* `schema.sql`: A relational SQL script configuring your database schema inside MySQL. It establishes 16 master columns mapping transactional metrics like Order IDs, customer identification data, and purchase values.
* `generate_data.py`: A Python script utilizing deterministic tracking seeds (`seed(101)`) to populate the system rows with 50,000 highly realistic transaction sequences across international cities. It enforces commercial parameters inside a processing loop (`Revenue = (Quantity * Price) - Discount`) before loading rows into MySQL.

2. Cloud Storage Integration & Execution Core
* `migrate_data.py`: A secure, password-masked Python ETL pipeline. It reads rows locally, transforms column frameworks to uppercase text strings to meet standard syntax rules, and streams records to your remote warehouse over the network via high-speed `write_pandas` scripts.
* `snowflake_analytics.sql`:An analytics script executed inside your Snowflake browser canvas window. It deploys isolated database spaces and compute instances (`COMPUTE_WH`), running complex CTE structures and Left Joins to evaluate operational KPIs.
* Key Business Metric Extracted: The query isolated a primary regional market trend, showing that the Apparel category inside India ranked as your top-grossing sector, capturing 2,287,921.80 in net cloud revenue.

 3. Data Science Predictive Analytics Layer
* `predict_churn.py`: A data science script that pulls columns back down from Snowflake into local Python memory spaces. It computes an algorithmic behavior indicator rule (a customer has churned if their review score is ≤ 2 or if their order is Cancelled), normalizes column weighting parameters via `StandardScaler`, and trains an ensemble XGBoost Classifier Model that successfully registers a 97.00% target accuracy score.

 4. Production Operations & Dashboard Reporting
* `run_pipeline.py`:A master orchestrator file constructed manually using Python’s native system execution tracking module (`logging`). It handles stage execution runs and captures standard text errors seamlessly while removing all verbose print notifications from your log outputs.
* `export_data.py`: An extraction file running data download loops to structure a clean flat file spreadsheet asset (`master_sales_data.csv`).
* `requirements.txt`:An environment management tracking checklist grouping every necessary framework library version to automate reproducibility steps.
* `ECommerce_Sales_&_Customer_Analytics.pbix`: Your Power BI Desktop reporting layout, displaying global penetration metrics across three visual sectors: Executive Sales Card, Product Revenue Distribution Bar Charts, and a Geographic Sales Bubble Map Grid

---

 Local Execution Instructions

To execute the entire end-to-end data platform flow sequentially, log system metrics to your console, train the analytical validation models, and generate the flat data sheets, run this single orchestrator command inside your terminal workspace:

```powershell
pip install -r requirements.txt
python run_pipeline.py
```
