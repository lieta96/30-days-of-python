#Level 1

#1
age= int(input('Enter your age: '))
if age>=18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18-age} more years to learn to drive.')

#2
print('Who is older (me or you)?')
your_age=int(input('Enter your age: '))
my_age=25
difference=your_age-my_age
if your_age==my_age :
    print('We have the same age! Happy quarter century')
elif difference==1:
    print('You are one year older than me')
elif difference>1:
    print(f'You are {difference} years older than me')
elif difference==-1:
    print('You are one year younger than me')

else: 
    print (f'You are {abs(difference)} years younger than me')

#3
num_a=input('Ingrese el primer número: ')
num_b=input('Ingrese el segundo número: ')
if num_a<num_b:
    print(f'{num_a}<{num_b}')
elif num_a>num_b:
    print(f'{num_a}>{num_b}')
else: print (f'{num_a}={num_b}')

##Level 2

#1 
grade=int(input('Ingresá tu calificación del examen: '))
if 80<=grade<=100:
    print('Tu calificación es A')
elif 80>grade>=70:
    print('Tu calificación es B')
elif 70>grade>=60:
    print('Tu calificación es C')
elif 60>grade>=50:
    print('Tu calificación es D')
else: print ('Tu calificación es F')

#2
month=input('Please enter the actual month: ').lower()
if month== 'september' or month=='october' or month=='november':
    print ('It is Autumn at the North Hemisphere')
elif month== 'december' or month=='january' or month=='february':
    print ('It is Winter at the North Hemisphere')
elif month== 'march' or month=='arpil' or month=='may':
    print ('It is Spring at the North Hemisphere')
elif month== 'june' or month=='july' or month=='august':
    print ('It is Summer at the North Hemisphere')
else: print ('Sorry, you enter a wrong month.')

#3
new_fruit= input('Cuál es tu fruta favorita? ').lower()
fruits=['banana','naranja','mango','limón']
if new_fruit in fruits:
    print(f'Tenemos {new_fruit} para ofrecerte!')
else: print (f'En este momento no tenemos {new_fruit}, volvé mañana!')

##Level 3
#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Calle Wallaby 42 Sidney',
        'zipcode': '02210'
    }
}
if person['skills']: 
    skills=person['skills']
    middle_skill= len(skills)//2
    print(f'{skills[middle_skill]}')
    if 'Python' in skills:
        print('This person studied Python')
        if 'JavaScript' in skills and 'React' in skills:
            print ('This person is a front end developer')
            if 'Node' in skills and 'MongoDB' in skills and 'Python' in skills:
                print ('This person is also a back end developer. So, this person is a full stack developer')
            else: print('I am not sure if this person is a back end develoepr')
        else: print('I am not sure if this person is a front end develoepr')
    else: print ('This person did not study python')
else: print('This person does not have skills')

if person['is_marred'] and person['country']=='Finland':
    print(f'{person["first_name"]} lives in {person["country"]} and he is married.')
else: print ('Some information is missing.')
