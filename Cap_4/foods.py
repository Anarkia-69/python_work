""" Copiar una lista """
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods [:]

print('my favorite foods are:')
print(my_foods)

print('\nMy friends favorite foods are:')
print(friends_foods)

""" Añadiremos una nueva comida a cada lista con .append() """

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods [:]
my_foods.append('cannoli')
friends_foods.append('ice cream')

print('my favorite foods are:')
print(my_foods)


print('\nMy friends favorite foods are:')
print(friends_foods)

""" Omitiendo la copia de la lista por un igual a = """

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods 
my_foods.append('cannoli')
friends_foods.append('ice cream')

print('my favorite foods are:')
print(my_foods)


print('\nMy friends favorite foods are:')
print(friends_foods)