# Lumen Telecom - Service Revenue Assurance & Rate Realignment Platform
**Data Engineer | Tech Mahindra | Lumen USA | Nov 2022 - Nov 2025 | 2 Sub-Projects**

### 📌 Business Overview - What I Actually Did
Built data platform for Lumen to identify expired telecom services from Order Forms & Contracts and realign active services to current market rates.

**Flow:** Check Service Expiry from Order Forms/Contracts -> Customer-wise Service Analysis -> Calculate MRR, NRR, YRR -> Send Enquiry Emails to Customer & Lumen Client -> Connect with Client & Customer -> For Active Services, Fix Rates at Market Uplift (10%, 20%, 30%)

### 🔹 Two Sub-Projects I Worked On

**1. Expired Lease Project:**
- Identify services where `service_end_date < current_date`
- Calculate revenue at risk and pending renewals
- Trigger enquiry emails to customers for expired services

**2. Embedded Base Project:**
- For Active services, analyze if current rate is below market rate
- Realignment to market standard: Calculate rate uplift at 10%, 20%, 30%
- Fix services at new market rate after customer & client approval

### 🧮 Financial Calculations I Implemented

**For Each Service for Each Customer:**
- **MRR (Monthly Recurring Revenue):** `bandwidth * rate_per_mbps`
- **NRR (Non-Recurring Revenue):** One-time charges, installation, etc.
- **YRR (Yearly Recurring Revenue):** `MRR * 12`
- **Rate Uplift Logic:**
    - 10% Uplift: `new_rate = old_rate * 1.10`
    - 20% Uplift: `new_rate = old_rate * 1.20`
    - 30% Uplift: `new_rate = old_rate * 1.30`
    - Decision based on market_rate_card comparison

### 🏗️ Architecture - As per Resume (10M+ records/day)
