import requests
import time
from config import SHELLY_IP

def abfrage():
    a = requests.get(f"http://{SHELLY_IP}/rpc/Shelly.GetStatus", timeout=5)
    return (a.status_code, a.json())

def auswertung(wert):
    temperatur = wert["temperature:0"]["tC"]
    luftfeuchtigkeit = wert["humidity:0"]["rh"]
    
    print(f"temperatur: {temperatur} °C")
    print(f"luftfeuchtigkeit: {luftfeuchtigkeit} %")
    return (temperatur, luftfeuchtigkeit)

def komfort(wert):
    if wert  <19:
        return("zu kalt")
    elif wert >23:
        return("zu warm")
    else:
        return("komfort")

def feuchtigkeitsbewertung(wert):
    if wert <35:
        return("zu trocken")
    elif wert >65:
        return("zu feucht")
    else:
        return("optimal")
    
if __name__ == "__main__":
    while True:
        try:
            print("Versuche Verbindung herzustellen...")
            ergebnis=abfrage()
            messwerte=auswertung(ergebnis[1])
            print(messwerte)
            komfortstatus=komfort(messwerte[0])
            print(komfortstatus)
            feuchtigkeitsstatus=feuchtigkeitsbewertung(messwerte[1])
            print(feuchtigkeitsstatus)

        except requests.exceptions.RequestException:
            print("Verbindung fehlgeschlagen!")
            print("Nächster Versuch in 30 Sekunden..")  
        
        time.sleep(30)

    
