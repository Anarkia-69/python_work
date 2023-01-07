""" Modificar elemntos de una lista """

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

""" Cambiar el primer valor de la lista """

motorcycles[0] = 'ducati'
print (motorcycles)

""" Adjuntar elemntos al final de una lista """

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

motorcycles.append('ducati')
print (motorcycles)

""" El metodo .append() facilita la creacion dinamica de listas. """

motorcycles = []
motorcycles.append('ducati')
motorcycles.append('honda')
motorcycles.append('yamaha')
print (motorcycles)

"""" Insertar elementos en una lista en una posicion determinada """

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')

""" Eliminar elementos de una lista """

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

del motorcycles[-1]
print(motorcycles)

"""" Eliminar un elemento con el metodo pop()"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

popped_motorcycle = motorcycles.pop()
print (motorcycles)
print (popped_motorcycle)

""" Eliminar un elemento por valor con el metodo remove()"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)

motorcycles.remove('ducati')
print (motorcycles) 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print (motorcycles)
print(f'\nA {too_expensive.title()} is to expensive for me. ')

