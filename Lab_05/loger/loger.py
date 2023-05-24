from kafka import KafkaProducer
from datetime import datetime
import time

loger = KafkaProducer(bootstrap_servers='kafka:9092')

while True:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = current_time.encode()
    loger.send('common', message)
    time.sleep(5)