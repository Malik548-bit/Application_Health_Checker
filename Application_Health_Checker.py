import requests
import logging
import time

# Application URL
APP_URL = '(link unavailable)'  # Replace with your application URL

# Logging setup
logging.basicConfig(filename='app_health.log', level=logging.INFO)

def check_app_status():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            logging.info(f"Application is UP: {APP_URL} (Status Code: {response.status_code})")
            return "UP"
        else:
            logging.warning(f"Application is DOWN: {APP_URL} (Status Code: {response.status_code})")
            return "DOWN"
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is DOWN: {APP_URL} (Error: {e})")
        return "DOWN"

def main():
    while True:
        status = check_app_status()
        print(f"Application Status: {status}")
        time.sleep(60)  # Check every 1 minute

if __name__ == "__main__":
    main()

