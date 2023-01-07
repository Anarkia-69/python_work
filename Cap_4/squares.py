""" Usar range() con variable temporal"""

squares = []
for value in range (1,100):
    square = value**2
    squares.append(square)
print (squares)

""" Estadisticas sencilla con una lista de numeros range() """

value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print (min(value))
print (max(value))
print (sum(value))

"""" Listas por compresion, en una sola linea de codigo """

squares = [value**2 for value in range(1,11)]
print (squares)