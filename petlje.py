# For petlja se koristi za iteriranje kroz sekvencu s točno određenim brojem članova 
# (listu, n-torku, riječnik, set ili string)

knjige = ['Zlatarevo zlato', 'Ježeva kućica', 'Gospodar prstenova', 'Zločin i kazna']
# Jednostavna for petlja
# for knjiga in knjige:
#     print(f'Trenutna knjiga: {knjiga}')

# Prekid/break
# for knjiga in knjige:
#     if knjiga == 'Gospodar prstenova':
#         break
#     print(f'Trenutna knjiga: {knjiga}')

# Continue
# for knjiga in knjige:
#     if knjiga == 'Gospodar prstenova':
#         continue
#     print(f'Trenutna knjiga: {knjiga}')

# Raspon/range
# for i in range(0, 10, 1):
#     print(i)
# for i in range(len(knjige)):
#     print(knjige[i])

# While petlja izvršava skup naredbi dok je njezin uvjet istinit
i = 10
while i > 0:
    print(i)
    i = i - 1 #i -= 1
