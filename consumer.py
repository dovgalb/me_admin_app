import pika

params = pika.URLParameters(
    'amqps://gjbweibk:eL88hOkPdDTTII1I8d7mtO6nTGZscunX@cow.rmq2.cloudamqp.com/gjbweibk'
)

connection = pika.BlockingConnection(params)

chanel = connection.channel()

chanel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('received in admin')
    print(body)

chanel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')

chanel.start_consuming()

chanel.close()
