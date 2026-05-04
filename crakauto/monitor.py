import time
from tester import test_api

def monitor_loop():
    while True:
        result = test_api()

        print("Health Check:", result)

        if not all(result.values()):
            print("⚠️ System issue detected")

        time.sleep(30)
