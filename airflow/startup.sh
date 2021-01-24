service postgresql start
su - postgres -c "createdb airflow"
su - postgres bash -c "psql -c \"CREATE USER airflow WITH PASSWORD '12345678';\""

cp -f airflow.cfg /root/airflow/airflow.cfg

airflow db reset -y

##python default_user.py

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