

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
    formatted_city_country = f"{city} {country}"
    return formatted_city_country.title()

place = city_country("santiago", 'chile')
print(place)

place = city_country("cdmx", 'mexico')
print(place)

place = city_country("buenos aires", 'argentina')
print(place)









    #8-7. Album:

#Escriba una función llamada make_album() que cree un diccionario que describa un álbum de música. 
# La función debe tomar el nombre de un artista y el título de un álbum, y debe devolver un diccionario que contenga estos dos datos. 
# Utilice la función para crear tres diccionarios que representen diferentes álbumes. 
# Imprima cada valor de retorno para mostrar que los diccionarios están almacenando la información del álbum correctamente.

#Use Ninguno para agregar un parámetro opcional para hacer album() que le permita almacenar la cantidad de canciones en un álbum. 
# Si la línea de llamada incluye un valor para el número de canciones, agregue ese valor al diccionario del álbum. 
# Realice al menos una nueva llamada de función que incluya la cantidad de canciones en un álbum.
albumes = []

def make_album(name, artist=None, songs=None):
    """Returning a album"""
    album = {'name': name}
    if artist:
        album['artist'] = artist
    if songs:
        album['songs'] = songs
    
    albumes.append(album)
    return album

new_album = make_album('death bed','whisky hell child', 13)
new_album = make_album('residente','calle 13')
new_album = make_album('pamela chu','tangari')

for album in albumes:
    name = album['name']
    artist = album.get('artist', 'Unknown Artist')
    songs = album.get('songs', 'Unknown')
    print(f"\nAlbum: {name.title()}\nBand/Artist: {artist.title()}\nNumber of Songs: {songs}")


















    #8-8. User Albums:

#Comience con su programa del ejercicio 8-7. Escriba un ciclo while que 
# permita a los usuarios ingresar el artista y el título de un álbum. 
# Una vez que tenga esa información, llame a make_album() con la entrada del usuario e imprima el diccionario que se crea. 
# Asegúrese de incluir un valor de salida en el ciclo while.

albumes = []

def make_album(name, artist=None, songs=None):
    """Returning a album"""
    album = {'name': name}
    if artist:
        album['artist'] = artist
    if songs:
        album['songs'] = songs
    
    albumes.append(album)
    return album


while True:
    print("\n\t---Describa un album---")
    print("(ingrese la letra 'q' en cualquier momento para cerrar el programa)\n")

    n_album = input("El nombre del album: ")
    if n_album == 'q'.lower():
        break
    a_album = input("El artista/banda del album: ")
    if a_album == 'q'.lower():
        make_album(n_album)
        break
    s_album = input("Cuantas pistas/canciones tiene el album: ")
    if s_album == 'q'.lower():
        make_album(n_album, a_album)
        break
    make_album(n_album, a_album, s_album)

for album in albumes:
    name = album['name']
    artist = album.get('artist', 'Unknown Artist')
    songs = album.get('songs', 'Unknown')
    print(f"\nAlbum: {name.title()}\nBand/Artist: {artist.title()}\nNumber of Songs: {songs}")











    #8-9. Messages:

#Haz una lista que contenga una serie de mensajes de texto cortos. 
# Pasa la lista a una función llamada show_messages(), que imprime cada mensaje de texto.

lista_de_compra = []
producto_comprado = []

lista_de_compra.append('disco duro')
lista_de_compra.append('teclado')
lista_de_compra.append('raton')
lista_de_compra.append('monitor')
lista_de_compra.append('tarjeta grafica')
lista_de_compra.append('placa madre')
lista_de_compra.append('fuente de poder')

while lista_de_compra:
    compra_del_momento = lista_de_compra.pop()
    print(f"Comprando: {compra_del_momento}")
    producto_comprado.append(compra_del_momento)

print("\n\t---Lista de compras---")
for item in producto_comprado:
    print(f"\t   - {item}")






    #8-10. Sending Messages:

#Comience con una copia de su programa del Ejercicio 8-9. 
# Escriba una función llamada enviar mensajes () que imprima cada mensaje de texto y mueva cada mensaje a una
#  nueva lista llamada mensajes enviados a medida que se imprime. 
# Después de llamar a la función, imprima ambas listas para asegurarse de que los mensajes se movieron correctamente.

        ###creo es lo mismo  que hice arriba###
lista_de_compra = []
producto_comprado = []

lista_de_compra.append('disco duro')
lista_de_compra.append('teclado')
lista_de_compra.append('raton')
lista_de_compra.append('monitor')
lista_de_compra.append('tarjeta grafica')
lista_de_compra.append('placa madre')
lista_de_compra.append('fuente de poder')

def mensaje():
    while lista_de_compra:
        compra_del_momento = lista_de_compra.pop()
        print(f"Comprando: {compra_del_momento}")
        producto_comprado.append(compra_del_momento)

    print("\n\t---Lista de compras---")
    for item in producto_comprado:
        print(f"\t   - {item}")

mensaje()







    #8-11. Archived Messages:

#Comience con su trabajo del Ejercicio 8-10. Llame a la función enviar mensajes() con una copia de la lista de mensajes. 
# Después de llamar a la función, imprima ambas listas para mostrar que la lista original ha conservado sus mensajes.

def mensaje(lista_de_compra, producto_comprado):
    while lista_de_compra:
        compra_del_momento = lista_de_compra.pop()
        print(f"Comprando: {compra_del_momento}")
        producto_comprado.append(compra_del_momento)

def lista_comprado():
    print("\n\t---Lista de compras---")
    for item in producto_comprado:
        print(f"\t   - {item}")
    print("\n\t---Lista de compra original---")
    for item in lista_de_compra:
        print(f"\t   - {item}")



lista_de_compra = []
producto_comprado = []

lista_de_compra.append('disco duro')
lista_de_compra.append('teclado')
lista_de_compra.append('raton')
lista_de_compra.append('monitor')
lista_de_compra.append('tarjeta grafica')
lista_de_compra.append('placa madre')
lista_de_compra.append('fuente de poder')



mensaje(lista_de_compra[:], producto_comprado)       #    ⬅⬅⬅⬅⬅⬅⬅⬅ aqui lo que hace que funcione, el [:] crea una copia de el original.
lista_comprado()










    #8-12.  Sandwiches:

#Escribe una función que acepte una lista de artículos que una persona quiere en un sándwich. 
# La función debe tener un parámetro que recopile tantos elementos como proporcione la llamada a la función, 
# y debe imprimir un resumen del sándwich que se está ordenando. 
# Llame a la función tres veces, usando un número diferente de argumentos cada vez.
def preparar_sandwiches(*ingredientes):
    """
    regresaremos los ingredientes al usuario
    """
    print(ingredientes)

preparar_sandwiches('jamon', 'queso', 'pan', 'jitomate',  'mayonesa')

  #----------------------------------------------------------------------------------------------------------- 

def preparar_sandwiches(*ingredientes):
    """
    regresaremos los ingredientes al usuario
    """
    print("\nCreando un sandwich con los siguientes ingredientes")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")

preparar_sandwiches('jamon', 'queso', 'pan', 'jitomate',  'mayonesa')

   #----------------------------------------------------------------------------------------------------------- 

def preparar_sandwiches(tamaño, *ingredientes):
    """
    regresaremos los ingredientes al usuario
    """
    print(f"\nCreando un sandwich tamaño {tamaño} con los siguientes ingredientes")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")

preparar_sandwiches('grande', 'jamon', 'queso', 'pan', 'jitomate',  'mayonesa')




    #8-13.  User Profile:

#Comience con una copia de user profile.py de la página 149. 
# Cree un perfil de usted mismo llamando a build profile(), usando su nombre y apellido y otros tres pares clave-valor que lo describan.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics',
                             )
user_profile_1 = build_profile('Lidwin', 'Gasca',               #           ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅
                               locacion='Ejido las Golondrinas',#           ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅
                               campo='Aprendiz de instalacion de HVAC')#    ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅

print(user_profile_1)#          ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅
print(user_profile)



    #8-14.  Cars:

#Escriba una función que almacene información sobre un automóvil en un diccionario. 
# La función siempre debe recibir un fabricante y un nombre de modelo. 
# Entonces debería aceptar un número arbitrario de argumentos de palabras clave. 
# Llame a la función con la información requerida y otros dos pares de nombre y valor, como un color o una característica opcional. 
# Su función debería funcionar para una llamada como esta:
#
#           >>> car = make_car('subaru', 'outback', color='blue', tow_package=True)
#
#Imprima el diccionario que se devuelve para asegurarse de que toda la información se almacenó correctamente.

descripcion_de_autos = {}

def descripcion_coche(brand, modelo, **mas_info):
    """construyendo un diccionario que contiene los detalles de un coche."""
    import time  # Import time module
    mas_info['car brand'] = brand
    mas_info['modelo'] = modelo
    timestamp = time.time()  # Get the current timestamp in seconds    ⬅# Esto es un especie de ID, para que no haya caros repetidos, 
    key = (brand, modelo, timestamp)                                    # o mejor dicho para que no se sobre escriban.
    descripcion_de_autos[key] = mas_info
    return mas_info

car = descripcion_coche('subaru', 'outback', color='blue', tow_package=True)
car1 = descripcion_coche('honda', 'civic', color='white', tow_package=True)
car2 = descripcion_coche('yoyota', 'tacoma', color='sand', tow_package=True)
car3 = descripcion_coche('nissan', 'versa', color='gray', tow_package=True)
car4 = descripcion_coche('honda', 'accord', color='black', tow_package=True)

for clave, valor in descripcion_de_autos.items():  # Agregamos el metodo .items()
    print(f"\n{clave}\n - {valor}")