from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import lookupdate_test

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
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
    'lookupdate_dag',
    default_args=default_args,
    description='A simple DAG to run lookupdate_test.py',
    schedule_interval=interval,
)

def callable():
    lookupdate_test.run()



run_this = PythonOperator(
    task_id='lookupdate_test',
    python_callable=callable,
    dag=dag,
)

# Define the task dependencies
run_this