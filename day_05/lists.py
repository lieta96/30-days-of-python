
# Level 1

#1
empty_list=[]

#2
more_than_five=[0,1,2,3,4,5,6]

#3
lenght_list=len(more_than_five)

#4
middle_index=lenght_list//2
first_item=more_than_five[0]
middle_item=more_than_five[middle_index]
print (middle_item)
last_item=more_than_five[lenght_list-1]
print(last_item)

#5
mixed_data_types=["Julieta",24,1.60,"a quien le importa", "Calle Wallaby 42 Sidney"]

#6
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]

#7
print (it_companies)

#8
print (len(it_companies))

#9
print (f'Primera empresa: {it_companies[0]}')
print (f'Empresa del medio: {it_companies[len(it_companies)//2]}')
print (f'Última compañía: {it_companies[len(it_companies)-1]}')

#10
it_companies[0]="Accenture"
print (it_companies)

#11
it_companies.append('Sony')
print (it_companies)

#12
it_companies.insert(len(it_companies)//2,"ARSAT")
print (it_companies)

#13
it_companies[0]= it_companies[0].upper()
print (it_companies)

#14
print(' # '.join(it_companies))

#15
print (f'"Sony está dentro de la lista?: {"Sony" in it_companies}')

#16
it_companies.sort()
print (it_companies)

#17
it_companies.sort(reverse=True)
print (it_companies)

#18
print(it_companies[3:])

#19
print(it_companies[0:-3])

#20
print(f'Lista completa: \t\t{it_companies}')
it_companies.pop(len(it_companies)//2)
print (f'Lista sin el elemento del medio: {it_companies}')

#21
it_companies.pop(0)
print(it_companies)

#22 igual que 20

#23
it_companies.pop()
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25 idem anterior

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print (front_end+back_end)

#27
full_stack=front_end.copy()+back_end.copy()
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)

# Level 2
