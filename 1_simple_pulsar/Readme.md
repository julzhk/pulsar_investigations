Getting started with Apache Pulsar 
-

Some useful commands:

Start Pulsar:

`bin/pulsar standalone`


pulsar-admin
-

What's going on in Pulsar?

`bin/pulsar-admin namespaces list public/functions`

`bin/pulsar-admin tenants list`

`bin/pulsar-admin clusters list`
 
pulsar-client
-

Create / consume a simple message

 `bin/pulsar-client produce -m "Hello Pulsar" public/default/test-topic`
 
 `bin/pulsar-client consume -s test-subscription public/default/test-topic`



Monitoring throughput 
-

Gives an answer to: What is Pulsar's throughput performance?   

A generous producer!

` 
bin/pulsar-perf produce -r 10 -s 50 public/default/perf-topic
` 

A hungry consumer!

`bin/pulsar-perf consume -s test-subscription public/default/perf-topic`


Display all subscriptions on a topic:
-
`bin/pulsar-admin persistent subscriptions public/default/test-topic`

