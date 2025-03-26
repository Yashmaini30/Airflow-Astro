"""

We'll define the DAG where the task are as follows:

1. Task 1: Start with two numbers
2. Task 2: Add 5 to the both numbers
3. Task 3: Multiply both numbers together
4. Task 4. Subtract 10 from the result of Task 3
5. Task 5: take square root of the result of Task 4

"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import math

# Define functions
def start_numbers(**context):
    num1, num2 = 5, 10
    context["ti"].xcom_push(key="num1", value=num1)
    context["ti"].xcom_push(key="num2", value=num2)
    print(f"Starting with {num1} and {num2}")
    return num1, num2

def add_five(**context):
    ti = context["ti"]
    num1 = ti.xcom_pull(task_ids="start_task", key="num1")
    num2 = ti.xcom_pull(task_ids="start_task", key="num2")

    num1 += 5
    num2 += 5
    ti.xcom_push(key="num1", value=num1)
    ti.xcom_push(key="num2", value=num2)
    
    print(f"Added 5: num1={num1}, num2={num2}")
    return num1, num2

def multiply_numbers(**context):
    ti = context["ti"]
    num1 = ti.xcom_pull(task_ids="add_five_task", key="num1")
    num2 = ti.xcom_pull(task_ids="add_five_task", key="num2")

    result = num1 * num2
    ti.xcom_push(key="result", value=result)

    print(f"Multiplied numbers: {num1} * {num2} = {result}")
    return result

def subtract_ten(**context):
    ti = context["ti"]
    num = ti.xcom_pull(task_ids="multiply_task", key="result")

    result = num - 10
    ti.xcom_push(key="result", value=result)

    print(f"Subtracted 10: {num} - 10 = {result}")
    return result

def square_root(**context):
    ti = context["ti"]
    num = ti.xcom_pull(task_ids="subtract_task", key="result")

    result = math.sqrt(num)
    ti.xcom_push(key="result", value=result)

    print(f"Square root: sqrt({num}) = {result}")
    return result

# Define DAG
with DAG(
    dag_id="simple_math_dag",
    schedule_interval="@daily",
    start_date=datetime(2024, 3, 25),
    catchup=False,
) as dag:

    start_task = PythonOperator(
        task_id="start_task",
        python_callable=start_numbers,
        provide_context=True,
    )

    add_five_task = PythonOperator(
        task_id="add_five_task",
        python_callable=add_five,
        provide_context=True,
    )

    multiply_task = PythonOperator(
        task_id="multiply_task",
        python_callable=multiply_numbers,
        provide_context=True,
    )

    subtract_task = PythonOperator(
        task_id="subtract_task",
        python_callable=subtract_ten,
        provide_context=True,
    )

    sqrt_task = PythonOperator(
        task_id="sqrt_task",
        python_callable=square_root,
        provide_context=True,
    )

    # Define task dependencies
    start_task >> add_five_task >> multiply_task >> subtract_task >> sqrt_task
