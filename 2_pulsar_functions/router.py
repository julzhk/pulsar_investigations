from pulsar import Function

# taken from example: https://pulsar.apache.org/docs/en/2.6.0/functions-overview/

class RoutingFunction(Function):
    def __init__(self):
        self.basket = "persistent://public/default/basket-items"
        self.fruits_topic = "persistent://public/default/fruits"
        self.vegetables_topic = "persistent://public/default/vegetables"

    def is_fruit(item):
        return item in [b"apple", b"orange", b"pear", b"other fruits..."]

    def is_vegetable(item):
        return item in [b"carrot", b"lettuce", b"radish", b"other vegetables..."]

    def process(self, item, context):
        context.get_logger().warn('start')
        if self.is_fruit(item):
            context.get_logger().warn('is fruit')
            context.publish(self.fruits_topic, item)
        elif self.is_vegetable(item):
            context.get_logger().warn('is veg')
            context.publish(self.vegetables_topic, item)
        else:
            context.publish(self.basket, f'NOT {item} item')
            warning = "The item {0} is neither a fruit nor a vegetable".format(item)
            print(warning)
            context.get_logger().warn(warning)
