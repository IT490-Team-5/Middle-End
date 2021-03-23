import pika
import json

def callback(ch, method, properties, body):
	print(json.loads(body))	

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume('hello', callback, auto_ack=True)


print('Waiting for messages..')
channel.start_consuming()

