""" Comprobar si hay un valor en una lista """

banned_users = ['andrew','carolina','david']
user = 'david'

if user in banned_users:
    print (f'{user.title()}, you can post a response if you wish.')

else:
    print (f'{user.title()}, you can not post a response, registration please')

""" Comprobar si no hay un valor an la lista de registros """

banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in  banned_users:
    print (f'{user.title()}, you can not post a response, registration please')

else:
    print (f'{user.title()}, you can post a response, registration please')

"""Activada cuenta VSCODE con Tabnine y Github"""