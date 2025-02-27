from serializers.location_serializer import locations_serializer
from typing import List


def receiver_serializer(receiver) -> dict:
    return {
        "receiver_id": receiver["receiver_id"],
        "locations": locations_serializer(receiver["locations"])
    }

def receivers_serializer(receivers: List) -> list:
    return [receiver_serializer(receiver) for receiver in receivers]