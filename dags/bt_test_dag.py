from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 5),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
}

customer_args = {
    "customer": "bt"
}

# Maybe move time intervals to a general ETLephant config?
# Mintues
interval = timedelta(minutes=5)
# Hourly
# interval = timedelta(hours=1)
# # Daily
# interval = timedelta(days=1)

# Define the success callback function

dag = DAG(
    'bt_dag',
    default_args=default_args,
    description='A simple DAG to run etl_test.py',
    schedule_interval=interval,
    catchup=False,
)

def callable():
    etl.run(customer_args)


run_this = PythonOperator(
    task_id='etl',
    python_callable=callable,
    dag=dag,
)

# Define the task dependencies