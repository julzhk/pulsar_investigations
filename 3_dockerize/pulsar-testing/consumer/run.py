import pulsar
import time as t

if __name__ == "__main__":
    t.sleep(60)
    client = pulsar.Client('pulsar://pulsar:6650')
    consumer = client.subscribe('my-topic', 'my-subscription')
    while True:
        t.sleep(1)
        msg = consumer.receive()
        try:
            print(f'Received message "{msg.data()}" id="{msg.message_id()}"', flush=True)
            consumer.acknowledge(msg)
        except:
            consumer.negative_acknowledge(msg)

    client.close()
