import os
import subprocess

cmd_check_user = 'psql -h localhost -U airflow -c "select current_user;" airflow'

print(os.system(cmd_check_user))

if os.system(cmd_check_user) != 0:
    print('初始化資料庫')
    #os.popen('bash /app/resetdb.sh')
    p = subprocess.Popen(['bash','/app/scripts/resetdb.sh'])    
    p.communicate() #now wait plus that you can send commands to process
    print("初始化資料庫-完成")
else:
    print('資料庫已存在，略過此步驟')

