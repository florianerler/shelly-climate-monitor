import requests
import time

def abfrage():
        a = requests.get("http://192.168.1.129/rpc/Shelly.GetStatus")
        return (a.status_code)



while True:
    print(abfrage())
    time.sleep(60)
    