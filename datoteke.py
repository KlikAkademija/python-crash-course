# S Pythonom možemo kreirati i brisati datoteke, kao i čitati iz njih te ih modificirati/update-ati.

# Otvaranje datoteke
mojaDat = open('mojaDatoteka.txt', 'w')

# Info o datoteci
print('Ime: ', mojaDat.name)
print('Je zatvorena: ', mojaDat.closed)
print('Način otvaranja: ', mojaDat.mode)

# Pisanje u datoteku
mojaDat.write('Divan je dan')
mojaDat.write(' za programiranje')
mojaDat.close()

# Dodavanje u datoteku
mojaDat = open('mojaDatoteka.txt', 'a')
mojaDat.write(' i gledanje videa o Pythonu')
mojaDat.close()

# Čitanje iz datoteke
mojaDat = open('mojaDatoteka.txt', 'r+')
tekst = mojaDat.read(50)
print(tekst)