""" Trabajar con parte de una lista
    Partir una lista """

players =['charles','martina','michael','florence','eli']
print (players[0:3])

players =['charles','martina','michael','florence','eli']
print (players[1:4])

""" Si omitimos el primer indice en un trozo """

players =['charles','martina','michael','florence','eli']
print (players[:4])

""" Si queremos que incluya el final de la lista """

players =['charles','martina','michael','florence','eli']
print (players[1:])

""" Si queremos los tres ultimos jugadores """

players =['charles','martina','michael','florence','eli']
print (players[-3:])

""" Pasar en bucle por un trozo """

players = ['charles','martina','michael','florence','eli']

print ('Here are the first three players on my team:')
for player in players[:3]:
    print (player.title())

