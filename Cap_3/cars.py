""" Ordenar lista de manera permanente con el metodo sort()"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print (cars)

""" Ordenar en orden alfabetico inverso """

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print (cars)

""" Ordenar una lista temporalmente con la funcion sorted() """

cars = ['bmw', 'audi', 'toyota', 'subaru']

print ('Here is the original list: ')
print (cars)

print ('\nHere is the sorted list: ')
print (sorted(cars))

print ('\nHere is the original list again: ')
print (cars)

print ('\nHere is the sorted reverse list: ')
print (sorted(cars, reverse=True))

""" Imprimir una lista en orden inverso """

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print (cars)

""" Descubrir la longitud de una lista """

cars = ['bmw', 'audi', 'toyota', 'subaru']
print (len(cars))

""" """
