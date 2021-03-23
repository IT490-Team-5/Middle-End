import pika
import json

def callback(ch, method, properties, body):
	r = json.loads(body)	
	d = {}

	# here, the front end is sending me either login verification or registering
	if r.get("reason") == "create" or r.get('reason') == "login":
		channel.basic_publish(exchange="", routing_key="right", body=body)

	# here, the backend is sending me a generated response query (after front end). 
	elif r.get("reason") == "query":
		r["reason"] = "sqlstatement"	
		res = json.dumps(r)
		channel.basic_publish(exchange="", routing_key="database", body=res)

	elif r.get("reason") == "results":
		pass
	else:
		print("I don't understand")

creds = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, "vh1", creds))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.queue_declare(queue="right")
channel.queue_declare(queue="database")
channel.queue_declare(queue="front")
channel.basic_consume('hello', callback, auto_ack=True)


print('Waiting for messages..')
channel.start_consuming()

