-- Snowflake Cloud Data Warehouse Reporting Engine Logic
USE DATABASE ECOMMERCE_ANALYTICS_DW;
USE SCHEMA RAW;

WITH CategoryMetrics AS (
    SELECT 
        CATEGORY,
        COUNTRY,
        COUNT(DISTINCT ORDER_ID) AS Total_Orders,
        SUM(QUANTITY) AS Total_Units_Sold,
        SUM(DISCOUNT) AS Total_Discount_Given,
        SUM(REVENUE) AS Net_Revenue,
        AVG(REVIEW_SCORE) AS Avg_Customer_Satisfaction
    FROM MASTER_SALES_DATA
    GROUP BY CATEGORY, COUNTRY
),

RiskAnalysis AS (
    SELECT 
        CATEGORY,
        SUM(REVENUE) AS Leaked_Revenue
    FROM MASTER_SALES_DATA
    WHERE ORDER_STATUS = 'Cancelled'
    GROUP BY CATEGORY
)

SELECT 
    c.CATEGORY,
    c.COUNTRY,
    c.Total_Orders,
    c.Total_Units_Sold,
    ROUND(c.Net_Revenue, 2) AS Net_Revenue,
    ROUND((c.Net_Revenue / NULLIF(c.Total_Orders, 0)), 2) AS Average_Order_Value,
    ROUND(c.Total_Discount_Given, 2) AS Discount_Investment,
    ROUND(c.Avg_Customer_Satisfaction, 2) AS Customer_Satisfaction_Score,
    ROUND(COALESCE(r.Leaked_Revenue, 0), 2) AS Cancelled_Revenue_Loss
FROM CategoryMetrics c
LEFT JOIN RiskAnalysis r ON c.CATEGORY = r.CATEGORY
ORDER BY Net_Revenue DESC;
