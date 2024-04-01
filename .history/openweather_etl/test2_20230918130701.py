from kafka import KafkaProducer
import requests
import json

kafka_booststrap_servers = 'localhost:9092'
kafka_topic_name = 'weather_test'


a =1
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('weather_test', key=b'key', value=b'Hello, Kafka!')
