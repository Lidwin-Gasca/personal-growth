
#CHAPTER 6
            #🐍DICTIONARIES🐍

        #🦴A Simple Dictionary

                                #Considere un juego con extraterrestres que pueden tener diferentes colores y valores de puntos. 
                                # Este diccionario simple almacena información sobre un extraterrestre en particular:
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

        #📝Working with Dictionaries

                        #Un diccionario en Python es una colección de "key-value pair"/"pares clave-valor". 
                        # Cada clave está conectada a un valor, y puede usar una clave/llave para acceder al valor asociado con esa clave.
                        # El valor de una clave puede ser un número, una cadena, una lista o incluso otro diccionario. 
                        # De hecho, puede usar cualquier objeto que pueda crear en Python como un valor en un diccionario.

                        #En Python, un diccionario está entre llaves, {}, con una serie de pares 
                        # clave-valor dentro de las llaves, como se muestra en el ejemplo anterior:

alien_0 = {'color': 'green', 'points': 5}

                        #Un "par clave-valor" es un conjunto asociado entre sí. 
                        # Cuando proporciona una clave, Python devuelve el valor asociado con esa clave. 
                        # Cada clave está conectada a su valor por dos puntos (:), y los pares clave-valor individuales están separados por comas. 
                        # Puede almacenar tantos pares clave-valor como desee en un diccionario.

#El diccionario más simple tiene exactamente un par clave-valor, 
# como se muestra en esta versión modificada del diccionario alien_0:
alien_0 = {'color': 'green'}
#Este diccionario almacena una pieza de información sobre alien_0, a saber, el color del alienígena. 
# La cadena 'color' es una clave en este diccionario, y su valor asociado es 'verde'.


        #`1-Accessing Value In A Dictionary

#Para obtener el valor asociado con una clave, ingrese el nombre del diccionario 
# y luego coloque la clave dentro de un conjunto de corchetes, como se muestra aquí:
alien_0 = {'color' : 'green'}
print(alien_0['color'])
#Esto devuelve el valor asociado con la clave 'color' del diccionario alien_0:  GREEN/verde

#Puede tener un número ilimitado de pares clave-valor en un diccionario.
#Por ejemplo, aquí está el diccionario alien_0 original con dos pares clave-valor:
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
 #Si ejecuta este código cada vez que se derriba a un alienígena, se recuperará el valor en puntos del alienígena.



        #`2- Adding new key-value Pairs / par clave valor.

#Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. 
# For example, to add a new key-value pair, you would give the name of the dictionary followed by the new 
# key in square brackets along with the new value.

#Let's add two new pieces of information to the alien a dictionary: the alien's x- and y-coordinates, 
# which will help us display the alien in a particular position on the screen. 
# Let's place the alien on the left edge of the screen, 25 pixels down from the top. 
# Because screen coordinates usually start at the upper-left corner of the screen, we'll place the alien 
# on the left edge of the screen by setting the x-coordinate to 0 and 25 pixels from the top by setting 
# its y-coordinate to positive 25, as shown here:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#The final version of the dictionary contains four key-value pairs. 
# The original two specify color and point value, and two more specify the alien position.

#NOTE
#As of Python 3.7, dictionaries retain the order in which they were defined. 
# When you print a dictionary or loop through its elements, you will see the elements in the order in which they were added to the dictionary.




        #`3- Starting with an Empty Dictionary

#It's sometimes convenient, or even necessary, to start with an empty diction ary and then add each new item to it. 
# To start filling an empty dictionary define a dictionary with an empty set of braces and then add each key-value pair on its own line. 
# For example, here's how to build the alien a dictionary using this approach:
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
#Typically, you'll use empty dictionaries when storing user-supplied data in a dictionary or when you write code 
# that generates a large number of key-value pairs automatically.




        #`4- Modifying Values in a Dictionary

#To modify a value in a dictionary, give the name of the dictionary with the key in square brackets 
# and then the new value you want associated with that key. 
# For example, consider an alien that changes from green to yellow as a game progresses:
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
#We first define a dictionary for alien_o that contains only the alien's color; 
# then we change the value associated with the key 'color' to 'yellow'. 
# The output shows that the alien has indeed changed from green to yellow:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right.
    #Determine how far  to move the alien based on its current speed.
if alien_0['speed'] == 'slow':                                      #At 0, an if-elif-else chain determines how far the alien should move to the 
    x_increment = 1                                               #right and assigns this value to the variable x_increment. If the alien's 
elif alien_0['speed'] == 'medium':                               #speed is 'slow', it moves one unit to the right; if the speed is 'medium', 
    x_increment = 2                                             #it moves two units to the right; and if it's 'fast', it moves three units 
else:                                                          #to the right. Once the increment has been calculated, it's added to the 
    #this must be fast alien.                                 #value of x_position at @, and the result is stored in the dictionary's x_position.                          
    x_increment = 3                                                     
#the new posittion is the old position plus the increment.          
alien_0['x_position'] = alien_0['x_position'] + x_increment         
                                    
print(f"New position: {alien_0['x_position']}")                         
#We start by defining an alien with an initial x position and y position, and a speed of 'medium'. 
# We've omitted the color and point values ​​for the sake of simplicity, but this example would work 
# the same way if you included those key-value pairs as well. 
# We also print the original value of x_position to see how far the alien moves to the right.

#This technique is pretty cool: by changing one value in the alien's dic- tionary, you can change the overall behavior of the alien. 
# For example, to turn this medium-speed alien into a fast alien, you would add the line:
alien_0['speed'] = 'fast'
#El bloque if-elif-else asignaría un valor mayor a x_increment la próxima vez que se ejecute el código.




        #`5- Removing key-value pairs

#Cuando ya no necesite una parte de la información almacenada en un diccionario, 
# puede usar la declaración delta para eliminar por completo un par clave-valor. 
# Todo lo que necesita es el nombre del diccionario y la clave que desea eliminar.

#Por ejemplo, eliminemos los puntos clave del diccionario alien o junto con su valor:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)




        #`6- A Dictionary of similar Objects

#The previous example involved storing different kinds of information about one object, an alien in a game. 
# You can also use a dictionary to store one kind of information about many objects. For example, say you want 
# to poll a number of people and ask them what their favorite programming language is. A dictionary is useful 
# for storing the results of a simple poll, like this:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
#Como puede ver, hemos dividido un diccionario más grande en varias líneas. 
# Cada clave es el nombre de una persona que respondió a la encuesta y cada valor es su elección de idioma. 
# Cuando sepa que necesitará más de una línea para definir un diccionario, presione ENTER después de la llave de apertura. 
# Luego, sangra la línea siguiente un nivel (cuatro espacios) y escribe el primer par clave-valor, seguido de una coma. 
# A partir de este punto, cuando presione ENTER, su editor de texto debería sangrar automáticamente 
# todos los pares clave-valor subsiguientes para que coincidan con el primer par clave-valor.

#Una vez que haya terminado de definir el diccionario, agregue una llave de cierre en una nueva línea después del último par 
# clave-valor y sangre un nivel para que se alinee con las claves del diccionario. También es una buena práctica incluir una 
# coma después del último par clave-valor, de modo que esté listo para agregar un nuevo par clave-valor en la siguiente línea.
#NOTE
#La mayoría de los editores tienen alguna funcionalidad que le ayuda a formatear listas extendidas y diccionarios de manera 
# similar a este ejemplo. También hay disponibles otras formas aceptables de formatear diccionarios largos, por lo que es 
# posible que vea un formato ligeramente diferente en su editor o en otras fuentes.

#To use this dictionary, given the name of a took the poll, you can easily look up their favorite language:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
#Puede usar esta misma sintaxis con cualquier individuo representado en el diccionario.





        #`7- Using get() to acces Values

#El uso de claves entre paréntesis cuadrados para recuperar el valor que le interesa de un diccionario puede causar un problema potencial: 
# si la clave que solicita no existe, obtendrá un error.

#Veamos qué sucede cuando pides el valor en puntos de un extraterrestre que no tiene establecido un valor en puntos:
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])    #esto resulta en un rastreo, mostrando un keyError. NOTE: para solucionar esto usa el metodo get()

#Aprenderá más sobre cómo manejar errores como este en género en el Capítulo 10. 
# Para los diccionarios, específicamente, puede usar el método get() para establecer 
# un valor predeterminado que se devolverá si la clave solicitada no existe.

#El método get() requiere una clave como primer argumento. 
# Como segundo argumento opcional, puede pasar el valor que se devolverá si la clave no existe:
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No points value assigned.')
print (point_value)

#Si omite el segundo argumento en la llamada a get() y la clave no existe, Python devolverá el valor Ninguno. 
# El valor especial Ninguno significa que "no existe ningún valor". 
# Esto no es un error: es un valor especial destinado a indicar la ausencia de un valor. Verá más usos para Ninguno en el Capítulo 8.





    # 📝LOOPING THROUGH A DICTIONARY
                                        #Un solo diccionario de Python puede contener solo unos pocos pares clave-valor o millones de pares. 
                                        # Debido a que un diccionario puede contener grandes cantidades de datos, Python le permite recorrer 
                                        # un diccionario. Los diccionarios se pueden utilizar para almacenar información de diversas formas; 
                                        # por lo tanto, existen varias formas diferentes de recorrerlos. Puede recorrer todos los pares 
                                        # clave-valor de un diccionario, sus claves o sus valores.

        #`1- Looping throug all Key-Values pairs

#Antes de explorar los diferentes enfoques de los bucles, consideremos un nuevo
# diccionario diseñado para almacenar información sobre un usuario en un sitio web. 

# El siguiente diccionario almacenaría el nombre de usuario, el nombre y el apellido de una persona:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
 }
#Puede acceder a cualquier pieza de información sobre el usuario 0 en función de lo que ya ha aprendido en este capítulo. Pero, ¿y si 
# quisiera ver todo lo almacenado en el diccionario de este usuario? Para hacerlo, puede recorrer el diccionario usando un bucle for:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
 }
 
for clave, valor in user_0.items():
    print(f"\nKey: {clave}")
    print(f"Value: {valor}")

#Recorrer todos los pares clave-valor funciona particularmente bien para diccionarios como el ejemplo de 
# favourite_languages.py en la página 97, que almacena el mismo tipo de información para muchas claves diferentes. 
# Si recorre el diccionario de idiomas_favoritos, obtiene el nombre de cada persona en el diccionario y su 
# lenguaje de programación favorito. Debido a que las claves siempre se refieren al nombre de una persona y 
# el valor siempre es un idioma, usaremos las variables nombre e idioma en el bucle en lugar de clave y valor. 
# Esto hará que sea más fácil seguir lo que sucede dentro del ciclo:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for nombre , lenguaje, in favorite_languages.items():                     #Este tipo de ciclos/looping funcionaria incluso con miles
    print(f"{nombre.title()}'s favorite language is {lenguaje.title()}.")       # y millones de item/elementos (parejas clave-valor)



        

        #`- Looping through all the keys in a Dictionary

#El método keys() es útil cuando no necesita trabajar con todos los valores en un diccionario. 
# Recorramos el diccionario de idiomas_favoritos e imprimamos los nombres de todos los que respondieron la encuesta:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for nombre in favorite_languages.keys():
    print(nombre.title())
#Recorrer las teclas es en realidad el comportamiento predeterminado cuando se recorre un diccionario, 
# por lo que este código tendría exactamente el mismo resultado si escribiera...
for nombre in favorite_languages:
    print(nombre)
    #en vez de
for nombre in favorite_languages.keys():
    print(nombre)
    #Puede optar por usar el método keys() explícitamente si hace que su código sea más fácil de leer, o puede omitirlo si lo desea.
#Puede acceder al valor asociado con cualquier clave que le interese dentro del bucle utilizando la clave actual. 
# Imprimamos un mensaje para un par de amigos sobre los idiomas que eligieron. 
# Recorreremos los nombres en el diccionario como lo hicimos anteriormente, 
# pero cuando el nombre coincida con uno de nuestros amigos, mostraremos un mensaje sobre su idioma favorito:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for nombre in favorite_languages.keys():
    print(f"Hi {nombre.title()}.")

    if nombre in friends:
        language = favorite_languages[nombre].title()
        print(f"\t{nombre.title()}, I see you love {language}!")
        #todos los nombres de favorite_language son mecionados, pero los de la lista friends reciben un mensaje especial.

#Tambien podemos usar el metodo keys() para encontrar si alguien en particular no esta en el diccionario, de la siguiente manera:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

if 'erin' not in favorite_languages.keys():
    print(f"Erin, porfavor toma tu voto de leguaje de programacion preferido")





    #Looping Through a Dictionary's Keys in a Particular Oder

#A partir de Python 3.7, recorrer un diccionario devuelve los elementos en el mismo orden en que se insertaron. 
# A veces, sin embargo, querrá recorrer un diccionario en un orden diferente.

#Una forma de hacer esto es ordenar las claves a medida que se devuelven en el bucle for. 
# Puede usar la función sorted() para obtener una copia de las claves en orden:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")




    # Looping Through All Values in a Dictionary

#Si está interesado principalmente en los valores que contiene un diccionario, puede usar el método de valores() 
# para devolver una lista de valores sin ninguna clave. Por ejemplo, digamos que simplemente queremos una lista 
# de todos los idiomas elegidos en nuestra encuesta de lenguajes de programación sin el nombre de la persona que eligió cada idioma:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())         #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅-
    #La declaración for aquí extrae cada valor del diccionario y lo asigna a la variable idioma.     ⬆
    # Cuando se imprimen estos valores, obtenemos una lista de todos los idiomas elegidos:  ➡➡➡➡➡-


#Este enfoque extrae todos los valores del diccionario sin verificar si hay repeticiones. 
# Eso podría funcionar bien con una pequeña cantidad de valores, pero en una encuesta con 
# una gran cantidad de encuestados, esto daría como resultado una lista muy repetitiva. 
# Para ver cada idioma elegido sin repetición, podemos usar un conjunto Un conjunto es una colección en la que cada elemento debe ser único:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#A medida que continúe aprendiendo sobre Python, a menudo encontrará una característica 
# integrada del lenguaje que lo ayuda a hacer exactamente lo que quiere con sus datos.

#Puedes construir un conjunto directamente usando llaves y separando los elementos con comas:
    languages = {'python', 'ruby', 'python', 'c'}
    languages
{'ruby', 'python', 'c'}
#NOTE
#It's easy to mistake sets for dictionaries because they're both wrapped in braces. 
# When you see braces but no key-value pairs, you're probably looking at a set. 
# Unlike Ests and dictionaries, sets do not retain items in any specific order






#NESTING

                    #A veces querrá almacenar varios diccionarios en una lista, o una lista de elementos como un valor dentro 
                    # de un diccionario, o incluso un diccionario dentro de otro diccionario. El anidamiento es una característica 
                    # poderosa, como lo demostrarán los siguientes ejemplos.

 



    # A Listf Of Dictionaries

#El diccionario alien_0 contiene una variedad de información sobre un extraterrestre, pero no tiene espacio para almacenar 
# información sobre un segundo extraterrestre, y mucho menos una pantalla llena de extraterrestres. ¿Cómo puedes manejar una 
# flota de extraterrestres? Una forma es hacer una lista de extraterrestres en la que cada extraterrestre sea un diccionario 
# de información sobre ese extraterrestre. Por ejemplo, la siguiente lista de compilación de código de tres alienígenas:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = {'color': 'red', 'points': 15}

for alien in aliens:
    print(alien)

#Un ejemplo más realista involucraría a más de tres alienígenas con un código que genera automáticamente cada alienígena. 
# En el siguiente ejemplo, usamos range() para crear una flota de 30 alienígenas:

#Make an empty list for storing aliens.
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

#Todos estos alienígenas tienen las mismas características, pero Python considera a cada uno un objeto separado, lo que nos permite 
# modificar cada alienígena individualmente.


#¿Cómo podrías trabajar con un grupo de extraterrestres como este? Imagina que un aspecto de un juego tiene algo para cambiar los 
# colores, podemos usar un bucle for y una declaración if para cambiar el color de los alienígenas. Por ejemplo, para cambiar los 
# primeros tres extraterrestres a extraterrestres amarillos de velocidad media que valen 10 puntos cada uno, podríamos hacer esto:
aliens = []
#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:                #Porque queremos modificar los primeros tres alienígenas. 
    if alien['color'] == 'green':       #Todos los alienígenas son verdes ahora, pero ese no siempre será el caso, 
        alien['color'] == 'yellow'      # por lo que escribimos una declaración if para asegurarnos de que solo estamos modificando 
        alien['speed'] == 'medium'      # alienígenas verdes. Si el alienígena es verde, cambiamos el color a 'amarillo', la 
        alien['points'] == 10           # velocidad a 'media' y el valor de puntos a 10, como se muestra en el siguiente resultado:
#Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#Puede expandir este ciclo agregando un bloque "elif" que convierte a los alienígenas amarillos en rojos, que se 
# mueven rápidamente, con un valor de 15 puntos cada uno. Sin volver a mostrar todo el programa, ese bucle se vería así:
for alien in aliens[:3]:                
    if alien['color'] == 'green':       
        alien['color'] == 'yellow'      
        alien['speed'] == 'medium'      
        alien['points'] == 10           
    elif alien['color'] == 'yellow':
        alien['color'] == 'red'
        alien['speed'] == 'fast'
        alien['points'] == 15






# A List In A Dictionary

                #En lugar de poner el diccionario dentro de una lista, a veces es útil poner una lista dentro del diccionario. 
                # Por ejemplo, considere cómo podría describir una pizza que alguien está ordenando. Si tuviera que usar solo una 
                # lista, todo lo que realmente podría almacenar es una lista de los ingredientes de la pizza. con un diccionario, 
                # una lista de ingredientes puede ser solo un aspecto de la pizza que estás describiendo.

#En el siguiente ejemplo, se almacenan dos tipos de información para cada pizza: un tipo de corteza y una lista 
# de ingredientes. La lista de toppings es un valor asociado a la clave 'toppings'. Para utilizar los elementos 
# de la lista, le damos el nombre del diccionario y la tecla 'toppings', como haríamos con cualquier valor del 
# diccionario. En lugar de devolver un solo valor, obtenemos una lista de ingredientes:
pizza = {#Store information about a pizza being ordered.
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza"
    "with the following topping:")

for topping in pizza['toppings']:
    print(f"\t{topping}")




#Puede anidar una lista dentro de un diccionario cada vez que desee asociar más de un valor con una sola clave en un diccionario. 
# En el ejemplo anterior de los lenguajes de programación favoritos, si tuviéramos que almacenar las respuestas de cada persona 
# en una lista, las personas podrían elegir más de un lenguaje favorito. Cuando recorremos el diccionario, el valor asociado con 
# cada persona sería una lista de idiomas en lugar de un solo idioma. Dentro del bucle for del diccionario, usamos otro bucle for 
# para recorrer la lista de idiomas asociados con cada persona:
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
#Para refinar aún más este programa, puede incluir una instrucción if al principio del bucle for del diccionario para ver 
# si cada persona tiene más de un idioma favorito examinando el valor de len (idiomas). Si una persona tiene más de un favorito, 
# el resultado sería el mismo. Si la persona solo tiene un idioma favorito, puede cambiar la redacción para reflejar eso. 
# Por ejemplo, podría decir que el idioma favorito de Sarah es C.

#NOTE
#No debe anidar listas y diccionarios demasiado profundamente. 
# Si está anidando elementos mucho más profundamente que lo que 
# ve en los ejemplos anteriores o está trabajando con el código 
# de otra persona con niveles significativos de anidamiento, lo 
# más probable es que exista una forma más sencilla de resolver 
# el problema.






    #A Dictionary In A Dictionary

#Puede anidar un diccionario dentro de otro diccionario, pero su código puede complicarse rápidamente cuando lo hace. 
# Por ejemplo, si tiene varios usuarios para un sitio web, cada uno con un nombre de usuario único, puede usar los nombres 
# de usuario como claves en un diccionario. A continuación, puede almacenar información sobre cada usuario mediante el 
# uso de un diccionario como el valor asociado con su nombre de usuario. En la siguiente lista, almacenamos tres 
# datos sobre cada usuario: su nombre, apellido y ubicación. Accederemos a esta información recorriendo los nombres 
# de usuario y el diccionario de información asociado con cada nombre de usuario:
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    #Observe que la estructura del diccionario de cada usuario es idéntica. 
    # Aunque Python no lo requiere, esta estructura facilita el trabajo con los diccionarios anidados. 
    # Si el diccionario de cada usuario tuviera claves diferentes, el código dentro del ciclo for sería más complicado.

#Sumario:
        #En este ⬆ capítulo aprendió cómo definir un diccionario y cómo trabajar con la información almacenada en un diccionario. 
        # Aprendió cómo acceder y modificar elementos individuales en un diccionario y cómo recorrer toda la información en un diccionario. 
        # Aprendió a recorrer los pares clave-valor de un diccionario, sus claves y sus valores. 
        # También aprendió cómo anidar varios diccionarios en una lista, anidar listas en un 
        # diccionario y anidar un diccionario dentro de un diccionario.

#En el próximo capítulo ⬇ aprenderás sobre los bucles while y cómo aceptar entradas de personas que están usando sus programas. 
# Este será un capítulo emocionante, porque aprenderá a hacer que todos sus programas sean interactivos: 
# podrán responder a las entradas del usuario.
