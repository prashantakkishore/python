# Dictionaries {}

dict1 = {'name': 'pks', 'city': 'Lucknow'}
print(type(dict1))  # <class 'dict'>

names_ages = [('pks', 32) , ('kkd' , 22) , ('dds' , 44)]
dict2 = dict(names_ages)
print(dict2) # {'pks': 32, 'kkd': 22, 'dds': 44}


for k, v in dict1.items():
    print(k, ":", v)

# GET
print(dict1['name'])  # pks
print(dict1['city'])  # Lucknow

# ADD
dict1['country'] = 'India'
print(dict1) # {'name': 'pks', 'city': 'Lucknow', 'country': 'India'}

# UPDATE
dict1['country'] = 'USA'
print(dict1) # {'name': 'pks', 'city': 'Lucknow', 'country': 'USA'}

# DELETE
del dict1['country']
print(dict1) # {'name': 'pks', 'city': 'Lucknow'}
