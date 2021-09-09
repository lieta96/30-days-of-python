#Level 1

empty_tpl=()

#2
sisters=('Noelia', 'Amanda')
brothers=('Francisco', "Julián")

#3
siblings= sisters+brothers

#4
numer_of_siblings=len(siblings)

#5
list_siblings=list(siblings)
list_siblings.append('Blanca')
list_siblings.append('Adrían')
family_members=tuple(list_siblings)
print (family_members)

#Level 2

#1
siblings_unpack=family_members[0:4]
parents_unpack=family_members[-2:]
print (parents_unpack)

#2
fruits=("frutilla","arándanos","frambuesa")
vegetables=("rúcula","morrón","zanahoria")
animals=("gatos", "tortuga","pingüino","carpincho")
food_stuff_tp=fruits+vegetables+animals

#3
food_stuff_lt=list(food_stuff_tp)

#4
food_stuff_lt.pop(len(food_stuff_lt)//2)
print (food_stuff_lt)

#5
del food_stuff_lt[:3]
del food_stuff_lt[-3:]
print(food_stuff_lt)

#6
del food_stuff_lt

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print (f'"Estonia" es un país nórdico? {"Estonia" in nordic_countries}')
print (f'"Iceland" es un país nórdico? {"Iceland" in nordic_countries}')