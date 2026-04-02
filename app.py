

# ////////////////////////////////////////////////////////////////

# from flask import Flask, render_template, jsonify
# from monitor import get_network_data

# app = Flask(__name__)

# @app.route('/')
# def home():
#     traffic, status, logs = get_network_data()
#     return render_template('index.html', traffic=traffic, status=status)

# @app.route('/data')
# def data():
#     _, _, logs = get_network_data()

#     times = [log["time"] for log in logs]
#     values = [log["traffic"] for log in logs]

#     return jsonify({"times": times, "values": values})

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, jsonify
# from monitor import NetworkMonitor

# app = Flask(__name__)
# monitor = NetworkMonitor()

# @app.route('/')
# def home():
#     traffic, status, _ = monitor.run_monitor()
#     return render_template('index.html', traffic=traffic, status=status)

# @app.route('/data')
# def data():
#     _, _, logs = monitor.run_monitor()

#     times = [log["time"] for log in logs]
#     values = [log["traffic"] for log in logs]

#     return jsonify({
#         "times": times,
#         "values": values
#     })

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, jsonify
from monitor import NetworkMonitor

app = Flask(__name__)
monitor = NetworkMonitor()

THRESHOLD = 80  # 🔥 configurable threshold

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    traffic, status, logs = monitor.run_monitor()

    times = [log["time"] for log in logs]
    values = [log["traffic"] for log in logs]

    # 🔥 Check alert
    alert = any(v > THRESHOLD for v in values)

    return jsonify({
        "times": times,
        "values": values,
        "current_traffic": traffic,
        "status": status,
        "alert": alert
    })

if __name__ == '__main__':
    app.run(debug=True)
    