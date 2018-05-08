#!/usr/bin/env python
import pika
import uuid
import time
from threading import Thread
from threading import Timer

class cloudDebug(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.0.1.6'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='my_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

def check():
    time.sleep(2)
    if answer != None:
        return
    return ' '

myDebug_rpc = cloudDebug()
answer = None

#timeout = 10
#t = Timer(timeout, print, ['Sorry, times up'])
#t.start()
#prompt = "You have %d seconds to choose the correct answer...\n" % timeout
#answer = input(prompt)
#t.cancel()

while True:
    #t = Timer(timeout, print, [' '])
    #t.start()
    #prompt = 'remoteCall #> '
    #print('teste1')
    #answer = input(prompt)
    #print('teste2')
    response = myDebug_rpc.call(input('remoteCall #> '))
    print(response.decode('utf-8'))
    #t.cancel()
