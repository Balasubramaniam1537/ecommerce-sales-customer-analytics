import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

print(" Exporting local MySQL database records to an analytical CSV sheet...")

# Define credentials to connect locally
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

# Extract and save locally
mysql_engine = create_engine(mysql_url)
df = pd.read_sql("SELECT * FROM master_sales_data;", con=mysql_engine)
df.to_csv("master_sales_data.csv", index=False)

print("print("Data export completed successfully. Output saved to master_sales_data.csv.")

