service postgresql start
su - postgres -c "createdb airflow"
airflow db init

# create an admin user
airflow users create \
    --username $AIRFLOW_USER \
    -p $AIRFLOW_PASSWORD \
    --firstname airflow \
    --lastname airflow \
    --role Admin \
    --email $AIRFLOW_EMAIL

airflow webserver -p 8080 & airflow scheduler
airflow worker