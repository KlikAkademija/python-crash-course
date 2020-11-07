# N-torka je kolekcija članova koja je poredana i nepromjenjiva. Dopušta duplikate.
# Kreiranje n-torke
imena = ('Marko', 'Ivana', 'Sanja')
# imena2 = tuple(('Marko', 'Ivana', 'Sanja'))

# N-torka s jednim članom
imena2 = ('Marko', )

# Dohvaćanje vrijednosti
print(imena[1])

# Ne možemo mijenjati vrijednost članova
# imena[0] = 'Janko'

# Brisanje n-torke
del imena2

# Duljina n-torke
print(len(imena))

# Set je kolekcija članova koja je neporedana i neindeksirana. Ne dopušta duplikate.
# Kreiranje seta
imena_set = {'Marko', 'Ivana', 'Sanja'}

# Provjera je li podatak u setu
# print('Marko' in imena_set)

# Dodavanje u set
imena_set.add('Leo')

# Dodavanje duplikata
imena_set.add('Marko')

# Uklanjanje iz seta
imena_set.remove('Marko')

# Uklanjanje svih članova
imena_set.clear()

# Brisanje seta
del imena_set
print(imena_set)