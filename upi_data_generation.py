import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker("en_IN")
np.random.seed(42)

# --- Constants ---
NUM_USERS = 2000
NUM_MERCHANTS = 300
NUM_TXNS = 80000

cities = ["Kolkata", "Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad"]
merchant_categories = ["Grocery", "Food", "Travel", "Shopping", "Recharge", "Utilities"]
banks = ["SBI", "HDFC", "ICICI", "Axis", "PNB"]
device_os_options = ["Android", "iOS"]
payment_modes = ["QR", "UPI ID", "Scan & Pay"]
failure_reasons = ["Insufficient Balance", "Incorrect PIN", "Timeout"]
promo_options = ["Yes", "No"]

# --- Users and Merchants ---
users = [f"U{str(i).zfill(5)}" for i in range(1, NUM_USERS + 1)]
merchants = [f"M{str(i).zfill(4)}" for i in range(1, NUM_MERCHANTS + 1)]

# --- Helper: random datetime ---
def random_datetime(start, end):
    delta = end - start
    int_delta = int(delta.total_seconds())
    return start + timedelta(seconds=random.randint(0, int_delta))

# --- Transaction generation ---
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 30)

data = []

for i in range(NUM_TXNS):
    user = random.choice(users)
    merchant = random.choice(merchants)

    base_amount = np.random.normal(400, 150)
    amount = max(50, round(base_amount, 2))

    txn_time = random_datetime(start_date, end_date)
    location = random.choice(cities)
    merchant_city = random.choice(cities)
    device_id = fake.uuid4()
    device_os = random.choice(device_os_options)
    bank = random.choice(banks)
    payment_mode_detail = random.choice(payment_modes)
    status = "Success"
    txn_failure_reason = None
    promotion_applied = random.choice(promo_options)
    is_fraud = 0
    fraud_reason = None
    ip_address = fake.ipv4()

    # ---- FRAUD INJECTION (10%) ----
    if random.random() < 0.10:
        is_fraud = 1
        fraud_type = random.choice([
            "High Amount",
            "Odd Hour",
            "Rapid Transactions",
            "Location Mismatch",
            "Multiple Failures"
        ])

        if fraud_type == "High Amount":
            amount = round(np.random.normal(20000, 5000), 2)

        elif fraud_type == "Odd Hour":
            txn_time = txn_time.replace(hour=random.randint(0, 4))
            amount = round(np.random.normal(15000, 4000), 2)

        elif fraud_type == "Rapid Transactions":
            amount = round(np.random.normal(300, 50), 2)

        elif fraud_type == "Location Mismatch":
            location = random.choice([c for c in cities if c != location])
            merchant_city = random.choice([c for c in cities if c != merchant_city])
            amount = round(np.random.normal(12000, 3000), 2)

        elif fraud_type == "Multiple Failures":
            status = "Failed"
            txn_failure_reason = random.choice(failure_reasons)
            amount = round(np.random.normal(5000, 1500), 2)

        fraud_reason = fraud_type

    data.append([
        f"T{i+1}",
        user,
        txn_time,
        amount,
        merchant,
        merchant_city,
        random.choice(merchant_categories),
        status,
        device_id,
        device_os,
        location,
        bank,
        payment_mode_detail,
        promotion_applied,
        ip_address,
        is_fraud,
        fraud_reason,
        txn_failure_reason
    ])

# --- Columns ---
columns = [
    "transaction_id",
    "user_id",
    "transaction_datetime",
    "amount",
    "merchant_id",
    "merchant_city",
    "merchant_category",
    "transaction_status",
    "device_id",
    "device_os",
    "location",
    "bank_name",
    "payment_mode_detail",
    "promotion_applied",
    "ip_address",
    "is_fraud",
    "fraud_reason",
    "txn_failure_reason"
]

# --- Create DataFrame ---
df = pd.DataFrame(data, columns=columns)

# --- Save CSV ---
path = r"d:/data_analytics/projects/upi fraud detection/upi_transactions_synthetic.csv"
df.to_csv(path, index=False)
print("CSV saved successfully at:", path)
print("Number of rows:", len(df))
print("Columns:", df.columns.tolist())


