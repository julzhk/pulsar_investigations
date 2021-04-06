from invoke import task

PULSAR_ROOT = '~/apache-pulsar-2.6.2/'


# invoke: run bash from python with eg: 'invoke deploy-function'


@task
def list(c):
    # show all tasks
    c.run('inv --list')


@task
def start(c):
    # start local dev mode for pulsar
    c.run(f'{PULSAR_ROOT}bin/pulsar standalone')


@task
def topics(c):
    # show pulsar topics
    c.run(f'{PULSAR_ROOT}bin/pulsar-admin persistent list public/default')


@task
def perf_test_producer(c):
    # make some pulsar messages in the perf-topic; gives a throughput performance score
    # invoke perf-test-producer
    # example result :
    # Throughput produced: 10.1 msg/s
    # Latency: mean:   4.398

    c.run(f'{PULSAR_ROOT}bin/pulsar-perf produce -r 10 -s 50 public/default/perf-topic')


@task
def perf_test_consumer(c):
    # consumer pulsar messages in the perf-topic (created above)
    # invoke perf-test-consumer
    # example result :
    # org.apache.pulsar.testclient.PerformanceConsumer -
    # Throughput received: 10.050 msg / s

    c.run(f'{PULSAR_ROOT}bin/pulsar-perf consume -s test-subscription public/default/perf-topic')


@task
def test_topic_subscribers(c):
    # show all pulsar subscribers on a given topic (test-topic)
    #  <tenant>/<namespace>/<topic> or <topic>
    c.run(f'{PULSAR_ROOT}bin/pulsar-admin persistent subscriptions public/default/test-topic')


@task
def deploy_function(c):
    # invoke deploy_function
    # puts this python code in pulsar : like an AWS lambda function
    c.run(f"{PULSAR_ROOT}bin/pulsar-admin functions create  "
          " --py  ~/Projects/LearningPulsar/2_pulsar_functions/router.py  "
          "--classname router.RoutingFunction "
          " --tenant public "
          "--namespace default "
          "--name route-fruit-veg "
          "--inputs persistent://public/default/basket-items")


@task
def delete_function(c):
    c.run(f"{PULSAR_ROOT}bin/pulsar-admin functions delete \
  --tenant public \
  --namespace default \
  --name route-fruit-veg"
          )


@task
def list_functions(c):
    # invoke list-functions
    # >>>"route-fruit-veg"

    c.run(f"{PULSAR_ROOT}bin/pulsar-admin functions list"
          )


@task
def trigger_function(c):
    # Function in trigger function has unidentified topic
    c.run(f'{PULSAR_ROOT}bin/pulsar-admin functions trigger '
          f'--tenant public '
          f'--namespace default '
          f'--name route-fruit-veg '
          f'--topic persistent://public/default/basket-items '
          f'--trigger-value "apple"'
          )


@task
def start_function_worker(c):
    # to allow the deployed function to start processing:
    # invoke start-function-worker
    # Server started at http: // 127.0.0.1: 6750 / admin
    # INFO org.apache.pulsar.functions.worker.Worker - / ** Started worker server on port = 6750 ** /
    c.run(f"{PULSAR_ROOT}bin/pulsar functions-worker")


@task
def produce_food(c):
    c.run(f"python "
          f"produce_food.py")


@task
def consume_food(c):
    c.run(f"python "
          f" consumer_food.py")

