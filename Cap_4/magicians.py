""" Pasar por un bucle por una lista completa """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

""" Sacar mas partido a un bucle for """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was the great trick!')

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was the great trick!')
    print(f'I can not wait to see your next trick, {magician.title()}.\n')   

""" Hacer algo despues de un bucle for """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was the great trick!')
    print(f'I can not wait to see your next trick, {magician.title()}.\n')   
print('Thank you, everyone. That was a great magic show!')

""" Olvidar sangrar lineas adicionales """

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was the great trick!')
print(f'I can not wait to see your next trick, {magician.title()}.\n')  

