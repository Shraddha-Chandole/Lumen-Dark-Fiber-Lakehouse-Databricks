# Expired Lease & Embedded Base - MRR, NRR, YRR Calculation
from pyspark.sql.functions import current_date, datediff, when, col, count, sum, round

bronze_df = spark.read.format("delta").load("/delta/bronze/customer_services")

# Expiry Check - Expired Lease vs Embedded Base
silver_df = bronze_df.withColumn("service_status",
    when(col("service_end_date") < current_date(), "Expired")
    .otherwise("Active"))

# MRR, NRR, YRR per service per customer
silver_financial_df = silver_df \
    .withColumn("MRR", col("bandwidth_mbps") * col("current_rate_per_mbps")) \
    .withColumn("NRR", col("one_time_installation_charge") + col("other_charges")) \
    .withColumn("YRR", col("MRR") * 12) \
    .withColumn("MRR_10_percent_uplift", round(col("MRR") * 1.10, 2)) \
    .withColumn("MRR_20_percent_uplift", round(col("MRR") * 1.20, 2)) \
    .withColumn("MRR_30_percent_uplift", round(col("MRR") * 1.30, 2))

silver_financial_df.write.format("delta").mode("overwrite").save("/delta/silver/service_financials")
