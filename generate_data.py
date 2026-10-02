import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Initialize data generation frameworks
fake = Faker()
Faker.seed(101)  
random.seed(101)
np.random.seed(101)



print("Initializing data generation sequence for 50,000 analytical records...")


DB_USER = "root"
DB_PASSWORD = "your_mysql_password_here"  
DB_PORT = "3306"
DB_NAME = "ecommerce_analytics"


connection_url = URL.create(
    drivername="mysql+mysqlconnector",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)

num_records = 50000

categories = {
    "Electronics": ["Smartphone 14 Pro", "Wireless ANC Headphones", "4K Ultra-Wide Monitor", "Mechanical Keyboard"],
    "Furniture": ["Ergonomic Desk Chair", "Solid Oak Coffee Table", "Standing Desk Frame", "LED Floor Lamp"],
    "Apparel": ["Waterproof Parka", "Premium Denim Jeans", "Breathable Mesh Sneakers", "Organic Cotton Hoodie"],
    "Home Kitchen": ["Air Fryer XL", "Smart Espresso Machine", "Stainless Steel Cookware Set", "Blender 1200W"],
    "Books & Stationery": ["Data Engineering Handbook", "Leatherbound Journal", "Fountain Pen Set", "Architect Planner"]
}

category_list = list(categories.keys())
segments = ["Champions", "Loyal Customers", "Potential Loyalists", "New Customers", "At-Risk", "Hibernating"]
payments = ["Credit Card", "PayPal", "UPI", "Debit Card"]
statuses = ["Delivered", "Shipped", "Processing", "Cancelled"]

print("Creating dimensional frames...")
unique_customers = [f"CUST-{10000 + i}" for i in range(5000)]
cities_pool = [(fake.city(), random.choice(["USA", "India", "United Kingdom", "Canada", "Germany"])) for _ in range(100)]

data = []

for i in range(1, num_records + 1):
    order_id = f"ORD-{100000 + (i // 2)}"  
    customer_id = random.choice(unique_customers)
    
    category = random.choice(category_list)
    product_name = random.choice(categories[category])
    product_id = f"PROD-{hash(product_name) % 10000:04d}"
    
    city, country = random.choice(cities_pool)
    order_date = fake.date_time_between(start_date="-3y", end_date="now")
    
    quantity = int(random.choices([1, 2, 3, 4, 5], weights=[0.60, 0.25, 0.10, 0.03, 0.02])[0])
    base_price = float(random.randint(15, 1200) if category != "Books & Stationery" else random.randint(10, 80))
    
    discount = 0.0
    if random.random() < 0.40:
        discount = round(base_price * quantity * random.choice([0.05, 0.10, 0.15, 0.20]), 2)
        
    revenue = round((quantity * base_price) - discount, 2)
    
    status = random.choices(statuses, weights=[0.80, 0.10, 0.07, 0.03])[0]
    payment = random.choice(payments)
    review = int(random.choices([5, 4, 3, 2, 1], weights=[0.55, 0.25, 0.10, 0.06, 0.04])[0])
    segment = random.choices(segments, weights=[0.15, 0.25, 0.20, 0.15, 0.15, 0.10])[0]
    
    data.append({
        "Order_ID": order_id,
        "Customer_ID": customer_id,
        "Product_ID": product_id,
        "Product_Name": product_name,
        "Category": category,
        "Date": order_date,
        "City": city,
        "Country": country,
        "Quantity": quantity,
        "Price": base_price,
        "Discount": discount,
        "Revenue": revenue,
        "Payment_Method": payment,
        "Order_Status": status,
        "Review_Score": review,
        "Customer_Segment": segment
    })

df = pd.DataFrame(data)

print("Streaming to local MySQL instances...")
engine = create_engine(connection_url)
df.to_sql('master_sales_data', con=engine, if_exists='append', index=False)

print("Data ingestion complete. Successfully loaded 50,000 analytical records into MySQL schema.")

