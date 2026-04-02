# Custom Monitoring Tool 


# import random
# from datetime import datetime

# class NetworkMonitor:

#     def __init__(self):
#         self.logs = []

#     def generate_traffic(self):
#         return random.randint(1, 100)

#     def detect_status(self, traffic):
#         if traffic > 80:
#             return "Suspicious"
#         return "Normal"

#     def run_monitor(self):
#         traffic = self.generate_traffic()
#         status = self.detect_status(traffic)
#         time = datetime.now().strftime("%H:%M:%S")

#         self.logs.append({
#             "time": time,
#             "traffic": traffic,
#             "status": status
#         })

#         return traffic, status, self.logs

import random
import datetime

class NetworkMonitor:
    def __init__(self):
        self.logs = []

    def run_monitor(self):
        traffic = random.randint(10, 100)
        status = "Normal" if traffic < 80 else "High Traffic"

        log = {
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "traffic": traffic
        }

        self.logs.append(log)

        # Keep last 10 logs
        self.logs = self.logs[-10:]

        return traffic, status, self.logs