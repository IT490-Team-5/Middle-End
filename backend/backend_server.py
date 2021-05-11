import pika
import json

def callback(ch, method, properties, body):
    info = json.loads(body)
    print(info)
    if info.get("reason") == "create":
    #This is when we get something to turn into SQL Statement add AND process register
      query = "INSERT INTO test (user, pass) VALUES (%s, %s)"
      message = {'create':query, 'reason':'query2', 'values':(info["user"], info["password"])}
    
    if info.get("reason") == "login":
    #This is when we get something to turn into SQL Statement add AND process login
        query = "SELECT * FROM test WHERE user=%s and pass=%s"
        message = {'login':query, 'reason':'query2', 'values':(info["user"], info["password"])}

    if info.get("reason") == "fetch":
        query = "SELECT score FROM test WHERE user=%s and pass=%s"
        message = {"reason":"query2", "values":(info["user"], info["password"]), queryString: message }

    msgjson = json.dumps(message)
    channel.basic_publish(exchange='', routing_key='hello', body=msgjson)
    


creds = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('25.3.113.97', 5672, "vh1", creds))
channel = connection.channel()
channel.queue_declare(queue='right')
channel.basic_consume('right', callback, auto_ack=True)