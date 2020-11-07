# Funkcija je blok koda koji se izvršava samo onda kad je funkcija pozvana. 
# Za označavanje funkcije koristimo uvlake, odnosno tipku tab.

# Kreiranje funkcije
def reciBok(ime = 'netko'):
    print(f'Bok, {ime}!')

# Povratne vrijednosti
def zbroji(a, b):
    zbroj = a + b
    return zbroj

X = zbroji(2, 3)
print(X)