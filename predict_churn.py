import pandas as pd
import numpy as np
import snowflake.connector
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score

print("🤖 Initializing Predictive Customer Analytics Pipeline...")



SNOWFLAKE_USER = "YOUR_SNOWFLAKE_USERNAME"  
SNOWFLAKE_PASSWORD = "your_snowflake_password_here"           
SNOWFLAKE_ACCOUNT = "jmlnvcs-zf81443"

print("☁️ Pulling records from Snowflake instance for training dataset...")
ctx = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse="COMPUTE_WH",
    database="ECOMMERCE_ANALYTICS_DW",
    schema="RAW"
)

query = "SELECT CATEGORY, QUANTITY, PRICE, DISCOUNT, REVENUE, PAYMENT_METHOD, ORDER_STATUS, REVIEW_SCORE FROM MASTER_SALES_DATA;"
df = pd.read_sql(query, ctx)
ctx.close()
print(f"Data extraction complete. Successfully retrieved {len(df)} rows from cloud storage.")

print("Beginning statistical feature engineering sequence...")

df['IS_CHURNED'] = np.where((df['REVIEW_SCORE'] <= 2) | (df['ORDER_STATUS'] == 'Cancelled'), 1, 0)

# Encode text values to numbers for the math model
le_cat = LabelEncoder()
le_pay = LabelEncoder()
df['CATEGORY_ENC'] = le_cat.fit_transform(df['CATEGORY'])
df['PAYMENT_ENC'] = le_pay.fit_transform(df['PAYMENT_METHOD'])


feature_columns = ['QUANTITY', 'PRICE', 'DISCOUNT', 'REVENUE', 'REVIEW_SCORE', 'CATEGORY_ENC', 'PAYMENT_ENC']
X = df[feature_columns]
y = df['IS_CHURNED']

# Split data: 80% to train the model, 20% to test its accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# Standardize numerical values
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# --- STEP 3: TRAIN THE MACHINE LEARNING MODEL
# ==========================================
print("Training high-performance XGBoost Classifier model...")
model = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate performance metrics
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print("\n================== MODEL EVALUATION SUMMARY ==================")
print(f"Accuracy Score: {accuracy * 100:.2f}%")
print("\nClassification Report Metrics:")
print(classification_report(y_test, y_pred))
print("================================================================")
print("Model training and validation sequence completed successfully.")

