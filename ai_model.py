from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.2)

def detect_anomaly(latency, loss):
    try:
        # Use historical-like data
        data = np.array([
            [20, 0],
            [30, 1],
            [50, 2],
            [200, 10],
            [latency, loss]
        ])

        model.fit(data)
        pred = model.predict([[latency, loss]])

        return "Anomaly" if pred[0] == -1 else "Normal"

    except:
        return "Normal"