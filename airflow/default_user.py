from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
import os

# Get environment variables
USER = os.getenv('AIRFLOW_USER')
PASSWORD = os.environ.get('AIRFLOW_PASSWORD')
EMAIL = os.environ.get('AIRFLOW_EMAIL')

user = PasswordUser(models.User())
user.username = USER
user.email = EMAIL
user.password = PASSWORD
user.superuser = True
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()