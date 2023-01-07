"""
Ejemplo sencillo de listas
"""

bicycles = ['trek' , 'cannondale' , 'redline' , 'specialized']
print (bicycles)

"""Acceder a elementos de una lista"""

bicycles = ['trek' , 'cannondale' , 'redline' , 'specialized']
print (bicycles[0])
print (bicycles[1])
print (bicycles[2])
print (bicycles[3])

"""Al añadir .title aparecera el dato de la lista en MAYUSCULAS"""

bicycles = ['trek' , 'cannondale' , 'redline' , 'specialized']
print (bicycles[0].title())

""" Sintaxis especial para acceder al ultimo elemento de una lista con -1 """

bicycles = ['trek' , 'cannondale' , 'redline' , 'specialized']
print (bicycles[-1].title())  # Ultimo elemento
print (bicycles[-2].title())  # Penultimo elemento
print (bicycles[-3].title())  # antepenultimo elemento

""" Podemos usar cadenas (f) para crear un mensaje usando un valor de la lista """

bicycles = ['trek' , 'cannondale' , 'redline' , 'specialized']
message = f'My first bcycle was a {bicycles[0].title()}'
print (message)

bicycles = ['trek' , 'cannondale' , 'redline' , 'specialized']
message = f'My second bcycle was a {bicycles[-1].title()}'
print (message)