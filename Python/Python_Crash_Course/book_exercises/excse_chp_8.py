

    #8-1. Message:

#Escriba una función llamada mostrar_mensaje() que imprima una oración que diga a todos lo que está aprendiendo en este capítulo. 
# Llame a la función y asegúrese de que el mensaje se muestre correctamente.
def mostrar_mensaje():
     """Mustra lo aprendo"""
     print("Tu Estas Aprendiendo Python")
mostrar_mensaje()








    #8-2. Favorite Book:

#Escribe una función llamada libro_favorito() que acepte un parámetro, título.
# La función debe imprimir un mensaje, como Uno de mis libros favoritos es Alicia en el país de las maravillas.
# Llame a la función, asegurándose de incluir el título de un libro como argumento en la llamada a la función.
def favorite_book(title):
    """Libros favoritos"""
    print(f"Mi libro favorito es {title.title()}.")
favorite_book('El viejo y el mar')








    #8-3. T-Shirt:

#Escriba una función llamada hacer camisa() que acepte un tamaño y el texto de un mensaje que debe imprimirse en la camisa. 
# La función debe imprimir una oración que resuma el tamaño de la camisa y el mensaje impreso en ella.

#Llame a la función una vez usando argumentos posicionales para hacer una camisa. 
# Llame a la función por segunda vez usando argumentos de palabras clave.
def camisa(tamaño, texto):
    """texto en camisa"""
    print(f"Camisa tamaño {tamaño}, con texto: {texto}")

camisa("'ch'", "Guitar Hero")
camisa(tamaño="Large", texto="'Opnipotente'")









    #8-4. Large Shirts:

#Modificar la función make_shirt() para que las camisetas sean grandes por defecto con un mensaje que dice Me encanta Python. 
# Haz una camiseta grande y una camiseta mediana con el mensaje predeterminado y una camiseta de cualquier tamaño con un mensaje diferente.
def make_shirt(texto='Me encanta Python', tamaño='Large'):
    """creando camisas"""
    print(f"Camisa tamaño {tamaño}, con texto: {texto}")

make_shirt()
make_shirt(tamaño='mediana')
make_shirt('Parangaricutirinicuaro', 'chica')











    #8-5. Cities:

#Escribe una función llamada describe_city() que acepte el nombre de una ciudad y su país. 
# La función debe imprimir una oración simple, como Reykjavik está en Islandia.
#  Asigne al parámetro para el país un valor predeterminado. 
# Llame a su función para tres ciudades diferentes, al menos una de las cuales no se encuentra en el país predeterminado.
def describe_city(ciudad, pais='Mexico'):
    """Descripcion de ciudades"""
    print(f"La ciudad {ciudad.title()}, se encuentra en el pais {pais}")

describe_city('campeche')
describe_city('merida')
describe_city('nueva york', 'EUA')





