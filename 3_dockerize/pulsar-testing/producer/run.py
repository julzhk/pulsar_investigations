from datetime import datetime
import pulsar
import random as rd
import time as t
import json

if __name__ == "__main__":
    t.sleep(60)
    client = pulsar.Client('pulsar://pulsar:6650')
    producer = client.create_producer('my-topic')
    rd.seed()
    while True:
        producer.send(
            json.dumps(
                {
                    'time': f'{datetime.now()}',
                    'message': rd.choice([
                        'Hey what\'s up mate ?',
                        'I\'m batman.',
                        '2 + 2 = 4 !',
                        'Indeeeeeeeed a wise choice !'
                    ])
                }
            ).encode('utf-8')
        )
        t.sleep(0.2 + rd.random())
    client.close()
