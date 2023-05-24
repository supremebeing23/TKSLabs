###LAB_05

```
being@DESKTOP-RCRJVRG:/mnt/c/Users/IT$ docker network create lab
85aa51da5e23cba0cbf774c6e53015edcfe0832b92731a33b39dfc207578a811
```
```
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_05$ docker-compose up -d
Pulling zookeeper (zookeeper:)...
latest: Pulling from library/zookeeper
1bc677758ad7: Pull complete
458b02b5411a: Pull complete
b04a165ead1d: Pull complete
1187c73b1850: Pull complete
5930529b6097: Pull complete
8b11d2d1cbc9: Pull complete
5d3163cc8fed: Pull complete
64efce64799b: Pull complete
Digest: sha256:1c2283ec6e32f1e0df06e09c310c8a88110e97c3e373abfff0138062b26b906a
Status: Downloaded newer image for zookeeper:latest
Pulling kafka (wurstmeister/kafka:)...
latest: Pulling from wurstmeister/kafka
42c077c10790: Pull complete
44b062e78fd7: Pull complete
b3ba9647f279: Pull complete
10c9a58bd495: Pull complete
ed9bd501c190: Pull complete
03346d650161: Pull complete
539ec416bc55: Pull complete
Digest: sha256:2d4bbf9cc83d9854d36582987da5f939fb9255fb128d18e3cf2c6ad825a32751
Status: Downloaded newer image for wurstmeister/kafka:latest
Creating lab_05_zookeeper_1 ... done
Creating lab_05_kafka_1     ... error

ERROR: for lab_05_kafka_1  Cannot start service kafka: driver failed programming external connectivity on endpoint lab_05_kafka_1 (d2e55ec877151778d98d0fcc055f7e57769e17336bb7018081c8001a15265798): Error starting userland proxy: listen tcp4 0.0.0.0:9092: bind: address already in use

ERROR: for kafka  Cannot start service kafka: driver failed programming external connectivity on endpoint lab_05_kafka_1 (d2e55ec877151778d98d0fcc055f7e57769e17336bb7018081c8001a15265798): Error starting userland proxy: listen tcp4 0.0.0.0:9092: bind: address already in use
ERROR: Encountered errors while bringing up the project.
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_05$ docker-compose up -d
lab_05_zookeeper_1 is up-to-date
Starting lab_05_kafka_1 ... done
```

```
being@DESKTOP-RCRJVRG:~/TKSLabs/Lab_05$ docker-compose ps
       Name                     Command               State                    Ports
------------------------------------------------------------------------------------------------------
lab_05_kafka_1       start-kafka.sh                   Up      0.0.0.0:9092->9092/tcp,:::9092->9092/tcp
lab_05_zookeeper_1   /docker-entrypoint.sh zkSe ...   Up      2181/tcp, 2888/tcp, 3888/tcp, 8080/tcp
```

```
docker build -t logerkafka .
[+] Building 10.9s (8/8) FINISHED
 => [internal] load .dockerignore                                                                                  0.5s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                               0.3s
 => => transferring dockerfile: 260B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3                                                        1.2s
 => [internal] load build context                                                                                  0.4s
 => => transferring context: 30B                                                                                   0.0s
 => CACHED [1/3] FROM docker.io/library/python:3@sha256:b9683fa80e22970150741c974f45bf1d25856bd76443ea561df4e6fc0  0.0s
 => [2/3] RUN pip install kafka-python                                                                             6.6s
 => [3/3] ADD loger.py /                                                                                           1.2s
 => exporting to image                                                                                             1.2s
 => => exporting layers                                                                                            1.1s
 => => writing image sha256:a2d35ef955ece9729447dd54aaf1c3eb5626096d7405f238bb9f6fb6e1dc6780                       0.1s
 => => naming to docker.io/library/logerkafka
```
```
docker build -t checkerkafka .
[+] Building 4.4s (8/8) FINISHED
 => [internal] load .dockerignore                                                                                  0.4s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                               0.5s
 => => transferring dockerfile: 264B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3                                                        1.8s
 => [1/3] FROM docker.io/library/python:3@sha256:b9683fa80e22970150741c974f45bf1d25856bd76443ea561df4e6fc00c2bc17  0.0s
 => CACHED [2/3] RUN pip install kafka-python                                                                      0.0s
 => [internal] load build context                                                                                  0.2s
 => => transferring context: 309B                                                                                  0.0s
 => [3/3] ADD checker.py /                                                                                         0.8s
 => exporting to image                                                                                             0.8s
 => => exporting layers                                                                                            0.7s
 => => writing image sha256:634e689d335af2d34b3758c37e0288dfa069983cb16f07db09fd0ba350b4dc40                       0.1s
 => => naming to docker.io/library/checkerkafka
```
```
version: "3.7"
services:
  zookeeper:
    image: zookeeper
    networks:
      - lab05

  kafka:
    image: wurstmeister/kafka
    depends_on:
      - zookeeper
    ports:
      - 9092:9092
    environment:
      - KAFKA_ADVERTISED_HOST_NAME=kafka  
      - KAFKA_BROKER_ID=1
      - KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092
      - KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092
      - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
      - KAFKA_CREATE_TOPICS=common:1:1
      - KAFKA_PORT=9092
    networks:
      - lab05
      
  loger:
    image: logerkafka     
    depends_on:
      - kafka
      - loger
    networks:
      - lab05
      
  checker:
    image: checkerkafka
    depends_on:
     - kafka
    networks:
      - lab05      

networks:
  lab05:
    name: lab05
    external: true
```

SERVICE 1
```
from kafka import KafkaProducer
from datetime import datetime
import time

loger = KafkaProducer(bootstrap_servers='kafka:9092')

while True:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = current_time.encode()
    loger.send('common', message)
    time.sleep(5)
```

SERVICE2
```
from kafka import KafkaConsumer

checker = KafkaConsumer('common', bootstrap_servers=['kafka:9092'])

for message in checker:
    print(f"Received message: {message.value.decode()}")
```









