DEVICES = [
    {"name": "Google DNS", "ip": "8.8.8.8"},
    {"name": "Cloudflare DNS", "ip": "1.1.1.1"},
    {"name": "My PC", "ip": "192.168.1.12"},          # ✅ SNMP test
    {"name": "Router", "ip": "192.168.1.1"},        # ✅ SNMP test
    {"name": "OpenDNS", "ip": "208.67.222.222"},
    {"name": "AWS Server", "ip": "54.239.28.85", "domain": "https://aws.amazon.com"},
    {"name": "GitHub", "ip": "140.82.114.4", "domain": "https://github.com"}
]

THRESHOLDS = {
    "latency": 200,
    "packet_loss": 5
}

SNMP = {
    "community": "public",
    "port": 161
}