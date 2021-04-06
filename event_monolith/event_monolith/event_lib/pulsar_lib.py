from functools import wraps
from time import gmtime, strftime

import pulsar
from pulsar.schema import Record, String, AvroSchema


class WebVisit(Record):
    url = String()
    greeting = String()
    username = String()


class WebVisit2(Record):
    url = String()
    greeting = String()
    time = String()

    @property
    def to_dict(self):
        return {'url': self.url,
                'time': self.time}


client = pulsar.Client("pulsar://localhost:6650")
producer_name = 'web-decorator2'
topic = f'persistent://public/default/{producer_name}'
producer = client.create_producer(
    topic=topic,
    producer_name=producer_name,
    schema=AvroSchema(WebVisit2),
)


def Pulsar_send(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        producer.send(WebVisit2(url='Hello', greeting='hola', time=showtime))
        return function(request, *args, **kwargs)

    return wrap
