#30 Days Of Python: Day 3 - Operators

# Ejercicios 1 a 3
age= 24
print ('Edad:', age)
height_own= 1.58
print ('Altura:', height_own)
complex_number= 4+ 1j

#Área de un triángulo
print ('Número complejo elegido:', complex_number)
base= float(input ('Calcularemos el área de un triángulo.ngrese la base:'))
height= float(input ('Gracias! Ahora ingrese la altura:'))
print ('El área del triángulo es', base*height*0.5)

#Perímetro de un triángulo
side_a=float(input('Ahora calcularemos el perímetro de un triángulo. Ingresa la medida de un lado:'))
side_b=float(input('Ahora ingresa la medida del segundo lado:'))
side_c=float(input('Gracias! Ingresá la medida del tercer lado:'))
perimeter=side_a+side_b+side_c
print ('EL perímetro del triángulo es',perimeter )

Área y perímetro de un rectángulo
print ('Calcularemos el área y el perímetro de un rectángulo')
width= float(input('Ingresa el valor de la base:'))
lenght=float(input('Ingresá la altura:'))
area_rectangle=width *lenght
perimeter_rectangle=width*2+lenght*2
print (f'El área del rectángulo es {area_rectangle} y el perímetro es {perimeter_rectangle}')

#Área y perímetro de una circunferencia
print ('Calcularemos el área y el perímetro de una circunferencia')
radius= float(input('Ingresa el radio de la circunferencia'))
area_circle= 3.14* (radius**2)
perimeter_circle=3.14*radius*2
print (f'El área de la circunferencia de radio {radius} es {area_circle} y el perímetro es {perimeter_circle}')

#Intersección con el eje x e y, y la pendiente
slope_1=2 #y=2x-2
int_y=-2
int_x=1

#Dados (2,2) y (6,10), calcular la pendiente y la disntacia euclidea
x1=2
x2=6
y1=2
y2=10
dist_x=x2-x1
dist_y=y2-y1
slope_2=dist_x/dist_y
euclidean_distance=pow (dist_x**2+dist_y**2,0.5)

print (f'La pendiente 1 es mayor que la pendietne 2?: {slope_1<slope_2}')

x_value=float(input('Dada la función y = x^2 + 6x + 9, ingrese un valor de x'))
print (f'El valor de y es{x_value**2+6*x_value+9}')

print (len('python') < len('dragon')) #false

print ('on' in 'python' and 'on' in 'dragon')

print ('jargon' in 'I hope this course is not full of jargon')

float_python=float (len('phyton'))
str_python=str(float_python)
print (type(str_python))

#Pares e imapres
even_or_not=float(input('Ingrese un número entero:'))
print(f'El número ingresado es par? {even_or_not%2==0}')

print (7//3==int(2.7))

print (type('10')==type(10))
print (int('9.8')==10)

hours=float(input('Ingresa la cantidad de horas que trabajás en el día:'))
rate=float(input('Cuánto ganás por cada hora de trabajo?'))
print (f'En la semana ganás {rate*hours*5}')

years=float(input('Qué edad tenés?'))
print (f'Viviste {years*60*60*24*365} segundos')

for number in [1,2,3,4,5]:
    print (f'{number} {number**0} {number**1} {number**2} {number**3}')