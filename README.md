# UPI Fraud Detection System – Transaction Risk Analysis (Python)

## Project Overview
This project builds a **rule-based fraud detection and risk scoring system** using analysis of **80,000 UPI transactions**.

Instead of jumping straight to machine learning, the focus is on:
- Understanding **fraud behavior**
- Identifying **high-risk transaction patterns**
- Translating insights into **clear business rules**

This mirrors how real payment systems design fraud controls before (or alongside) ML models.

---

## Dataset Summary
- Total transactions: **80,000**
- Fraudulent transactions: **8,040**
- Overall fraud rate: **10.05%**
- Transaction status:
  - 96% successful
  - 4% failed

> The dataset is **synthetic** but designed to simulate realistic UPI transaction behavior.

---

## Key Fraud Insights

### 1. Transaction Status & Fraud
- **54% of failed transactions are fraudulent**
- Failed transactions are not noise — they often indicate fraud attempts being blocked

**Business Insight:**  
Transaction failure itself is a strong fraud signal.

---

### 2. Temporal Patterns
- **Highest fraud activity between 1 AM – 5 AM**
- **January and April** show elevated fraud levels
- Daytime transactions are significantly safer

**Real-world parallel:**  
Banks apply stricter checks during low-activity hours.

---

### 3. Amount-Based Risk (Strongest Indicator)
| Transaction Amount | Fraud Rate |
|-------------------|-------------|
| < ₹1,000          | 0%          |
| ₹1,000 – ₹5,000   | 5.6%        |
| ₹5,000 – ₹15,000  | 62.1%       |
| > ₹15,000         | 71.0%       |

**Critical Insight:**  
Fraud is overwhelmingly concentrated in **high-value transactions**.

---

### 4. Category & Location Analysis
- Merchant categories show similar fraud rates (~10%)
- No single city or bank dominates fraud activity
- Device type and payment method have minimal standalone impact

**Conclusion:**  
Fraud depends more on **transaction context + behavior** than surface-level categories.

---

## High-Risk Fraud Patterns Identified
| Pattern                             | Fraud Rate  |
|-------------------------------------|-------------|
| Late-night + Large Amount           | 78%         |
| Location mismatch + Amount > ₹3,000 | 72.7%       |
| Weekend large transactions          | 67.6%       |
| Failed transaction status           | 54.2%       |

These patterns closely resemble **real-world fraud rule engines**.

---

## Risk Scoring System

### Risk Score: 0 – 100
(Higher score = higher fraud risk)

Scores are calculated using **data-driven rules** derived from observed fraud rates.

### Automated Actions
| Risk Score | Action                                |
|------------|---------------------------------------|
| ≥ 50       | Escalate to fraud team                |
| 43 – 49    | Strong verification (OTP + biometric) |
| 20 – 42    | Flag for manual review                |
| < 20       | Auto-approve                          |

Each decision includes **explainable reasons**, ensuring transparency.

---

## System Features
- Rule-based fraud detection
- Explainable risk scoring
- Behavioral pattern analysis
- Scenario testing across different transaction types
- Business-aligned decision thresholds

---

## Business Value

### For Payment Platforms
- Early detection of high-risk transactions
- Reduced manual review workload
- Clear audit trail for compliance and investigations

### For Customers
- Faster approvals for low-risk transactions
- Stronger security for suspicious activity
- Transparent and predictable fraud checks

---

## Tools & Techniques
- Python (pandas, numpy)
- Exploratory Data Analysis (EDA)
- Feature engineering
- Behavioral pattern detection
- Rule-based decision systems
- Risk scoring logic

---

## Key Takeaway
This project demonstrates **how fraud detection actually starts in industry**:
not with black-box models, but with **data-driven rules, behavioral insights, and explainable decisions**.

It shows the ability to convert raw transaction data into **practical fraud controls**.
