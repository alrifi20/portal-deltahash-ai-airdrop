import requests
import time

BASE_URL = "https://portal.deltahash.ai"

cookie = input("Masukkan cookie connect.sid: ")
device_id = input("Masukkan Device ID: ")

headers = {
    "accept": "*/*",
    "content-type": "application/json",
    "origin": "https://portal.deltahash.ai",
    "referer": "https://portal.deltahash.ai/",
    "user-agent": "Mozilla/5.0",
    "cookie": cookie
}

def connect_mining():
    url = BASE_URL + "/api/mining/connect"

    payload = {
        "deviceId": device_id
    }

    r = requests.post(url, headers=headers, json=payload)
    data = r.json()

    if data.get("success"):
        session = data["session"]
        print("\n✅ Mining Connected")
        print("Session ID:", session["id"])
        print("Connected Epoch:", data["epochNumber"])
    else:
        print("❌ Connect gagal")
        print(data)


def heartbeat():
    url = BASE_URL + "/api/mining/heartbeat"

    payload = {
        "deviceId": device_id
    }

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code == 200:
        print("💓 Heartbeat OK")
    else:
        print("❌ Heartbeat Error:", r.status_code)


def check_status():
    url = BASE_URL + "/api/user"

    try:
        r = requests.get(url, headers=headers)
        data = r.json()

        user = data["user"]

        print("\n📊 STATUS")
        print("User:", user["username"])
        print("Balance:", user["balance"], "DTH")
        print("Device Connected:", user["deviceConnected"])
        print("Epoch Participated:", user["totalEpochsParticipated"])

    except:
        print("❌ Tidak bisa mengambil status")


print("🚀 Start DeltaHash Miner\n")

connect_mining()

counter = 0

while True:

    heartbeat()

    counter += 1

    if counter % 2 == 0:
        check_status()

    time.sleep(30)
