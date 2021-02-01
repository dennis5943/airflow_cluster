# airflow_cluster
Airflow 2.0 Docker + Swarm佈署

佈署

docker stack deploy -c docker-compose.yml airflow_cluster


移除佈署

docker stack rm airflow_cluster