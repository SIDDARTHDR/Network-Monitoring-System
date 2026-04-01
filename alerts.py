from config import THRESHOLDS

def check_alerts(device):
    alerts = []

    if device["status"] == "DOWN":
        alerts.append("Device DOWN")

    if device["latency"] > THRESHOLDS["latency"]:
        alerts.append("High Latency")

    if device["packet_loss"] > THRESHOLDS["packet_loss"]:
        alerts.append("Packet Loss High")

    return alerts