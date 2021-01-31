import os

#/var/lib/postgresql/11/main
src_folder = '/var/lib/postgresql'
data_folder = os.getenv('POSTGRES_DATA').rstrip('/')

cmd_change_cfg = """python3 /app/scripts/fixcfg.py \
    -f /etc/postgresql/11/main/postgresql.conf \
    -s \"data_directory = '/var/lib/postgresql/11/main'\" \
    -r \"data_directory = '{}/postgresql/11/main'\"""".format(data_folder)
print(cmd_change_cfg)
print('修正postgresql.conf:' + str(os.system(cmd_change_cfg)))

if not os.path.isdir(data_folder + '/postgresql'):
    print("資料夾是空的，準備搬移")
else:    
    print("資料夾不是空的，無法轉移")
    print("data_folder:" + data_folder)
    print(os.listdir(data_folder))
    print('啟動postgresql服務:' + str(os.system('service postgresql start')))
    exit()

print('關閉postgresql服務:' + str(os.system('service postgresql stop')))

#cmd_mv = 'mv {}/* {}'.format(src_folder,data_folder)
cmd_mv = 'rsync -rav {} {}'.format(src_folder,data_folder)

print('move folder:' + str(os.system(cmd_mv)))
print('啟動postgresql服務:' + str(os.system('service postgresql start')))