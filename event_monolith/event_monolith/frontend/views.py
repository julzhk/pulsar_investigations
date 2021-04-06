from django.shortcuts import render
from pulsar.schema import AvroSchema

from event_lib.pulsar_lib import Pulsar_send, WebVisit2, client, topic, producer_name


@Pulsar_send
def home(request):
    consumer = client.subscribe(
        topic=topic,
        subscription_name=f'view-{producer_name}',
        schema=AvroSchema(WebVisit2))

    msg = consumer.receive()
    ex = msg.value()
    print("Received message a={} b={} c={}".format(ex.url, ex.greeting, ex.time))
    consumer.acknowledge(msg)
    consumer.close()
    return render(request, 'frontend/home.html', context=ex.to_dict)
