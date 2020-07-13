# ssi-data-engineer-analytics-coding-exercise
SSI Coding Exercise for a Data Engineer role

Given a raw data source stored in AWS S3, semi-structured (JSON) based on email elements/ threads and email contacts, we want to make it available to query through AWS Athena.
We would like AWS Glue to crawl the raw data and transform it to an enriched format (like Parquet) to be queried by AWS Athena, so a Python/ PySpark script is required to do the transformation jobs and build only one big table.
* You have to extract the data of the referenced tables from Glue Data Catalog in a Dynamic Frame.
* You have to apply transformations on the source tables (pivot arrays lists into rows and joins) and drop unnecessary columns.
* Finally write the data in a format such Apache Parquet that AWS Athena can query and process more efficiently.
