import redis
import time

# Conectar a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def publish_messages():
    for i in range(10):
        message = f'Mensaje {i}'
        r.publish('canal1', message)
        print(f'Publicado: {message}')
        time.sleep(1)

if __name__ == '__main__':
    publish_messages()


# SUBSCRIPTOR

import redis

# Conectar a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def subscribe_to_channel():
    pubsub = r.pubsub()
    pubsub.subscribe('canal1')
    
    print('Suscrito al canal1')
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f'Recibido: {message["data"].decode("utf-8")}')

if __name__ == '__main__':
    subscribe_to_channel()
