# Enquiry Emails to Customer and Lumen Client
from pyspark.sql.functions import col, lit, current_date

silver_df = spark.read.format("delta").load("/delta/silver/service_financials")

# Expired Lease Enquiry
expired_lease_enquiry = silver_df.filter(col("service_status") == "Expired") \
    .withColumn("enquiry_type", lit("Expired Lease - Renewal Required")) \
    .withColumn("email_cc", lit("lumen_client_team@lumen.com"))

# Embedded Base - Rate Uplift 10/20/30%
embedded_base_enquiry = silver_df.filter(col("service_status") == "Active") \
    .withColumn("enquiry_type", lit("Embedded Base - Rate Uplift 10/20/30%"))

expired_lease_enquiry.write.format("delta").mode("overwrite").save("/delta/gold/enquiry_expired_lease")
embedded_base_enquiry.write.format("delta").mode("overwrite").save("/delta/gold/enquiry_embedded_base")
