# Klasa je nacrt za kreiranje objekata. Objekt ima svoja svojstva i metode (funkcije). Gotovo sve u Pythonu je objekt

# Kreiranje klase
class Pas:
    # Konstruktor
    def __init__(self, vrsta, ime, boja, tezina):
        self.vrsta = vrsta
        self.ime = ime
        self.boja = boja
        self.tezina = tezina

    def spava(self):
        return f'ZZZZZ kaže {self.ime} dok spava i ima {self.tezina} kila'

    def pojeo_rucak(self):
        self.tezina = self.tezina + 1

# Extendanje klase
class PolicijskiPas(Pas):
    # Konstruktor
    def __init__(self, vrsta, ime, boja, tezina):
        self.vrsta = vrsta
        self.ime = ime
        self.boja = boja
        self.tezina = tezina
        self.godineIskustva = 0

    def zabiljezi_iskustvo(self, godineIskustva):
        self.godineIskustva = godineIskustva

    def spava(self):
        return f'ZZZZZ kaže {self.ime} dok spava i ima {self.tezina} kila. Neka se odmara jer ima {self.godineIskustva} godina rada iza sebe.'

# Init objekta Pas
floki = Pas('ovčar', 'Floki', 'smeđa', 15)
floki.pojeo_rucak()

# Init objekta policijski pas
garo = PolicijskiPas('doberman', 'Garo', 'crna', 20)
garo.zabiljezi_iskustvo(10)

print(garo.spava())