airflow db init

# create an admin user
airflow users create \
    --username $AIRFLOW_USER \
    -p $AIRFLOW_PASSWORD \
    --firstname airflow \
    --lastname airflow \
    --role Admin \
    --email $AIRFLOW_EMAIL