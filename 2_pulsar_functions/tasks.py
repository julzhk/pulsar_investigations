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
    # make some pulsar messages in the perf-topic
    c.run(f'{PULSAR_ROOT}bin/pulsar-perf produce -r 10 -s 50 public/default/perf-topic')


@task
def perf_test_consumer(c):
    # consumer pulsar messages in the perf-topic (created above)
    c.run(f'{PULSAR_ROOT}bin/pulsar-perf consume -s test-subscription public/default/perf-topic')


@task
def test_topic_subscribers(c):
    # show all pulsar subscribers on a topic
    #  <tenant>/<namespace>/<topic> or <topic>
    c.run(f'{PULSAR_ROOT}bin/pulsar-admin persistent subscriptions public/default/test-topic')


@task
def deploy_function(c):
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
    c.run(f"{PULSAR_ROOT}bin/pulsar-admin functions list"
          )


@task
def trigger_function(c):
    c.run(f'{PULSAR_ROOT}bin/pulsar-admin functions trigger '
          f'--tenant public '
          f'--namespace default '
          f'--name route-fruit-veg '
          f'--topic basket-items '
          f'--trigger-value "carrot"'
          )


@task
def start_function_worker(c):
    # to allow the deployed function to start processing:
    c.run(f"{PULSAR_ROOT}bin/pulsar functions-worker")
