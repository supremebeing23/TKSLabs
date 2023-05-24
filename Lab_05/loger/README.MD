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




