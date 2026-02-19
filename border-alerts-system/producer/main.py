import json
from confluent_kafka import Producer
from priority_logic import *
import redis

r = redis.Redis(host="localhost", port=6379, db=0)

producer_config = {"bootstrap.servers": "localhost:9092"}

producer = Producer(producer_config)


def report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode("utf-8")}")
        print(
            f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}"
        )

    # Opening and reading the JSON file
    with open("border_alerts.json", "r") as f:
        # Parsing the JSON file into a Python dictionary
        data = json.load(f)

    for item in data:
        if item == priority_URGENT:
            r.lpush("queue_urgent", json.dumps(data))
        elif item == priority_NORMAL:
            r.lpush("queue_normal", json.dumps(item))
        else:
            r.lpush("", json.dumps(item))

    value = json.dumps(item).encode("utf-8")

    producer.produce(topic="alerts", value=value, callback=report)

    producer.flush()
