# Setup Guide

## Prerequisites
- AWS Account
- S3 Buckets for staging and data warehouse
- AWS Glue, Athena, and QuickSight permissions

## Steps

### 1. Upload Data to S3
1. Create an S3 bucket for staging data.
2. Upload your Spotify data files to the bucket.

### 2. Set Up AWS Glue Jobs
1. Create a new Glue job using the provided `etl_script.py` and `glue_job_config.json`.
2. Run the Glue job to transform and load data.

### 3. Run AWS Glue Crawler
1. Create a Glue Crawler to catalog the transformed data.
2. Run the crawler to update the Glue Data Catalog.

### 4. Query Data with Amazon Athena
1. Open Athena and configure the data source to use the Glue Data Catalog.
2. Run sample queries from `athena_queries/sample_queries.sql`.

### 5. Visualize Data with QuickSight
1. Set up QuickSight and connect to the Athena data source.
2. Create dashboards and visualizations.
