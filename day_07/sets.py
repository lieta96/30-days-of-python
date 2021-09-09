#Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ages = [22, 19, 24, 25, 26, 24, 25, 24]

#1
len(it_companies)

#2
it_companies.add("Twitter")

#3
print(it_companies)
it_companies.pop()
print(it_companies)

#4
#La diferencia entre remove y discard es que si el elemento que queremos eliminar no está en el conjunto, entonces "remove" nos dará error, mientas que "discard" no. 

#Level 2
#1
C=A.union(B)

#2
A_intersection_B=A.intersection(B)
print(A_intersection_B)

#3
print(f'{A} es un subconjutno de {B}? {A.issubset(B)}')

#4
print(f'{A} es disjunt con {B}? {A.isdisjoint(B)}')

#5
A.update(B)

#6
print(f'La diferencia simétrica entre {A} y {B} es: {A.symmetric_difference(B)}')
#Ahora me da vacío porque A contiene todos los elementos de B

#7
del A
del B

#Level 3

#1
set_ages=set(ages)
print (len(set_ages),">",len(ages),"?", len(set_ages)>len(ages))

#2
#String: es una cadena de caracteres.
#List: es una colección de elementos ordenados que puede modificarse. A su vez, permite elementos repetidos.
#Tuple: es una coleccón de elementos ordenados e inmutables.
#Set: es una colección de elementos desordenados que puede modificarse, y no permite elementos repetidos.

#3
sentence= "I am a teacher and I love to inspire and teach people"
list_words=sentence.split()
set_words=set(list_words)
print(f'La cantidad de palabras distintas que hay en la frase "{sentence}" es {len(set_words)}')

