
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

#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age=ages[0]
max_age=ages[len(ages)-1]
print(f'Menor edad: {min_age}')
print(f'Mayor edad: {max_age}')
middle_age=ages[len(ages)//2]
print(f'Edad media: {middle_age}')
sum_ages=0
for age in ages:
    sum_ages+=age
print (sum_ages)
average_age=sum_ages/len(ages)
print(average_age)
range_ages=max_age-min_age
print(abs(min_age-average_age))
print(abs(max_age-average_age))

# 1 Countries 
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#Find the middle countries
print(f'La cantidad de países es par? {len(countries)%2==0==True}')
print (len(countries))
middle_countrie_number=len(countries)//2
middle_country=countries[middle_countrie_number]
print(middle_country)

#2
first_countries=countries[0:middle_countrie_number]
last_countries=countries[middle_countrie_number:len(countries)]
print(len(last_countries))

#3
new_countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China,Rusiua,USA,*scandic=new_countries
print(scandic)
print(China)


