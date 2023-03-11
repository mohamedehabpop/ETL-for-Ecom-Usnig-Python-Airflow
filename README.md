# Automated ETL for Ecom Usnig Python & Airflow
developed an Automated ETL for an ecommerce using it's Hidden API endpoint and used Airflow to orchestrate the pipeline

The pipeline was built using __Python; Pandas; Hidden API endpoint; AWS S3; Airflow;  Docker__



## How it works
### Data pipeline (sghut_ETL.py)
- __[Extract]:__ call [Data endpoint] to get the products data represented in the website
- __[Transform]:__ do some transformations like: renaming columns, cleaning data, changing data types and represnting data in a dataframe 
- __[Load]:__ load the final data and AWS S3 data lake

###  Workflow pipeline (sghut_dag.py)
- __[DAG]:__ created simple DAG to schedule running  the ETL



## Running project
