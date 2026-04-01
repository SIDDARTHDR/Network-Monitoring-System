import subprocess
import socket
import requests
import re
from config import DEVICES
from snmp_monitor import get_snmp_data

# -----------------------
# PING CHECK
# -----------------------
def ping_device(ip):
    try:
        output = subprocess.check_output(f"ping -n 2 {ip}", shell=True).decode()

        loss = int(re.search(r"(\d+)% loss", output).group(1))
        latency_match = re.search(r"Average = (\d+)ms", output)

        latency = int(latency_match.group(1)) if latency_match else 0

        return True, latency, loss
    except:
        return False, 0, 100


# -----------------------
# PORT CHECK
# -----------------------
def check_port(ip, port=80):
    try:
        socket.create_connection((ip, port), timeout=2)
        return True
    except:
        return False


# -----------------------
# HTTP CHECK
# -----------------------
def check_http(target):
    try:
        requests.get(target, timeout=2)
        return True
    except:
        return False


# -----------------------
# SMART DETECTION
# -----------------------
def smart_status(device):
    ip = device["ip"]

    ping_ok, latency, loss = ping_device(ip)
    port_ok = check_port(ip, 80)

    # 🔥 Use domain if available
    http_target = device.get("domain", f"http://{ip}")
    http_ok = check_http(http_target)

    if ping_ok:
        return "UP", latency, loss
    elif port_ok or http_ok:
        return "PARTIAL", latency, loss
    else:
        return "DOWN", latency, loss


# -----------------------
# MAIN MONITOR FUNCTION
# -----------------------
def monitor_network():
    results = []

    for device in DEVICES:
        status, latency, loss = smart_status(device)

        # 🔥 Get CPU using SNMP
        cpu = get_snmp_data(device["ip"])

        results.append({
            "name": device["name"],
            "ip": device["ip"],
            "status": status,
            "latency": latency,
            "packet_loss": loss,
            "cpu": cpu   # ✅ FIX ADDED
        })

    return results