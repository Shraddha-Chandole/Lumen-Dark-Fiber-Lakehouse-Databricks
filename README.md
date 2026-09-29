# Lumen Telecom - Service Revenue Assurance & Rate Realignment Platform

**Data Engineer | Tech Mahindra | Lumen USA | Nov 2022 - Nov 2025 | 2 Sub-Projects**

### 📌 Business Overview - What I Actually Did
Built data platform for Lumen to identify expired telecom services from Order Forms & Contracts and realign active services to current market rates.

**Flow:** 
Check Service Expiry from Order Forms/Contracts -> Customer-wise Service Analysis -> Calculate MRR, NRR, YRR -> Send Enquiry Emails to Customer & Lumen Client -> Connect with Client & Customer -> For Active Services, Fix Rates at Market Uplift (10%, 20%, 30%)

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

For Each Service for Each Customer:
- **MRR (Monthly Recurring Revenue):** `bandwidth * rate_per_mbps`
- **NRR (Non-Recurring Revenue):** One-time charges, installation, etc.
- **YRR (Yearly Recurring Revenue):** `MRR * 12`
- **Rate Uplift Logic:**
  - 10% Uplift: `new_rate = old_rate * 1.10`
  - 20% Uplift: `new_rate = old_rate * 1.20`
  - 30% Uplift: `new_rate = old_rate * 1.30`

### 🏗️ Architecture - As per Resume (10M+ records/day)

```
Oracle (ORDER_FORMS, CONTRACTS, CUSTOMER_SERVICES, RATE_CARDS)
  -> ADF Incremental -> ADLS Gen2 (Parquet)
  -> Databricks Auto Loader (Bronze)
  -> PySpark Silver (Expiry Flag, MRR/NRR/YRR Calc)
  -> Delta Lake MERGE - SCD2 (Gold) + OPTIMIZE Z-ORDER VACUUM
  -> dbt Models + Airflow DAGs
  -> Enquiry Email Trigger Tables
```

### 📊 Impact
- 10M+ service records processed daily
- Automated expiry detection for Expired Lease
- Enabled Embedded Base revenue uplift by 10/20/30%
- MRR/NRR/YRR reporting for Finance
- 40% Faster Jobs, 30% Storage Optimized, 45% Latency Reduced
- 99.5% Pipeline Reliability

### 🛠️ Tech Stack
- PySpark, Python, Oracle SQL, MySQL
- Azure Databricks, ADF, ADLS Gen2, Synapse
- Delta Lake (Bronze/Silver/Gold), Auto Loader, Delta Live Tables
- Airflow DAGs, Databricks Workflows, dbt
- Partitioning, Caching, Broadcast Joins, AQE, OPTIMIZE, Z-ORDER, VACUUM

### 📂 Repo Structure
- `notebooks/02_silver_expiry_mrr_nrr_yrr.py` - Expiry + MRR/NRR/YRR + 10/20/30%
- `notebooks/04_enquiry_email_trigger.py` - Enquiry Emails to Customer & Lumen

### 📧 Enquiry Email Flow
- Generated tables: `gold.enquiry_expired_lease` & `gold.enquiry_embedded_base`
- Contains: customer_id, service_id, MRR, NRR, YRR, Market Rates
- Business team sends emails to Customer and Lumen Client
- After approval, active services fixed at market rate

### 👩‍💻 Author
Shraddha Chandole - Data Engineer | Ex-Tech Mahindra Lumen | 4.5 Yrs | Immediate Joiner | Pune
Tech: PySpark, Azure Databricks, Delta Lake, ADF, ADLS Gen2, Oracle SQL, dbt, Airflow
Award: 2x Pat on the Back - TechM
