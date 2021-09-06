#1
strings=['Thirty','Days','Of','Python']
print (' '.join(strings))

#2
strings_2=['Coding', 'For' , 'All' ]
print (' '.join(strings_2))

#3, 4, 5, 6, 7
company=  "Coding For All"
print (company)
print (len(company))
print (company.upper())
print (company.lower())

#8
company_2 ="Coding For ALL"
print (company_2.capitalize())
print (company_2.title())
print (company.swapcase())

#9
print (company_2[1:])

#10
print (company_2.find("Coding"))

#11
company_3=company_2.replace("Coding", "Python")
print(company_3)

#12
company_4=company_3.replace("ALL", "Everyone")
print (company_4)

#13
print(company_2.split())

#14
companies="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print (companies.split(','))

#15
index_0=company_2[0]
print (index_0)

#16
last_index=len(company_2)-1
print (last_index)

#17
index_10=company_2[10]

#18
split_company_4=company_4.split()
print (f'{split_company_4[0][:1]}.{split_company_4[1][:1]}.{split_company_4[2][:1]}.:{company_4}')

#19
split_company_3=company_3.split()
print (f'{split_company_3[0][:1]}.{split_company_3[1][:1]}.{split_company_3[2][:1]}.:{company_3}')

#20
print(company_2.find('C'))

#21
print(company_2.find('F'))

#22
print(company_2.rfind('L'))

#23
sentence= 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#24
print(sentence.rfind("because"))

#25
phrase="because because because"
print (f'You cannot end a sentence with {phrase} is a conjunction')

#26
#Igual que el 23

#27
print(f'Does {company_2} start with a substring _Coding_?:{company_2.startswith("Coding")}')

#28
print(f'Does {company_2} end with a substring _Coding_?:{company_2.endswith("Coding")}')

#29
tab='\tCoding for all\t'
print (f'{tab}, without the left and right trailing spaces: {tab.strip()}')

#30
variable='thirty_days_of_python'
print(f'{variable} returns True when we use the method isidentifier():{variable.isidentifier()} ')

#31
python_libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
sentence_python_libraries=' '.join(python_libraries)
print(sentence_python_libraries)

#32
print('py \nI am enjoying this challenge.\nI just wonder what is next.')

#33
print ('py \nName \t\tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki')

#34
print (f'sh \nradius = 10\narea = 3.14 * radius ** 2 \nThe area of a circle with radius 10 is 314 meters square.')

#35
a=8
b=6
print(f'{a}+{b}={a+b} \n{a}-{b}={a-b} \n{a}*{b}={a*b} \n{a}/{b}={a/b} \n{a}%{b}={a%b} \n{a}//{b}={a//b} \n{a}**{b}={a**b} ')

