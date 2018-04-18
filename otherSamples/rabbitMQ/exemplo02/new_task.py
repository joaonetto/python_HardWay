#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.0.1.6'))
channel = connection.channel()

myQueue = 'myTask_01'
myMessage = 'Message to ' + myQueue
channel.queue_declare(queue=myQueue, durable=True)

#message = ' '.join(sys.argv[1:]) or "Oi Vava!"
channel.basic_publish(exchange='',
                      routing_key=myQueue,
                      body=myMessage,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))

myQueue = 'myTask_02'
myMessage = 'Message to ' + myQueue
channel.queue_declare(queue=myQueue, durable=True)

#message = ' '.join(sys.argv[1:]) or "Oi Vava!"
channel.basic_publish(exchange='',
                      routing_key=myQueue,
                      body=myMessage,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))


print(" [x] Enviando: %r" % myMessage)
connection.close()
