# Lista je kolekcija podataka koji su poredani. Lista je promjenjiva i može imati iste članove (duplikate).

# Kreiranje liste
brojevi = [1, 2, 3, 4, 5]
imena = ['Marko', 'Ivana', 'Sanja', 'Leo']

# Korištenje konstruktora
# brojevi2 = list((1, 2, 3, 4, 5))

# Dohvaćanje vrijednosti
print(imena[1])

# Dužina liste
print(len(imena))

# Dodavanje na kraj liste, append
imena.append('Dario')

# Uklanjanje članova liste
imena.remove('Leo')

# Mijenjanje redoslijeda članova liste
imena.reverse()

# Mijenjanje vrijednosti članova liste
imena[0] = 'Janko'

print(imena)