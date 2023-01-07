"""
Demasiados espacios en blanco en un programa puede resultar confusos
"""

# Eliminar espacios en blanco a la derecha

favorite_language =' Python '
favorite_language.rstrip()
print (f'Elimina espacio a la derecha \n{favorite_language}')

# Eliminar espacios en blanco a la izquierda

favorite_language =' Python '
favorite_language.lstrip()
print (f'Elimina espacio a la izquierda \n{favorite_language}')

# Eliminar espacios en blanco a ambos lados al mismo tiempo

favorite_language =' Python '
favorite_language.strip()
print (f'Elimina espacio a ambos lados \n{favorite_language}')