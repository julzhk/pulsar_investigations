import pulsar

# the 'router-pular' function should be filtering the stream created in 'produce-food.py' script
# into a new stream 'vegetables' which should be consumed here..

client = pulsar.Client("pulsar://localhost:6650")

consumer = client.subscribe('persistent://public/default/vegetables', 'vegetables')

waitingForMsg = True
while waitingForMsg:
    try:
        msg = consumer.receive(2000)
        print("Received message '{}'".format(msg.data()))
        consumer.acknowledge(msg)

        # waitingForMsg = False
    except:
        print("Waiting for a message...");

client.close()
