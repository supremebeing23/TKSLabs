from kafka import KafkaConsumer

consumer = KafkaConsumer('common', bootstrap_servers=['kafka:9092'])

for message in consumer:
    print(f"Received message: {message.value.decode()}")
