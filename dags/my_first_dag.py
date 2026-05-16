from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import requests
import os
from sqlalchemy import create_engine
import logging

default_args = {
    'owner': 'Junaid',
    'start_date': datetime(2026, 5, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# 1. Data Extract Karne Ka Task (With Error Handling)
def extract_retail_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    output_path = "/opt/airflow/dags/raw_retail_data.csv"
    
    try:
        logging.info("Internet se data extract shuru ho raha hai...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Agar internet ya URL ka masla ho to error dega
        
        with open(output_path, "w") as f:
            f.write(response.text)
        logging.info("Data kamyabi se extract ho kar CSV mein save ho gaya hai!")
        
    except requests.exceptions.RequestException as e:
        logging.error(f"DATA EXTRACTION FAILED: Internet ya URL ka masla hai. Error: {e}")
        raise

# 2. Advance Transformation Task
def transform_retail_data():
    input_path = "/opt/airflow/dags/raw_retail_data.csv"
    output_path = "/opt/airflow/dags/clean_retail_data.csv"
    
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError("Raw data file nahi mili!")
            
        df = pd.read_csv(input_path)
        df.fillna({'Age': 0, 'Cabin': 'Unknown'}, inplace=True)
        
        def assign_age_group(age):
            if age == 0: return 'Unknown'
            elif age < 12: return 'Child'
            elif age < 18: return 'Teenager'
            else: return 'Adult'
                
        df['Age_Group'] = df['Age'].apply(assign_age_group)
        df.to_csv(output_path, index=False)
        logging.info("Transformation aur Feature Engineering kamyabi se mukammal!")
        
    except Exception as e:
        logging.error(f"TRANSFORMATION FAILED: Code ya file mein masla hai. Error: {e}")
        raise

# 3. Data Load Karne Ka Task (With Error Handling)
def load_retail_data():
    input_path = "/opt/airflow/dags/clean_retail_data.csv"
    
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError("Clean data file nahi mili!")
            
        logging.info("Postgres database se connect ho raha hai...")
        engine = create_engine('postgresql://airflow:airflow@postgres:5432/airflow')
        
        df = pd.read_csv(input_path)
        df.to_sql('vantage_retail_table', engine, if_exists='replace', index=False)
        logging.info("Saara data Postgres database mein successfully load ho gaya hai!")
        
    except Exception as e:
        logging.error(f"DATABASE LOADING FAILED: Postgres connection ya query ka masla hai. Error: {e}")
        raise

# DAG Structure
with DAG(
    dag_id='vantage_retail_data_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract_raw_data',
        python_callable=extract_retail_data,
    )

    transform_task = PythonOperator(
        task_id='transform_clean_data',
        python_callable=transform_retail_data,
    )

    load_task = PythonOperator(
        task_id='load_to_postgres',
        python_callable=load_retail_data,
    )

    extract_task >> transform_task >> load_task