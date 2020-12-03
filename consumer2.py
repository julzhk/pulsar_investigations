import pulsar

client = pulsar.Client("pulsar://localhost:6650")

consumer = client.subscribe('persistent://public/default/test-topic', 'test-subscription-2')

waitingForMsg = True
while waitingForMsg:
    try:
        msg = consumer.receive(2000)
        print("Received message '{}'".format(msg.data()))
        consumer.acknowledge(msg)

        waitingForMsg = False
    except:
        print("Waiting for a message...");

client.close()
