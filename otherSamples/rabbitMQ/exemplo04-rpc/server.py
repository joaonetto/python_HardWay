#!/usr/bin/env python
import pika
import subprocess
import os
# output = subprocess.check_output("cat /etc/services", shell=True)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.0.1.6'))

channel = connection.channel()

channel.queue_declare(queue='my_queue')

def on_request(ch, method, props, body):
    response = os.popen(body).read()
    #print(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='my_queue')
channel.start_consuming()
