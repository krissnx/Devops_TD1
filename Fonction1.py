from datetime import datetime
from datetime import date, timedelta
s = datetime.today().strftime('%Y-%m-%d')
print('La date actuelle est :', s)
print('Choisissez le nombre de jour à soustraire :')
jour = input()
assert type(jour) == int, "Ce n'est pas un entier"
print("Vous avez saisi :", jour,"jours")
print("Soustraction des jours ....")
td = timedelta(jour)
print("Résultat de la soustraction : ", s - td)

