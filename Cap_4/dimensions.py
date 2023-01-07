""" Tuplas , Definir una Tupla"""

dimensions = (200,50)

print (dimensions[0])
print (dimensions[1])

""" Pasar en bucle por todos los valores de una tupla """

dimensions = (200,50)

for dimension in dimensions:
    print (dimension)

"""" Sobreescribir una tupla """

dimensions = (200,50)
print ('Original dimensions: ')
for dimension in dimensions:
    print (dimension)

dimensions = (400,100)
print ('\nModified dimensions: ')
for dimension in dimensions:
    print (dimension)   

""" Ejercicio Pruebelo 4_13 """    

comidas_basicas = ('arroz','pasta','pure','potaje','churrasco')
for comida in comidas_basicas:
    print (comida)

print ('\nLas comidas basicas han cambiado. \nEstas son las nuevas:\n')    


comidas_basicas = ('arroz','papas','pure','pollo carbonara','churrasco')

for comida in comidas_basicas:
    print (comida)

