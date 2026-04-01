from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from monitor import monitor_network
from alerts import check_alerts
from database import init_db, insert_log, validate_user
from automation import restart_interface
from ai_model import detect_anomaly   # NEW
from flask_socketio import SocketIO
import time
import threading



app = Flask(__name__)
app.secret_key = "supersecretkey"
socketio = SocketIO(app)

init_db()

def send_live_data():
    while True:
        devices = monitor_network()
        socketio.emit('update', devices)
        socketio.sleep(5)   # ✅ IMPORTANT (not time.sleep)

def start_background():
    socketio.start_background_task(send_live_data)



@app.route("/")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    
    devices = monitor_network()

    for d in devices:
        insert_log(d)
        alerts = check_alerts(d)

        if "Device DOWN" in alerts:
            restart_interface(d["ip"])

        d["alerts"] = alerts

        # AI Detection
        d["ai_status"] = detect_anomaly(d["latency"], d["packet_loss"])

    return render_template("dashboard.html", devices=devices)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if validate_user(username, password):
            session["user"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")



# ✅ NEW API FOR GRAPH
@app.route("/api/data")
def api_data():
    devices = monitor_network()
    return jsonify(devices)


if __name__ == "__main__":
    socketio.start_background_task(send_live_data)  # ✅ start thread safely
    socketio.run(app, debug=True)