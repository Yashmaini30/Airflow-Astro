from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

## Task 1
def preprocess_data():
    print("Preprocessing data")

def train_model():
    print("Training model")

## Task 2
def evaluate_model():
    print("Evaluating model")

## Define the DAG

with DAG(
    dag_id="ml_pipeline",
    start_date=datetime(2025,3,26),
    schedule_interval='@daily'
) as dag:
    
    ## define the task
    preprocess=PythonOperator(task_id="preprocess_task",python_callable=preprocess_data)
    train=PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate=PythonOperator(task_id="evaluate_task",python_callable=evaluate_model)

    ## set dependencies
    preprocess >> train >> evaluate