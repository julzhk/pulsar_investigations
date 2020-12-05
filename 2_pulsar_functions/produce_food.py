import pulsar

client = pulsar.Client("pulsar://localhost:6650")

producer = client.create_producer('persistent://public/default/basket-items')

for item in [
    b"apple", b"orange", b"pear", b"other fruits...",
    b"carrot", b"lettuce", b"radish", b"other vegetables...",
    b"cat", b"bat", b"dog", b"other animal...",

]:
    print(item)
    producer.send((f'{item}').encode('utf-8'))
    producer.send(item)
