# Stringovi u Pythonu su označeni jednostrukim ili dvostrukim navodnicima.
ime = 'Marko'
dob = 25

# Konkatenacija
# print('Bok moje ime je ' + ime + ' i imam ' + str(dob) + ' godina')

# Formatiranje stringova
# Pozicijski argumenti
# print('Moje ime je {ime} i imam {dob} godina'.format(ime=ime, dob=dob))
# F-stringovi
# print(f'Moje ime je {ime} i imam {dob} godina')

# Metode koje se mogu koristiti sa stringovima
s = 'klik akademija'
# Veliko početno slovo
print(s.capitalize())
# Velika slova
print(s.upper())
# Mala slova
print(s.lower())
# Duljina string
print(len(s))
# Zamjena
print(s.replace('akademija', 'online škola'))