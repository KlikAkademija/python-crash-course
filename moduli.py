# Modul je zapravo datoteka koji sadrži skup funkcija koje želimo koristiti u nekoj aplikaciji. Postoje temeljni python moduli, moduli koje možemo instalirati korištenjem pip package managera i custom moduli

# Temeljni python moduli
import datetime
from datetime import date

import time
from time import time

# danas = datetime.date.today()
danas = date.today()

timestamp = time()
print(timestamp)

# pip moduli
from emoji import emojize
print(emojize('Python is my :red_heart:'))

# custom moduli
import provjeraUnosa
from provjeraUnosa import provjeriBrojIliString

unos = input('Unesi broj ili string: ')
provjeriBrojIliString(unos)
