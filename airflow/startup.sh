bash startup_postgresql.sh

airflow webserver -p 8080 & airflow scheduler
airflow worker