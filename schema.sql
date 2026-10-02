-- Local Operational Relational Schema Blueprint Definition
CREATE DATABASE IF NOT EXISTS ecommerce_analytics;
USE ecommerce_analytics;

CREATE TABLE IF NOT EXISTS master_sales_data (
    Order_ID VARCHAR(50),
    Customer_ID VARCHAR(50),
    Product_ID VARCHAR(50),
    Product_Name VARCHAR(100),
    Category VARCHAR(50),
    Date DATETIME,
    City VARCHAR(50),
    Country VARCHAR(50),
    Quantity INT,
    Price DECIMAL(10, 2),
    Discount DECIMAL(10, 2),
    Revenue DECIMAL(10, 2),
    Payment_Method VARCHAR(30),
    Order_Status VARCHAR(20),
    Review_Score INT,
    Customer_Segment VARCHAR(30)
);
