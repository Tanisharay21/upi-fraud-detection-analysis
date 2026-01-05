# upi-fraud-detection-analysis
Data analytics project detecting fraudulent UPI transactions using pattern analysis and business rules. Includes EDA, fraud pattern discovery, and business recommendations.

1. **Fraud Distribution:**
- Total transactions: 80,000
- Fraud rate: 10.03% (8,022 fraud transactions)
- 98% transactions successful, 2% failed

2. **Temporal Patterns:**
- **Night transactions (1 AM - 5 AM)** show highest fraud rates
- **February** has unusually high fraud activity
- **Daytime transactions** are significantly safer
-
3. **Amount Analysis:**
Transaction Size Fraud Rate
Small (<₹1,000) 2.3% fraud
Medium (₹1,000-5,000) 99.9% fraud
Large (₹5,000-15,000) 100% fraud
Very Large (15k+) 100% fraud

 4. **Category Analysis:**
- All categories show similar fraud rates (~10%)
- No single merchant type, city, or bank stands out
- Fraud is evenly distributed across all categories

#### 5. **Critical Insight:**
**Transaction amount is the strongest fraud indicator**, not merchant type or location.
