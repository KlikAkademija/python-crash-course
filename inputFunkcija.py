# Napisati program koji od korisnika traži unos cijelog broja. Ako je uneseni broj >10 ispisati poruku VEĆI, 
# ako je uneseni broj manji od 10 ispisati MANJI, a za broj 10 ispisati DESET.

unos = int(input('Unesi jedan cijeli broj: '))

if unos > 10:
    print('VEĆI')
elif unos < 10:
    print('MANJI')
else:
    print('DESET')