from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:29092')
topic_name = 'test-topic'

# メッセージを送信
producer.send(topic_name, b'Hello, world123!')
producer.flush()  # すべての非同期メッセージが送信されるまで待機

print('Message sent to topic:', topic_name)
