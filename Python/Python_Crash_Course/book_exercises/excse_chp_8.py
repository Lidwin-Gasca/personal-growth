

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