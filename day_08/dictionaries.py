dog={}
dog['name']='Mafalda'
dog['color']='castaño'
dog['breed']='boxer'
dog['legs']=True
dog['age']=13
print (dog)

student={
    'first_name': 'Lucrecia',
    'career':'Web Development',
    'specialization':'Frontend Development',
    'age':26,    
    'skills':['HTML', 'CSS','JavaScript','React']
}
len(student)
student_skills=(student['skills'])
print(type(student_skills))
student_skills.append('Angular')
print(student['skills'])
keys=student.keys()
values=student.values()
student.items()
student.pop('age')
print(student)
del dog