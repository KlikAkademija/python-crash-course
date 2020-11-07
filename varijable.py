# Varijabla je mjesto za pohranu vrijednosti koje mogu biti različitih tipova 
'''
Ovo je 
komentar u više redaka
ili docstring
Možemo koristiti tri jednostruka ili dvostruka navodnika
'''

"""
PRAVILA IMENOVANJA:
- imena varijabli su case sensitive (ime i IME su različite varijable)
- moraju početi sa slovom ili donjom crtom _
- mogu sadržavati brojeve, ali ne mogu početi s brojem
"""

'''a = 5         # int
b = 6.5       # float
ime = 'Marko' # str
je_otvoren = True # bool'''

a, b, ime, je_otvoren = (5, 6.5, 'Marko', True)

# Matematičke operacije
x = a+b

# Casting
a = str(a) #'5'
b = int(b)
c = float(b)

print(type(c), c)
