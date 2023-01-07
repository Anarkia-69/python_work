""" Sentencias if """

cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print (car.upper())
    else:
        print (car.title())

"""" Ignorar mayusculas y minusculas al comprobar una igualdad """

cars = ['audi','Bmw','subaru','toyota']

for car in cars:
    if car.lower() == 'bmw':     # Aqui esta la diferencia .lower()
        print (car.upper())
    else:
        print (car.title())