# 🚀 Enterprise Network Monitoring & Mini SOC Dashboard

A real-time **Network Monitoring and SOC (Security Operations Center) Dashboard** built using **Python, Flask, Socket.IO, and JavaScript**.

This system continuously monitors network connectivity, detects anomalies, generates alerts, and provides an interactive dashboard for analysis — simulating a **mini SOC environment**.

---

## 🧠 Project Overview

This project monitors the connectivity and performance between your system and multiple external/internal devices such as:

* Google DNS (8.8.8.8)
* Cloudflare DNS (1.1.1.1)
* AWS Server
* GitHub
* Local Router / PC (via SNMP)

It evaluates:

* ✅ Reachability (Ping)
* ⚡ Latency (Response Time)
* 📉 Packet Loss
* 🌐 Service Availability (HTTP/Port)
* 🖥 CPU Usage (via SNMP)
* 🤖 AI-based anomaly detection

---

## 🎯 Key Features

### 📊 Real-Time Dashboard

* Live device monitoring using Socket.IO
* Dynamic charts (latency trends)
* Status classification: **UP / DOWN / PARTIAL**

### 🚨 SOC-Level Alerting System

* Alert generation based on thresholds
* Severity levels: **NORMAL / WARNING / CRITICAL**
* ✅ Alert deduplication (no repeated alerts)
* 🕒 Timestamped alerts
* 🔔 Toast notifications

### 🧠 AI-Based Anomaly Detection

* Detect unusual latency and packet loss patterns
* Intelligent classification of network behavior

### 📡 Smart Network Monitoring

* Ping + Port + HTTP combined logic
* Detect partial connectivity scenarios
* Real-world network diagnosis approach

### 📜 Logs & Forensics

* SQLite-based logging system
* Searchable logs
* Historical network analysis

### 🖥 Device Insights

* Clickable device-level analysis page
* Risk scoring (SOC-style)
* CPU monitoring using SNMP

### 🔐 Authentication System

* Login/logout system
* Session-based access control

---

## 🏗 Tech Stack

| Layer      | Technology                  |
| ---------- | --------------------------- |
| Backend    | Python, Flask               |
| Realtime   | Flask-SocketIO              |
| Frontend   | HTML, CSS, JavaScript       |
| Charts     | Chart.js                    |
| Database   | SQLite                      |
| Networking | Ping, Socket, HTTP Requests |
| Monitoring | SNMP (pysnmp)               |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/network-monitoring-dashboard.git
cd network-monitoring-dashboard
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🔑 Default Login

```
Username: Nero S
Password: 2705
```

---

## 📁 Project Structure

```
├── app.py               # Main Flask app
├── monitor.py           # Network monitoring logic
├── alerts.py            # Alert detection system
├── automation.py        # Auto-recovery actions
├── database.py          # SQLite logging system
├── config.py            # Devices & thresholds
├── snmp_monitor.py      # CPU monitoring via SNMP
├── templates/
│   ├── dashboard.html
│   ├── devices.html
│   ├── alerts.html
│   ├── logs.html
│   └── device.html
└── logs/
    └── network_logs.db
```

---

## 🧠 How It Works

1. System continuously monitors devices using:

   * Ping
   * Port checks
   * HTTP requests

2. Data is processed and classified:

   * UP / DOWN / PARTIAL

3. Alerts are generated when:

   * High latency
   * Packet loss
   * Device down

4. Data is:

   * Sent to frontend via WebSocket
   * Logged into database
   * Displayed in dashboard

---

## 🚀 Advanced Features (SOC-Level)

* Risk Scoring System
* Alert Deduplication
* AI Anomaly Detection
* Live Monitoring with WebSockets
* Device-level analytics

---

## 📸 Screenshots

* Dashboard with live metrics
* Alert panel with severity
* Device insights page
* Logs and analytics view

---

## 💼 Use Cases

* Network Monitoring
* DevOps Health Checks
* SOC Simulation
* Cybersecurity Learning Project
* Infrastructure Monitoring

---

## 📈 Future Enhancements

* 📡 Network Topology Graph
* 🌍 Geo-IP Tracking
* 📩 Email/SMS Alerts
* 🔔 Sound Notifications
* 🤖 Advanced ML-based anomaly detection
* 👥 Role-based access control

---

## 🏁 Conclusion

This project demonstrates a **real-world network monitoring system** with SOC-level capabilities, combining:

* Networking concepts
* Backend engineering
* Real-time systems
* Security monitoring

---

## 👨‍💻 Author

**Siddarth**

---

⭐ If you like this project, give it a star!
