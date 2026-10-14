import unittest
from shelly_monitor import komfort
from shelly_monitor import feuchtigkeitsbewertung
from shelly_monitor import auswertung

class TestKomfort(unittest.TestCase):
    def test_komfort_normal(self):
        wert = 21
        tatsächlicher_wert = komfort(wert)
        erwarteter_wert = "komfort"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
    
    def test_komfort_kalt(self):
        wert = 17
        tatsächlicher_wert = komfort(wert)
        erwarteter_wert = "zu kalt"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
    def test_komfort_warm(self):
        wert = 25
        tatsächlicher_wert = komfort(wert)
        erwarteter_wert = "zu warm"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
    def test_komfort_unterer_grenzwert(self):
        wert = 19
        tatsächlicher_wert = komfort(wert)
        erwarteter_wert = "komfort"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
    def test_komfort_oberer_grenzwert(self):
        wert = 23
        tatsächlicher_wert = komfort(wert)
        erwarteter_wert = "komfort"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
class TestFeuchtigkeitsbewertung(unittest.TestCase):
    def test_feuchtigkeitsbewertung_normal(self):
        wert = 50
        tatsächlicher_wert = feuchtigkeitsbewertung(wert)
        erwarteter_wert = "optimal"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
    def test_feuchtigkeitsbewertung_feucht(self):
        wert = 80
        tatsächlicher_wert = feuchtigkeitsbewertung(wert)
        erwarteter_wert = "zu feucht"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
    def test_feuchtigkeitsbewertung_trocken(self):
        wert = 20
        tatsächlicher_wert = feuchtigkeitsbewertung(wert)
        erwarteter_wert = "zu trocken"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
    def test_feuchtigkeitsbewertung_oberer_grenzwert(self):
        wert = 65
        tatsächlicher_wert = feuchtigkeitsbewertung(wert)
        erwarteter_wert = "optimal"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
    def test_feuchtigkeitsbewertung_unterer_grenzwert(self):
        wert = 35
        tatsächlicher_wert = feuchtigkeitsbewertung(wert)
        erwarteter_wert = "optimal"
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
class TestAuswertung(unittest.TestCase):
    def test_auswertung(self):
        wert = {"temperature:0": {"tC": 20}, "humidity:0": {"rh": 50}}
        tatsächlicher_wert = auswertung(wert)
        erwarteter_wert = (20, 50)
        self.assertEqual(tatsächlicher_wert, erwarteter_wert)
        
        