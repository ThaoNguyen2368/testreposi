from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Hàm Python sẽ chạy trong pipeline của bạn
def my_pipeline_function():
    print("Đang chạy pipeline...")

# Định nghĩa DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_daily_pipeline',  # Tên DAG
    default_args=default_args,
    description='DAG chạy pipeline mỗi ngày lúc 10h sáng',
    schedule_interval='0 10 * * *',  # Lịch trình: 10h sáng mỗi ngày
    start_date=datetime(2025, 4, 5),  # Ngày bắt đầu (có thể thay đổi)
    catchup=False,  # Không cần chạy các lần trước đó khi DAG mới được kích hoạt
)

# Tạo các tác vụ (tasks)
start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

pipeline_task = PythonOperator(
    task_id='run_pipeline',
    python_callable=my_pipeline_function,
    dag=dag,
)

# Sắp xếp các tác vụ
start_task >> pipeline_task
