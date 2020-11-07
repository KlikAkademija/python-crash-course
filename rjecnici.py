# Rječnik je kolekcija koja je neporedana, promjenjiva i indeksirana. Ne dopušta duplikate.

# Kreiranje rječnika
igrac = {
    'ime' : 'Marko',
    'lozinka': '1234',
    'bodovi' : 100
}

# Konstruktor
# igrac2 = dict(ime='Ivana', lozinka='aaaabb')

# Dohvaćanje vrijednosti
print(igrac['ime'])
print(igrac.get('lozinka'))

# Dodavanje para ključ-vrijednost
igrac['nadimak'] = 'MK'

# Svi ključevi
print(igrac.keys())

# Svi članovi
print(igrac.items())
 
# Kopiranje rječnika
igrac3 = igrac.copy()
igrac3['kredit'] = 1000

# Uklanjanje članova
del(igrac['nadimak'])
igrac.pop('lozinka')

# Čišćenje cijelog sadržaja
igrac.clear()

# Dužina rječnika
print(len(igrac3))
