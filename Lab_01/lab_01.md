#Лабораторна робота №1. Знайомство із системою контейнеризації Docker
#Task 5 Запустити hello-world

sudo docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

#5.2
sudo docker images  hello-world
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    feb5d9fea6a5   17 months ago   13.3kB


#task 6 ellerbrock/alpine-bash-git
#6.1
ubuntulabs@ubuntulabs-virtualbox:~$ sudo docker pull ellerbrock/alpine-bash-git
ubuntulabs@ubuntulabs-virtualbox:~$ sudo docker images ellerbrock/alpine-bash-git
REPOSITORY                   TAG       IMAGE ID       CREATED       SIZE
ellerbrock/alpine-bash-git   latest    67830aff234a   3 years ago   26.7MB
#6.2
sudo docker run -it -d --name lab01 --entrypoint /bin/bash ellerbrock/alpine-bash-git
[sudo] пароль до ubuntulabs: 
5c0f35abbc840d6dcc451e4eea30a6e09e573e62bd067fd155b4eabc9c10ac55

sudo docker exec -it lab01 bash

bash-4.4$ whoami
download

bash-4.4$ cd /
bash-4.4$ ls
bin    etc    lib    mnt    root   sbin   sys    usr
dev    home   media  proc   run    srv    tmp    var

bash-4.4$ git --version
git version 2.18.1

bash-4.4$ cd /home/download
bash-4.4$ git clone https://github.com/supremebeing23/TKSLabs.git
Cloning into 'TKSLabs'...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 17 (delta 1), reused 15 (delta 1), pack-reused 0
Unpacking objects: 100% (17/17), done.
bash-4.4$ ls
TKSLabs

bash-4.4$ exit
exit

ubuntulabs@ubuntulabs-virtualbox:~$ sudo docker restart lab01
[sudo] пароль до ubuntulabs: 
lab01

ubuntulabs@ubuntulabs-virtualbox:~$ sudo docker exec -it lab01 bash
bash-4.4$ ls
TKSLabs










