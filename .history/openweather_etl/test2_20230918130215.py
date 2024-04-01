from kafka import KafkaProducer
import requests
import json

kafka_booststrap_servers = 'localhost:9092'
kafka_topic_name = 'weather_test'

producer = KafkaProducer(bootstrap_servers=kafka_booststrap_servers)
# producer = KafkaProducer(boostrap_servers=kafka_booststrap_servers,
#                          value_serializer = lambda v: json.dumps(v).encode('utf-8'))

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('weather_test', key=b'key', value=b'Hello, Kafka!')