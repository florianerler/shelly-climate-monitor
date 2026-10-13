import requests
import time

#def abfrage():
#a = requests.get("https://httpbin.org/get", timeout=5)
#return (a.status_code, a.json())

def auswertung(wert):
    temperatur = wert["temperature:0"]["tC"]
    luftfeuchtigkeit = wert["humidity:0"]["rh"]
    
    print(f"temperatur: {temperatur} °C")
    print(f"luftfeuchtigkeit: {luftfeuchtigkeit} %")
    
testdaten = {
    "temperature:0": {"tC": 22.4},
    "humidity:0": {"rh": 48.5}
}
    

#while True:
 #   try:
  #      print("Versuche Verbindung herzustellen...")
  #      ergebnis=abfrage()
  #      auswertung(ergebnis[1])
        
   # except requests.exceptions.RequestException:
   #     print("Verbindung fehlgeschlagen!")
   #    print("Nächster Versuch in 60 Sekunden..")
        
auswertung(testdaten)        
        
#    time.sleep(60)
    