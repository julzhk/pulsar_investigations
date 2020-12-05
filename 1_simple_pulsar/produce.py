import pulsar

client = pulsar.Client("pulsar://localhost:6650")

producer = client.create_producer('persistent://public/default/test-topic')

for i in range(1000):
    print(i)
    producer.send((f'Hello Pulsar {i}!').encode('utf-8'))

