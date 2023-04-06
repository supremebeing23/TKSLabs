**LAB03**

## **Task 2.1**

being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/$ mkdir web_server
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/$ cd web_server
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/web_server$ echo "Hello, world!" > index.html
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/web_server$ cd /home/being/TKSLabs/Lab_03/
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/$ `nano Dockerfile`
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03$ `docker build -t apacheweb .`

> [+] Building 100.4s (8/8) FINISHED  => [internal] load build
> definition from Dockerfile                                            
> 1.0s  => => transferring dockerfile: 421B                                                                               0.0s  => [internal] load .dockerignore                                                                                  1.3s  => => transferring context: 2B                                                                                    0.0s  => [internal] load metadata for docker.io/library/ubuntu:latest                                                   1.3s  => [internal] load build context                                                                                  1.0s  => => transferring context: 96B                                                                                   0.0s  => [1/3] FROM docker.io/library/ubuntu:latest@sha256:67211c14fa74f070d27cc59d69a7fa9aeff8e28ea118ef3babc295a0428
> 7.0s  => => resolve docker.io/library/ubuntu:latest@sha256:67211c14fa74f070d27cc59d69a7fa9aeff8e28ea118ef3babc295a0428
> 0.8s  => => sha256:67211c14fa74f070d27cc59d69a7fa9aeff8e28ea118ef3babc295a0428a6d21
> 1.13kB / 1.13kB                     0.0s  => => sha256:7a57c69fe1e9d5b97c5fe649849e79f2cfc3bf11d10bbd5218b4eb61716aebe6
> 424B / 424B                         0.0s  => =>
> sha256:08d22c0ceb150ddeb2237c5fa3129c0183f3cc6f5eeb2e7aa4016da3ad02140a
> 2.30kB / 2.30kB                     0.0s  => => sha256:2ab09b027e7f3a0c2e8bb1944ac46de38cebab7145f0bd6effebfe5492c818b6
> 29.53MB / 29.53MB                   3.7s  => => extracting sha256:2ab09b027e7f3a0c2e8bb1944ac46de38cebab7145f0bd6effebfe5492c818b6
> 1.0s  => [2/3] RUN apt-get update && apt-get install -y apache2                                                        86.6s  => [3/3] COPY web_server/ /var/www/html/                                                                          1.7s  => exporting to image                                                                                             2.1s  => => exporting layers                                                                                            2.0s  => => writing image sha256:7021e10bfeab40c5e0e8e9aaad71f0ce97668937640918124ae1423cf0a3e959
> 0.0s  => => naming to docker.io/library/apacheweb                                                                       0.1s

 

being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03$ 

docker run -p 8080:80 -v /web_server:/var/www/html/ apacheweb



AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message

being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03$ **docker container ls**
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                                   NAMES
3546cde2eadd   apacheweb   "apache2ctl -D FOREG…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   distracted_booth





[labs@labs-vmwarevirtualplatform Lab_03]$ 

     docker run -d -p 3306:3306 --name=mysql -v data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test_db mysql/mysql-server:latest

> Unable to find image 'mysql/mysql-server:latest' locally latest:
> Pulling from mysql/mysql-server 6a4a3ef82cdc: Pull complete 
> 5518b09b1089: Pull complete  b6b576315b62: Pull complete 
> 349b52643cc3: Pull complete  abe8d2406c31: Pull complete 
> c7668948e14a: Pull complete  c7e93886e496: Pull complete  Digest:
> sha256:d6c8301b7834c5b9c2b733b10b7e630f441af7bc917c74dba379f24eeeb6a313
> Status: Downloaded newer image for mysql/mysql-server:latest
> 55d2bc53756bbfcff4426f3af2705e148055aa37b20c898c8e98baa45ba56451


[labs@labs-vmwarevirtualplatform Lab_03]$ `docker exec -it 55d2bc53756b bash`

    bash-4.4# mysql -u root -p
    Enter password: 
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 32
    Server version: 8.0.32 MySQL Community Server - GPL
    
    Copyright (c) 2000, 2023, Oracle and/or its affiliates.
    
    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.
    
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    
    mysql> CREATE USER 'monty'@'localhost' IDENTIFIED BY 'root';
    Query OK, 0 rows affected (0.05 sec)
    
    mysql> GRANT ALL PRIVILEGES ON *.* To 'monty'@'localhost'
        -> WITH GRANT OPTION;
    Query OK, 0 rows affected, 1 warning (0.00 sec)
    
    mysql> CREATE USER 'monty'@'%' IDENTIFIED BY 'root';
    Query OK, 0 rows affected (0.01 sec)
    
    mysql> GRANT ALL PRIVILEGES ON *.* To 'monty'@'%' WITH GRANT OPTION;
    Query OK, 0 rows affected (0.01 sec)



[labs@labs-vmwarevirtualplatform Lab_03]$ `docker run -d --name myadmin --link mysql:db -e PMA_HOST=mysql -p 8080:80 phpmyadmin/phpmyadmin:latest`

> Unable to find image 'phpmyadmin/phpmyadmin:latest' locally latest:
> Pulling from phpmyadmin/phpmyadmin f1f26f570256: Extracting
> [========================>                          ]   15.4MB/31.41MB
> f1f26f570256: Pull complete  ee0a4e40ccac: Pull complete 
> 5ca9fb408faa: Pull complete  5baa808a48ff: Pull complete 
> 6e8d74e4d8ee: Pull complete  fac8e70fcf67: Pull complete 
> b3b7906fb177: Pull complete  cb4935bbeb83: Pull complete 
> c9e00ef337e3: Pull complete  cfe495c8d695: Pull complete 
> dcc3fd107f0c: Pull complete  fe3c587d1f07: Pull complete 
> 677f27d94442: Pull complete  4d778a8cb653: Pull complete 
> 5f0f7b557ecd: Pull complete  6ad259d60f7c: Pull complete 
> 41acd705cbc4: Pull complete  912204d5a7e6: Pull complete  Digest:
> sha256:ed87921184b59f7d8fc85c6a5f041c22758a4d4419c0ee3bac38eb7e133eaed3
> Status: Downloaded newer image for phpmyadmin/phpmyadmin:latest
> docker: Error response from daemon: could not get container for ymsql:
> No such container: ymsql. See 'docker run --help'.
