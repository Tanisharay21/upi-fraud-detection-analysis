# Fraud Detection System - UPI Transaction Analysis

Project Overview
A data-driven fraud detection system that identifies fraudulent UPI transactions using pattern analysis and business rules. The system combines data exploration, fraud pattern discovery, and automated risk scoring to prevent financial losses.

## Key Findings from 80,000 Transactions Analysis

### **Fraud Distribution:**
- **Total transactions**: 80,000
- **Fraud rate**: 10.05% (8,040 fraud transactions)
- **Status analysis**: 96% transactions successful, 4% failed
- **Critical insight**: Failed transactions strongly correlate with fraud attempts

### **Temporal Patterns:**
- **Night transactions (1 AM - 5 AM)**: Highest fraud rates
- **January and April**: Unusually high fraud activity month
- **Daytime transactions**: Significantly safer
- **Business hours vs. after-hours**: Clear fraud pattern differences

### **Amount Analysis - The Strongest Fraud Indicator:**
| Transaction Size      | Fraud Rate | Risk Level |
|-----------------------|------------|------------|
| Small (<₹1,000)       | 0%         | Low        |
| Medium (₹1,000-5,000) | 5.6%       | Extreme    |
| Large (₹5,000-15,000) | 62.1%      | Extreme    |
| Very Large (15k+)     | 71%        | Extreme    |

### **Category Analysis:**
- All merchant types show similar fraud rates (~10%)
- No single city or bank stands out as particularly risky
- Fraud is evenly distributed across all categories
- **Critical Insight**: Transaction amount is the strongest fraud indicator, not merchant type or location

## ⚙️ System Features

### **Risk Scoring Engine:**
- **Score Range**: 0-100 (higher = more risky)
- **Data-Driven Rules**: All thresholds based on actual fraud patterns
- **Explainable Decisions**: Clear reasons provided for each risk assessment

### **Automated Actions:**
| Risk Score |                 Action                |          Description              |
|------------|---------------------------------------|--------------------------------=--|
| ≥50	       | ESCALATE TO FRAUD TEAM	               | Immediate investigation required  |
| 43-49	     | STRONG VERIFICATION (OTP + Biometric) | Enhanced authentication required  |
| 20-42	     | FLAG FOR REVIEW	                     | Manual review needed              |
| <20	       | AUTO APPROVE	                         | Low risk, instant approval        |

### **High-Risk Patterns Detected:**
1. **Night + Large Amount**: 78% fraud rate
2. **Location Mismatch + >₹3k**: 72.7% fraud rate  
3. **Weekend Large Transactions**: 67.6% fraud rate
4. **Failed Transaction Status**: 54.2% fraud rate


## Tested  Different Scenarios:**

- Tested different transaction patterns
- Shows all risk thresholds in action
- Demonstrates real-world fraud scenarios

## Business Impact

### **For Financial Institutions:**
- **Reduced fraud losses** by catching 70%+ fraud patterns automatically
- **Improved operational efficiency** - focus resources on high-risk cases
- **Regulatory compliance** with documented risk assessments

### **For Customers:**
- **Seamless experience** for low-risk transactions
- **Enhanced security** for suspicious activities
- **Transparent process** with clear risk explanations

## 📈 Actionable Recommendations

### **Immediate Actions:**
1. **Implement amount-based blocking**: Auto-decline transactions >₹5,000 at night
2. **Enhance location verification**: Flag location mismatches with amounts >₹3,000
3. **Monitor February closely**: Increase vigilance during high-fraud month

### **System Improvements:**
1. **Real-time monitoring**: Flag transactions crossing multiple risk thresholds
2. **Customer profiling**: Learn normal spending patterns for each user
3. **Dynamic thresholds**: Adjust based on time, location, and customer history

