# airflow_cluster
Airflow 2.0 Docker + Swarm佈署

部署基礎服務，指令:docker stack deploy -c docker-compose-base-service.yml airflow_base

會佈署三項服務

1.rabbitmq

2.adminer

3.postgres_db


