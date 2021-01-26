# airflow_cluster
Airflow 2.0 Docker + Swarm佈署

部署基礎服務，指令:docker stack deploy -c docker-compose-base-service.yml airflow_base

(會佈署三項服務 1.rabbitmq  2.adminer 3.postgres_db)

建立資料庫，指令:docker exec [postgres_db container ID] bash resetdb.sh

RabbitMQ :http://[airflow_base_RabbitMQ]:15672/#/

設定User:airflow:[password]

產生Host:airflow，並把airflow用戶加進host中

部署airflow cluster:docker stack deploy -c docker-compose.yml airflow_cluster
