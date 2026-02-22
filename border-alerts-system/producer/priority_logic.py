from main import *


def priority_URGENT(data):
    if (
        data["weapons_count"] > 0
        or data["distance_from_fence_m"] <= 50
        or data["people_count"] >= 8
        or data["vehicle_type"] == "truck"
    ):
        alerts = "URGENT"
    else:
        alerts = "URGENT"
    return alerts


def priority_NORMAL(data):
    if (
        data["distance_from_fence_m"] <= 150
        and data["people_count"] >= 4
        or data["vehicle_type"] == "jeep"
        and data["people_count"] >= 3
    ):
        alerts = "NORMAL"
    else:
        alerts = "NORMAL"
    return alerts
