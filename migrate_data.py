import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

print("Starting ETL Data Migration Process...")


MYSQL_USER = "root"
MYSQL_PASSWORD = "your_mysql_password_here"  
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_NAME = "ecommerce_analytics"

mysql_url = URL.create(
    drivername="mysql+mysqlconnector",
    username=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    database=MYSQL_NAME
)

print("Extracting 50,000 records from local MySQL database...")
mysql_engine = create_engine(mysql_url)
query = "SELECT * FROM master_sales_data;"
df = pd.read_sql(query, con=mysql_engine)
print(f"Extraction complete! Loaded {len(df)} rows into memory.")


SNOWFLAKE_USER = "YOUR_SNOWFLAKE_USERNAME"     
SNOWFLAKE_PASSWORD = "your_snowflake_password_here"             
SNOWFLAKE_ACCOUNT = "jmlnvcs-zf81443"

print("Connecting to Snowflake Cloud Storage layer...")
ctx = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse="COMPUTE_WH",
    database="ECOMMERCE_ANALYTICS_DW",
    schema="RAW"
)


print("Initiating high-speed bulk migration to Snowflake (Streaming 50,000 rows)...")


df.columns = [col.upper() for col in df.columns]


success, nchunks, nrows, _ = write_pandas(
    conn=ctx,
    df=df,
    table_name="MASTER_SALES_DATA"
)

# Close connection channel cleanly
ctx.close()

if success:
    print(f"ETL pipeline executed successfully. Ingested {nrows} records into Snowflake data warehouse.")
else:
    print("ETL pipeline failed. Ingestion encountered an unexpected exception.")

