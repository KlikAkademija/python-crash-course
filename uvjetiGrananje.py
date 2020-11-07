# If/else narebe se koriste kako bi se dio programa izvršio ili ne na temelju toga je li neki uvjet istinit, True ili lažan, False
a = 50
b = 10

# Operatori usporedbe (==, !=, >, <, >=, <=) – koriste se za usporedbu vrijednosti
# # Jednostavna if naredba
# if a > b:
#     print(f'{a} je veće od {b}')

# # If/else naredba
# if a > b:
#     print(f'{a} je veće od {b}')
# else:
#     print(f'{b} je veće od {a}')

# elif naredba
# if a > b:
#     print(f'{a} je veće od {b}')
# elif a == b:
#     print(f'{a} je jednako {b}')
# else:
#     print(f'{b} je veće od {a}')

# Logički operatori (and, or, not) – koriste se za izradu složenih uvjeta
# # and
# if a > 0 and a <= 20:
#     print(f'{a} je veći od 0 i manji ili jednak 20')

# # or
# if a > 0 or a <= 20:
#     print(f'{a} je veći od 0 ili manji ili jednak 20')

# not
if not(a == b):
    print(f'{a} nije jednak {b}')

