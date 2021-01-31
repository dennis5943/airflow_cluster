#啟動postgres -> 確認有無airflow database-> resetdb.sh ->keepalive
#rm -rf /postgresql/data/*

python3 /app/tmp/chgDBFolder.py
python3 /app/scripts/ResetdbIfNeed.py

python3 keepalive.py