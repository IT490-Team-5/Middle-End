import pika
import json

def callback(ch, method, properties, body):
    r = json.loads(body)	
    d = {}
    # here, the front end is sending me either login verification or registering. I send to backend.
    if r.get("reason") == "create" or r.get('reason') == "login":
        print("Received from Front end!: ")
        print("\t" + str(r)) 
        print("Relaying to Back end..")
        channel.basic_publish(exchange="", routing_key="right", body=body)

	# here, the backend is sending me a generated response query (after front end). I send to db.
    elif r.get("reason") == "query":
        print("Received from Backend!: ")
        print("\t" + str(r)) 
        print("Relaying to Database..")
        channel.basic_publish(exchange="", routing_key="database", body=body)
	
        # here, the database is sending me the results of the query. I send this to front.
    elif r.get("reason") == "results":

        print("Received from Database!: ")
        print("\t" + str(r)) 
        print("Relaying to Front end..")
	
        channel.basic_publish(exchange="", routing_key="front", body=body)
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

