#啟動postgres -> 確認有無airflow database-> resetdb.sh ->keepalive
#rm -rf /postgresql/data/*

#將postgresql data搬移至指定folder中
python3 /app/scripts/chgDBFolder.py

#確認資料庫中是否已有airflow db，若沒有則重設它
python3 /app/scripts/ResetdbIfNeed.py

python3 keepalive.py