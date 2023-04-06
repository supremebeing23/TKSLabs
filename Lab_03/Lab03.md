LAB03
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/$ mkdir web_server
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/$ cd web_server
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/web_server$ echo "Hello, world!" > index.html
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/web_server$ cd /home/being/TKSLabs/Lab_03/
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03/$ nano Dockerfile
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03$ docker build -t apacheweb .
[+] Building 100.4s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                                                               1.0s
 => => transferring dockerfile: 421B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  1.3s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                   1.3s
 => [internal] load build context                                                                                  1.0s
 => => transferring context: 96B                                                                                   0.0s
 => [1/3] FROM docker.io/library/ubuntu:latest@sha256:67211c14fa74f070d27cc59d69a7fa9aeff8e28ea118ef3babc295a0428  7.0s
 => => resolve docker.io/library/ubuntu:latest@sha256:67211c14fa74f070d27cc59d69a7fa9aeff8e28ea118ef3babc295a0428  0.8s
 => => sha256:67211c14fa74f070d27cc59d69a7fa9aeff8e28ea118ef3babc295a0428a6d21 1.13kB / 1.13kB                     0.0s
 => => sha256:7a57c69fe1e9d5b97c5fe649849e79f2cfc3bf11d10bbd5218b4eb61716aebe6 424B / 424B                         0.0s
 => => sha256:08d22c0ceb150ddeb2237c5fa3129c0183f3cc6f5eeb2e7aa4016da3ad02140a 2.30kB / 2.30kB                     0.0s
 => => sha256:2ab09b027e7f3a0c2e8bb1944ac46de38cebab7145f0bd6effebfe5492c818b6 29.53MB / 29.53MB                   3.7s
 => => extracting sha256:2ab09b027e7f3a0c2e8bb1944ac46de38cebab7145f0bd6effebfe5492c818b6                          1.0s
 => [2/3] RUN apt-get update && apt-get install -y apache2                                                        86.6s
 => [3/3] COPY web_server/ /var/www/html/                                                                          1.7s
 => exporting to image                                                                                             2.1s
 => => exporting layers                                                                                            2.0s
 => => writing image sha256:7021e10bfeab40c5e0e8e9aaad71f0ce97668937640918124ae1423cf0a3e959                       0.0s
 => => naming to docker.io/library/apacheweb                                                                       0.1s

 

being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03$ docker run -p 8080:80 -v /web_server:/var/www/html/ apacheweb
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message

being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_03$ docker container ls
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                                   NAMES
3546cde2eadd   apacheweb   "apache2ctl -D FOREG…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   distracted_booth



being@DESKTOP-RCRJVRG:/mnt/c/Users/IT$  docker run -d -p 3306:3306 --name=mysql -v data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=db mysql/mysql-server:latest
Unable to find image 'mysql/mysql-server:latest' locally
latest: Pulling from mysql/mysql-server
6a4a3ef82cdc: Pull complete
5518b09b1089: Pull complete
b6b576315b62: Pull complete
349b52643cc3: Pull complete
abe8d2406c31: Pull complete
c7668948e14a: Pull complete
c7e93886e496: Pull complete
Digest: sha256:d6c8301b7834c5b9c2b733b10b7e630f441af7bc917c74dba379f24eeeb6a313
Status: Downloaded newer image for mysql/mysql-server:latest
99b3673f8d046a904711927f9b41668f42be8159d69966aa57ba89fe644a0961

docker run -d --name admin --link mysql:db -p 8080:80 phpmyadmin/phpmyadmin:latest
66bfa496a1f995bfc4ca8c1358db1752728c4afe32a45a1ac2c0529972c7857b



being@DESKTOP-RCRJVRG:/mnt/c/Users/IT$ docker run -d --name myadmin --link mysql2:db -e PMA_HOST=mysql2 -e PMA_USER=root
 -e PMA_PASSWORD=b3RmELKOvCUrAdxIg0GEmugc3SY -p 8080:80 phpmyadmin/phpmyadmin:latest
58ebeef9e994dab5a78d49cdcd0280b77014fd40623a0b3bfda92e3a73f3347a
being@DESKTOP-RCRJVRG:/mnt/c/Users/IT$

docker run -p 3306:3306 --name mysql2 -e MYSQL_ROOT_PASSWORD=b3RmELKOvCUrAdxIg0GEmugc3SY -e MYSQL_ROOT_HOST=% -d mysql/mysql-server:latest

docker run -d -p 3306:3306 --name=mysql -v data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123 -e MYSQL_DATABASE=test_db  -e MYSQL_ROOT_HOST=% mysql/mysql-server:latest
docker run -d --name myadmin --link mysql:test_db -e PMA_HOST=mysql -e PMA_USER=root -e PMA_PASSWORD=123 -p 8080:80 phpmyadmin/phpmyadmin:latest
