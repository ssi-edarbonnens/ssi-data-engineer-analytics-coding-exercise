# ssi-data-engineer-analytics-coding-exercise
## **SSI Coding Exercise for a Data Engineer role**

Given a raw data source stored in AWS S3, semi-structured (JSON) based on email elements/ threads and email contacts, we want to make it available to query through AWS Athena.
We would like AWS Glue to crawl the raw data and transform it to an enriched format (like Parquet) to be queried by AWS Athena, so a Python/ PySpark script is required to do the transformation jobs and build only one big table.
* You have to extract the data of the referenced tables from Glue Data Catalog in a Dynamic Frame.
* You have to apply transformations on the source tables (pivot arrays lists into rows and joins) and drop unnecessary columns.
* Finally write the data in a format such Apache Parquet that AWS Athena can query and process more efficiently.

***

## Input (Athena SQL query)

```SQL
SELECT DISTINCT *
FROM "test_db"."enricheddata_test_table"
WHERE "recipient_name" = 'John Doe';
```

## Output

recipient_id | author_id | recipient_name | threadurn | content_mail_subject | thread_id | createdat | content_mail_body_text
------------ | --------- | -------------- | --------- | -------------------- | --------- | --------- | --------------
urn:li:person:a1b2c3d4d5 | `urn:li:seat:123456789` | John Doe | urn:li:messagingThread:6234532054298611712 | RE: Testing Stub Profile | I6234554148858486784_1000 | 1486428775329 | Update test v2 complete.
urn:li:person:a1b2c3d4d5 | `urn:li:seat:123456789` | John Doe | urn:li:messagingThread:6234532054298611712 | RE: Testing Stub Profile | I6234554148858486784_1000 | 1486428775129 | Test response complete.

