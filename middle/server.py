import pika, sys, os


def cb(ch, method, properties, body):
        print(">%s" % body.decode("utf-8"))

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_consume('hello', cb, auto_ack=True)


    print('>Waiting for messages..')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
