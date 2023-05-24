from kafka import KafkaConsumer

checker = KafkaConsumer('common', bootstrap_servers=['kafka:9092'])

for message in checker:
    print(f"Received message: {message.value.decode()}")
