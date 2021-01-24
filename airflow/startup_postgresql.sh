service postgresql start
su - postgres -c "createdb airflow"
su - postgres bash -c "psql -c \"CREATE USER airflow WITH PASSWORD '12345678';\""


pg_isready -U postgres

python3 keepalive.py