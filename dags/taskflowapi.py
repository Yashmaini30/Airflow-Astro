"""
Apache Airflow TaskFlow API which allows you to create
tasks using Python decorators like @task. Thi is a cleaner and more 
intuitive way of writing without needing to manually use the 
operatord likepython operator. 
"""

from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import math

## define the DAG

with DAG(
    dag_id="math_seq_dag_with_taskflow_api",
    schedule_interval="@daily",
    start_date=datetime(2024, 3, 27),
    catchup=False,
) as dag:
    
    ## task 1. start with initial number
    @task
    def  start_numbers():
        initial_number = 5
        print(f"Starting with {initial_number}")
        return initial_number
    
    ## task 2. add 5 to the initial number
    @task
    def add_five(initial_number):
        new_number = initial_number + 5
        print(f"Added 5: {initial_number} + 5 = {new_number}")
        return new_number
    
    ## task 3. multiply both numbers together
    @task
    def multiply_numbers(new_number1, new_number2):
        result = new_number1 * new_number2
        print(f"Multiplied numbers: {new_number1} * {new_number2} = {result}")
        return result
    
    ## task 4. subtract 10 from the result of task 3
    @task
    def subtract_ten(result):
        new_result = result - 10
        print(f"Subtracted 10: {result} - 10 = {new_result}")
        return new_result
    
    ## task 5. take square root of the result of task 4
    @task
    def square_root(new_result):
        result = math.sqrt(new_result)
        print(f"Square root: sqrt({new_result}) = {result}")
        return result
    
    ## set the dependencies
    start_valuue=start_numbers()
    added_value=add_five(start_valuue)
    multiply_value=multiply_numbers(added_value, added_value)
    subtract_value=subtract_ten(multiply_value)
    square_value=square_root(subtract_value)
