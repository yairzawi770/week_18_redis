from time import time
from kafka import KafkaConsumer
import json
from mongo_connection import *


def main():
    consumer = KafkaConsumer(
        topics="alerts",
        bootstrap_servers=KAFKA_SERVERS,
        group_id="team",
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
    )

    for msg in consumer:
        alerts = msg.value
        property_ = alerts.get("queue_urgent", "queue_normal")
        print(property_)

        result = orders_col.insert_one({msg}, {"$set": {"time_insertion": time.now()}})
    return result


if __name__ == "__main__":
    main()
