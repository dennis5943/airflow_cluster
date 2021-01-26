service postgresql start
su - postgres -c "createdb airflow"
su - postgres bash -c "psql -c \"CREATE USER airflow WITH PASSWORD '12345678';\""

airflow db reset -y

# create an admin user
airflow users create \
    --username $AIRFLOW_USER \
    -p $AIRFLOW_PASSWORD \
    --firstname airflow \
    --lastname airflow \
    --role Admin \
    --email $AIRFLOW_EMAIL