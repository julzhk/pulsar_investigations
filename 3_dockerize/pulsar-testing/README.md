# pulsar-testing

# Purpose

This project is just a simple example using Apache Pulsar with python with :

- a producer, sending random messages at random intervals to "my-topic".
- a consumer, subscribed to "my-topic", consuming and printing the messages.

# Install

Just have Docker installed.

# Run

Simply run

    $>docker-compose up --build

Then wait 60 seconds.
> The clients have to wait for Pulsar to setup metadatas
