from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.extract import main as extract_main
from scripts.transform import transform_data
from scripts.store import main as store_main

# Setting up the default parameters for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Defining the DAG structure
with DAG(
    dag_id='automated_etl_dag',
    default_args=default_args,
    description='Automated ETL pipeline for articles with extract, transform, and store phases.',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:

    # Define tasks using PythonOperator
    extract_task = PythonOperator(
        task_id='extract_articles',
        python_callable=extract_main,
        dag=dag
    )

    transform_task = PythonOperator(
        task_id='transform_articles',
        python_callable=transform_data,
        provide_context=True,
        op_kwargs={'articles': '{{ ti.xcom_pull(task_ids="extract_articles") }}'},
        dag=dag
    )

    store_task = PythonOperator(
        task_id='store_articles',
        python_callable=store_main,
        provide_context=True,
        op_kwargs={'articles': '{{ ti.xcom_pull(task_ids="transform_articles") }}'},
        dag=dag
    )

    # Set task dependencies
    extract_task >> transform_task >> store_task
