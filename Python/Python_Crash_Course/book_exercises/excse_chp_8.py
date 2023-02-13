

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





    #8-6. City Names:

#Escribe una función llamada city country() que tome el nombre de una ciudad y su país. 
# La función debería devolver una cadena/string con el formato siguiente:
#
#           >>> "Santiago, Chile"
#
#Llame a su función con al menos tres pares de ciudades y países e imprima los valores que se devuelven.
def city_country(city, country):
    """Takes the name and country, and formats it"""
    formatted_city_country = f"{city.title()} {country.title()}"
    return formatted_city_country

place = city_country("santiago", 'chile')
print(place)











    #8-7. Album:

#Escriba una función llamada make_album() que cree un diccionario que describa un álbum de música. 
# La función debe tomar el nombre de un artista y el título de un álbum, y debe devolver un diccionario que contenga estos dos datos. 
# Utilice la función para crear tres diccionarios que representen diferentes álbumes. 
# Imprima cada valor de retorno para mostrar que los diccionarios están almacenando la información del álbum correctamente.

#Use Ninguno para agregar un parámetro opcional para hacer album() que le permita almacenar la cantidad de canciones en un álbum. 
# Si la línea de llamada incluye un valor para el número de canciones, agregue ese valor al diccionario del álbum. 
# Realice al menos una nueva llamada de función que incluya la cantidad de canciones en un álbum.

















    #8-8. User Albums:

#Comience con su programa del ejercicio 8-7. Escriba un ciclo while que 
# permita a los usuarios ingresar el artista y el título de un álbum. 
# Una vez que tenga esa información, llame a make_album() con la entrada del usuario e imprima el diccionario que se crea. 
# Asegúrese de incluir un valor de salida en el ciclo while.






