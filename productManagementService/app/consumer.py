from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:29092'],
    auto_offset_reset='earliest'  # 最初からメッセージを読み取ります
)

print('Listening for messages on topic: test-topic')
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
