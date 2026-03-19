import requests
import ipaddress
import concurrent.futures
from urllib.parse import quote

requests.packages.urllib3.disable_warnings()

# MQTT Settings
# TODO: Make patameters to be setup by 3 options: 
# 1 - Config file to be loaded by app, 
# 2 - Passed as argument when executing main.py
# 3 - By asking for user input during execution if no parameter or file were passed on
NETWORK = "10.3.13.0/24"
MQTT_HOST = "lcpsrv"
MQTT_PORT = "1883"

# System Settings:
# TODO: Also make it configurable from user side as the MQTT Settings (?)
TIMEOUT = 3
MAX_THREADS = 40

found_devices = []
updated = []
already_ok = []
failed = []


def check_device(ip):

    try:
        url = f"http://{ip}/cm?cmnd=Status%200"
        r = requests.get(url, timeout=TIMEOUT)

        if "StatusMQT" in r.text:
            return ip, r.json()

    except:
        pass

    return None


def update_device(ip, status):

    try:

        current = status["StatusMQT"]["MqttHost"]

        if current == MQTT_HOST:
            already_ok.append(ip)
            return

        cmd = f"Backlog MqttHost {MQTT_HOST}; MqttPort {MQTT_PORT}"
        url = f"http://{ip}/cm?cmnd={quote(cmd)}"

        r = requests.get(url, timeout=TIMEOUT)

        if r.status_code == 200:
            updated.append(ip)
        else:
            failed.append(ip)

    except:
        failed.append(ip)


def main():

    print(f"Scanning network {NETWORK} for Tasmota devices...\n")

    ips = [str(ip) for ip in ipaddress.IPv4Network(NETWORK)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:

        results = executor.map(check_device, ips)

    for r in results:
        if r:
            found_devices.append(r)

    print(f"Found {len(found_devices)} Tasmota devices\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:

        futures = []

        for ip, status in found_devices:
            futures.append(executor.submit(update_device, ip, status))

        concurrent.futures.wait(futures)

    print("\n===== REPORT =====")

    print(f"Tasmota devices found : {len(found_devices)}")
    print(f"Already correct      : {len(already_ok)}")
    print(f"Updated              : {len(updated)}")
    print(f"Failed               : {len(failed)}")

    if updated:
        print("\nUpdated devices:")
        for i in updated:
            print(i)

    if failed:
        print("\nFailed devices:")
        for i in failed:
            print(i)


if __name__ == "__main__":
    main()
