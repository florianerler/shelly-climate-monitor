import requests
import time

def abfrage():
    a = requests.get("https://httpbin.org/get", timeout=5)
    return (a.status_code, a.json())

def auswertung(wert):
    print(wert["url"])
    
    



while True:
    try:
        print("Versuche Verbindung herzustellen...")
        ergebnis=abfrage()
        auswertung(ergebnis[1])
        
    except requests.exceptions.RequestException:
        print("Verbindung fehlgeschlagen!")
        print("Nächster Versuch in 60 Sekunden..")
        
        
        
    time.sleep(60)
    