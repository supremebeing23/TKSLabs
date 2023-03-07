```
ubuntulabs@ubuntulabs-virtualbox:~/TKSLabs/Lab_02$ sudo docker build -f ./Dockerfile_ver2 -t docker-docx .
[+] Building 62.9s (11/11) FINISHED                                                    
 => [internal] load build definition from Dockerfile_ver2                         0.0s
 => => transferring dockerfile: 195B                                              0.0s
 => [internal] load .dockerignore                                                 0.0s
 => => transferring context: 2B                                                   0.0s
 => [internal] load metadata for docker.io/library/python:3                       1.3s
 => [auth] library/python:pull token for registry-1.docker.io                     0.0s
 => [1/5] FROM docker.io/library/python:3@sha256:d3c16df33787f3d03b2e096037f6deb  0.0s
 => [internal] load build context                                                 0.0s
 => => transferring context: 22.98kB                                              0.0s
 => CACHED [2/5] COPY dockerbasics2.py /                                          0.0s
 => [3/5] COPY DockerBasics2.docx /                                               0.2s
 => [4/5] RUN pip install flask                                                   6.8s
 => [5/5] RUN pip install python-docx                                            53.1s
 => exporting to image                                                            1.5s 
 => => exporting layers                                                           1.5s 
 => => writing image sha256:faa0d12d772e6884fafe966d3475761b52b97b04729cee51f801  0.0s 
 => => naming to docker.io/library/docker-docx                                    0.0s 
ubuntulabs@ubuntulabs-virtualbox:~/TKSLabs/Lab_02$ sudo docker run docker-docx
Лабораторна робота №2. Створення Docker контейнера для запуску додатку.

Мета: ознайомитися з Docker та створенням власних Docker контейнерів, написати Dockerfile для збирання контейнера з додатком, запустити додаток у Docker контейнері.

Завдання

Створіть у робочому репозиторії каталог Lab_02. Усі наступні завдання необхідно виконувати у цьому каталозі.
Напишіть додаток, який буде запускатися з терміналу та виводити "Hello, World!" у консоль. Збережіть код у файлі з назвою "app.py".
Створіть файл з назвою "Dockerfile". Додайте у файл наступний вміст:

Цей Dockerfile означає, що ми будемо використовувати базовий образ Python версії 3, копіювати файл "app.py" в кореневу директорію контейнера, встановлювати бібліотеку Flask та запускати додаток командою "python ./app.py".
Відкрийте термінал та перейдіть до кореневої директорії проекту. Введіть наступну команду для збірки контейнера:

$> docker build -t myapp .

Запустіть Docker контейнер, використовуючи наступну команду:

$> docker run myapp

Зупиніть та видаліть створений контейнер.
На вибраній мові програмування напишіть програму, яка зчитує текст цієї лабораторної роботи із файлу і виводить його у термінал.
Створіть Dockerfile для запуску цієї програми у контейнері.
Зберіть та запустіть створений контейнер.
 Закомітьте усі створені файли та відправте зміни на GitHub.

```

