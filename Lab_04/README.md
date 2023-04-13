# Завдання 3. Запустити базу даних MySQL та PHPMyAdmin у Docker контейнерах” Лабораторної роботи №3 використовуючи Docker Compose
### Запуск консонльного текстового редаткора і створення docker-compose.yml
```sh
nano docker-compose.yml
```
### Інструкції docker-compose.yml
```sh
version: '3.3'

services:
  db: 
    image: mysql:latest
    container_name: mysql
    environment:
       MYSQL_DATABASE: db
       MYSQL_ROOT_USER: root
       MYSQL_ROOT_PASSWORD: 321
       MYSQL_ROOT_HOST: localhost
    ports:
      # <Port exposed>
      - '3306:3306'
    expose:
      # Opens port 3306 on the container
      - '3306'
      # Where our data will be persisted
    volumes:
      - /data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin:latest   
    environment:
      PMA_HOST: mysql
    ports:
      - '8080:80'
    expose:
      - '8080'
```
### Запуск сервісів з допомогою створеного docker-compose.yml
```sh
docker compose up
[+] Running 2/2
 ✔ Container lab_04-phpmyadmin-1  Created                                                                              1.1s
 ✔ Container mysql                Created                                                                              1.1s
Attaching to lab_04-phpmyadmin-1, mysql
mysql                | 2023-04-06 13:05:33+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.32-1.el8 started.
mysql                | 2023-04-06 13:05:33+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql                | 2023-04-06 13:05:33+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.32-1.el8 started.
lab_04-phpmyadmin-1  | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.20.0.3. Set the 'ServerName' directive globally to suppress this message
mysql                | '/var/lib/mysql/mysql.sock' -> '/var/run/mysqld/mysqld.sock'
lab_04-phpmyadmin-1  | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.20.0.3. Set the 'ServerName' directive globally to suppress this message
lab_04-phpmyadmin-1  | [Thu Apr 06 13:05:33.983851 2023] [mpm_prefork:notice] [pid 1] AH00163: Apache/2.4.56 (Debian) PHP/8.1.17 configured -- resuming normal operations
lab_04-phpmyadmin-1  | [Thu Apr 06 13:05:33.983919 2023] [core:notice] [pid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
mysql                | 2023-04-06T13:05:34.199017Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql                | 2023-04-06T13:05:34.200320Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.32) starting as process 1
mysql                | 2023-04-06T13:05:34.207067Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql                | 2023-04-06T13:05:35.651473Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql                | 2023-04-06T13:05:37.879643Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql                | 2023-04-06T13:05:37.879773Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql                | 2023-04-06T13:05:37.920553Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql                | 2023-04-06T13:05:37.939124Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
mysql                | 2023-04-06T13:05:37.940095Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.32'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
```

# Завдання 4. Використовуючи відому для Вас мову програмування реалізуйте два програмних сервіси та контейнеризуйте їх:

### Лістинг коду 1-го сервісу
```sh
import time
import datetime

output_dir = '/log'

while True:
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(f'{output_dir}/{current_time}.txt', 'a') as f:
        f.write(current_time + '\n')


    time.sleep(10)

```
### Dockerfile для створення контейнера з 1-шим сервісом
```sh
# Використовуємо офіційний образ Python з Docker Hub
FROM python:3
ADD logger.py /
# Запускаємо програму
CMD [ "python", "./logger.py" ]
```

### Створення image. Запуск контейнера
``` sh
$ docker build -t log .

$ docker run -d --name logger -v ./time:/log log
```
### Перелік прив'язаних томів (volumes)
``` sh
$docker volume ls
DRIVER    VOLUME NAME
local     time
```
### Перелік запущених контейнерів
``` sh
$ docker ps
CONTAINER ID   IMAGE     COMMAND                CREATED              STATUS              PORTS     NAMES
e406c08a52a5   log       "python ./logger.py"   About a minute ago   Up About a minute    logger
```
### Перевірка роботи сервісу в запущеному контейнері
``` sh
$ docker exec -it logger bash
root@e406c08a52a5:/# ls
bin  boot  dev  etc  home  lib  lib64  log  logger.py  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@e406c08a52a5:/# cd log
root@e406c08a52a5:/log# more log.txt
2023-04-13 06:54:44
2023-04-13 06:54:54
2023-04-13 06:55:04
2023-04-13 06:55:14
```
### Лістинг коду 2-го сервісу
```sh
import time
import os
def print_logs():
    for filename in os.listdir('/log'):
        if filename.endswith('.txt'):
            with open('/log/' + filename, 'r') as f:
                file_content = f.read()
            print('Filename:', filename, '\nContent:\n', file_content)
def main():
    print_logs()
while True:
    main()
    time.sleep(5)
````


### Dockerfile для створення контейнера з 2-гим сервісом
```sh
# Використовуємо офіційний образ Python з Docker Hub
FROM python:3
ADD logger2.py /
CMD [ "python", "./logger2.py" ]
```
### Запуск контейнера з другим сервісом
``` sh
$ docker run -d --name logchecker --volumes-from logger logchecker
```
### Перелік запущених контейнерів
``` sh docker ps
CONTAINER ID   IMAGE        COMMAND                 CREATED         STATUS          PORTS     NAMES
e8e401e7f3ed   logchecker   "python ./logger2.py"   3 minutes ago   Up 3 minutes              logchecker
e406c08a52a5   log          "python ./logger.py"    2 hours ago     Up 12 minutes             logger
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_04/time_checker$ docker volume ls
DRIVER    VOLUME NAME
local     time
```
### Перевірка роботи сервісу в запущеному контейнері
``` sh
$ docker logs  logchecker
Filename: /log/log.txt
Content:
 2023-04-13 08:51:53


Filename: /log/log.txt
Content:
 2023-04-13 08:51:53
2023-04-13 08:52:03


Filename: /log/log.txt
Content:
 2023-04-13 08:51:53
2023-04-13 08:52:03
2023-04-13 08:52:13
```
### Створення файлу docker-compose.yml для запуску сервісів з допомогою docker compose
```sh
version: '3.3'

services:
  logger:
    image: log
    container_name: logger_compose
    volumes:
      - ./time:/log

  logchecker:
    image: logchecker  
    container_name: logchecker_compose
    volumes:
      - ./time:/log
 
volumes:
  time:
    external: true
```
### Запуск контейнерів з допомогою docker compose
``` sh
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_04/time_checker$ docker compose up
[+] Running 2/0
 ✔ Container logchecker_compose  Created                                                                          0.0s
 ✔ Container logger_compose      Created                                                                          0.0s
Attaching to logchecker_compose, logger_compose

logchecker_compose  | Filename: /log/log.txt
logchecker_compose  | Content:
logchecker_compose  |  2023-04-13 10:44:13
logchecker_compose  |
logchecker_compose  | Filename: /log/log.txt
logchecker_compose  | Content:
logchecker_compose  |  2023-04-13 10:44:13
logchecker_compose  | 2023-04-13 10:44:23
```
### Запуск контейнерів з допомогою docker compose у фоновому режимі
```sh
$ docker compose up --build -d
[+] Running 2/2
 ✔ Container logchecker_compose  Started                                                                                                                          14.0s
 ✔ Container logger_compose      Started                                                                                                                          13.8s
 ```
 ### Перевірка роботи 1-го сервісу
```sh
$ docker ps
CONTAINER ID   IMAGE        COMMAND                 CREATED          STATUS         PORTS     NAMES
ab63eecd9609   log          "python ./logger.py"    16 seconds ago   Up 3 seconds             logger_compose
71b1b29ca7ef   logchecker   "python ./logger2.py"   16 seconds ago   Up 2 seconds             logchecker_compose
r$ docker exec -it logger_compose bash
root@ab63eecd9609:/# ls
bin  boot  dev  etc  home  lib  lib64  log  logger.py  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@ab63eecd9609:/# cd log
root@ab63eecd9609:/log# more log.txt
2023-04-13 11:01:06
2023-04-13 11:01:16
2023-04-13 11:01:26
2023-04-13 11:01:36
root@ab63eecd9609:/log# exit
exit
```
 ### Перевірка роботи 2-го сервісу
```sh
$ docker compose logs
logchecker_compose  | Filename: /log/log.txt
logchecker_compose  | Content:
logchecker_compose  |
logchecker_compose  |
logchecker_compose  | Filename: /log/log.txt
logchecker_compose  | Content:
logchecker_compose  |
logchecker_compose  | Filename: /log/log.txt
logchecker_compose  | Content:
logchecker_compose  |  2023-04-13 11:01:06
logchecker_compose  |
```
### Зупинка та видалення контейнерів
```sh
docker compose down
[+] Running 3/3
 ✔ Container logchecker_compose  Removed                                                                                                                          11.7s
 ✔ Container logger_compose      Removed                                                                                                                          11.9s
 ✔ Network time_checker_default  Removed                                                                                                                          0.8s
  ```
  
 ### Перевірка роботи контейнера з 1-шим сервісом 
 ```sh
  $ docker exec -it logger1 bash

root@0c1a78ce30fd:/log# ls
'2023-04-13 11:28:35.txt'  '2023-04-13 11:29:15.txt'  '2023-04-13 11:29:55.txt'   log_dockerfile_ver1.txt
'2023-04-13 11:28:45.txt'  '2023-04-13 11:29:25.txt'  '2023-04-13 11:30:05.txt'
'2023-04-13 11:28:55.txt'  '2023-04-13 11:29:35.txt'  '2023-04-13 11:30:15.txt'
'2023-04-13 11:29:05.txt'  '2023-04-13 11:29:45.txt'   log.txt
root@0c1a78ce30fd:/log# ls
'2023-04-13 11:28:35.txt'  '2023-04-13 11:29:15.txt'  '2023-04-13 11:29:55.txt'   log.txt
'2023-04-13 11:28:45.txt'  '2023-04-13 11:29:25.txt'  '2023-04-13 11:30:05.txt'   log_dockerfile_ver1.txt
'2023-04-13 11:28:55.txt'  '2023-04-13 11:29:35.txt'  '2023-04-13 11:30:15.txt'
'2023-04-13 11:29:05.txt'  '2023-04-13 11:29:45.txt'  '2023-04-13 11:30:25.txt'

root@0c1a78ce30fd:/log# exit
exit
$ docker stop logger1
logger1
```
 ### Перевірка роботи контейнера з 2-гим сервісом 
```sh
$ docker build -t checker .
[+] Building 4.1s (7/7) FINISHED

$ docker run --name checker -d --volumes-from logger1 checker
5189304cd51d2ada978d74dc14a84a9c7ea8b4d865dddaa53edb382e7efcc2e9


$ docker logs -n 20 checker
2023-04-13 10:28:41
2023-04-13 10:28:51
2023-04-13 10:29:01
2023-04-13 10:29:11
2023-04-13 10:29:21
2023-04-13 10:29:31
2023-04-13 10:29:41
2023-04-13 10:29:51
```
  
  
  
