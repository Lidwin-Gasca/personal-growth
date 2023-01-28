#CHAPTER 2
    #🐍Changing Case In String In Methods#

name = "tu mamaTambien"
print (name.title())  #al poner el .title hace que la primera letra de cada palabra sea mayuscula, 
#si hay una mayuscala en medio de la misma palabra, ésta se vuelve minúscula. 
print (name.upper())    #al poner .upper convierte todas las letras en mayusculas.
print (name.lower())    #al poner .lower convierte toda letra de las palabras en minusculas.

    #🦴Using Variables in Strings#

first_name = "Lidwin" #delaramos los valores de esta manera, poniendo simplemente el nombre de la variable 
#y su valor. En esto caso, un valor en formato "String"
last_name = "Gasca"
full_name = f"{first_name} {last_name}" #esta variable tiene como valor un string compuesto por por dos 
#variables que su vez tambien serán string, Ojo que por ello mismo este no es un simple string que contiene dos 
# variables dentro, se llama f-string y se usa para insertarle variables en su interior, sin importar si estas 
# mismas son de formato string o numero.
print(full_name)
print(f"Hola mundo soy {first_name} estoy aprendiendo Python, mi apellido es {last_name}. Acompañame en mi aventura")
print(f"Hello, {full_name.title()}!")
messege = f"Hello, {full_name.title()}!" #tambien pudo ser al estilo viejito full_name = "{}{}".format(first_name, last_name)
print(messege)

    #🦴Adding Whitespace To Strings with Tabs or Newlines

print("Python") #para agregar un tabulador a tu texto, usa una combinacion de caracteres como el mostrado 
#abajo de esta linea \t .
print("\tPython")   
#para agregar una nueva linea en un string, usa la combinacion de caracteres \n .
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript") #  tambien se pueden combinar ambas combinaciones.


    #🦴Stripping Whitespace

favorite_language = ' python '
print(favorite_language)    #imprimimos el valor tal cual sin alterar.

fav_right_lang = favorite_language.rstrip() #usamos el metodo .rstrip() para quitar el espacio a la derecha 
print(fav_right_lang)                       #de la palabra de dicho valor, y lo imprimimos.

fav_left_lang = favorite_language.lstrip()  #con el metodo .lstrip() quitamos espacio en blaco que se encuentren
print(fav_left_lang)                        #a la izquierda de el valor de nuestra variable (solo si el valor es
                                            #de formato string claro).


    #🦴 Avoiding Syntax Errors With Strings
#here's how to use a single and double quotes correctly. apostrophe
messege_1 = "One of Python's strengths is its diverse community."
print(messege_1)

    #🦴 Integers/Enteros
#you can add (+), subtract (-), multiply (*), snd divide (/) integers in Python.
#puedes sumar, restar, multiplicar y dividir enteros en Python.
print(f"(2 + 3) es igual a:\n {2 + 3}")
print(3-2)
print(2*3)
print(3/2)
#Python usa dos simbolos de multiplicacion para representar exponentes.
print(f"(3 ** 2) es igual a:\n {3 ** 2}")
print(3**3)
print(10**6)
#Python respeta el orden de operaciones, incluso resolvera las operaciones dentro de un parentesis primero,
#tal como la matematica real.
print(2 + 3 * 4)
print((2+3)* 4)

    #🦴Floats
#python llama a cualquier numero que contenga un decimal, Float. En su mayor parte, puedes escribir decimales 
#sin preocuparte de su comportamiento, simplemente ingresa los numeros que desees, y python se encargara de 
#de hacer lo que esperas que haga (a veces no lo hará, mas informacion adelante).
#Ejemplo de Float:
0.1 + 0.1 ##0.2
0.2 + 0.2 ##0.4
2 * 0.1 ##0.2
2 * 0.2 ##0.4
#Pero aveces te pude arrojar un numero decimal arbitrario en tu respuesta, por ejemplo:
0.2 + 0.1 ##0.30000000000000004
print(f"(3 * 0.1) es igual a:\n {3 * 0.1}") ##0.30000000000000004

    #🦴Integers and Floats
#cuando divides dos numeros, incluso si son numeros enteros, y que reultado tambien da numero entero, sin 
#imprtar ello, el resultado arrojado por Python sera en formato Float, es decir decimal.Ejemplo:
4/2 ##2.0
print(f"Cuatro entre dos da como resultado:\n {4/2}") ##2.0
#si revuelves enteros (integer) con decimales (float) en cualquier operacion, aun asi recibiras tu resultado
#arrojado en formato Float (decimal).

    #🦴Underscores In Numbers
universe_age = 14_000_000_000
#pudes usar guiones bajos en los numeros largos o incluso cortos, siempre y cuando no terminen en los extremos, 
#ya sea izquierda o derecha.
print(14_000_000_000) ##14000000000

    #🦴Multiple Assignment
x, y, z = 0, 0, 0  #puedes inicializar varias variables en la misma linea, en decir crear variables y darle valor
#debes separar las variables con comas, al inicializar el valor seguir el orden de las variables al dar el valor

    # 🦴Constants/constantes
#una contante es aquella variable cuyo valor jamás cambiara durante la vida del programa, como buena practica 
#los programadores usan todas la letras en el nombre de cuya variable en mayusculas. De esta manera quien lo lea
#en un futuro sabra que es una constante. Un ejemplo seria el siguiente:
MAX_CONNECTIONS = 5000

    #The Zen of Python
import this #corre esta linea de codigo en tu consola.


#CHAPTER 3                                                                      3️⃣

    #🐍What Is A List ?

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #this is a list
print(bicycles)

    #🦴 Accessing Elements In A List

print(bicycles[0]) #los elementos de una lista tienen un  numerado de lista, un indice, no im porta el valor de el 
#elementro de una lista, el primer elemento en ella tendra el indice "0", el sgundo el indice "1" el tercero el 
# indice "2" y asi sucesivamente, por ejmplo el elemento de la lista en el lugar octavo, tendria un indice de "7"
#otgro ejemplo: un elemento en el lugar 32 de la lista tendra un indice "31".
#al escribir el nombre de la variable que tiene una lista como su valor, si escribes el caracter de las casillas 
# #"[]" con un numero adentro, ese numero representara el indice del elemento que deseas visualizar o seleccionar
print(bicycles[0].title()) #tambien puedes alterar los valores/elementos de una lista.

    #🦴 Modifying Elements In A List
    
#por ejemplo tenemos una lista de motocicletas, el primer item de la lista en 'honda', Como cambiarias el valor de 
# el primer item?
motorcycles = ['honda', 'yamacha', 'suzuki']
print(motorcycles)
#en la linea debajo esta cambiaremos el valor de el primer item de la lista.
motorcycles[0] = 'ducati'
print(motorcycles)

    #🦴 Adding Elements To The List
    
    #`1- Appending Elements To The End Of A List
motorcycles.append('subaru')
print(motorcycles)  #el metodo append.() agrega un nuevo valor al final de la lista sin afectar ningun elemento en la lista.
    
    #`2- Inserting Elements Into A List
motorcycles.insert(0, 'kia')    #para usar el metodo insert.() en necesario especificar los parametros del mismo, este 
#metodo tiene dos parametros los cuales se respetan su orden y significado, el primer parametro es para tu como usuario 
#escogas la posicion de el nuevo elemento que estas insertando, vas a declar en que indice deseas posicionar tu nuevo 
#valor. El segundo parametro es para definir el valor que esta siendo insertado/agregado.
print(motorcycles)

    #🦴 Removing Elements From A List
    
        #`1- Removing An Item Using The 'del' Statement
del motorcycles[0] #con el statement/declaracion 'del' puedes eliminar el elemento de alguna posicion de la lista, 
print(motorcycles)  #siempre y cuando estas conciente de que conoces el indice del elemento que deseas eliminar.

        #`2- Removing An Item Using the 'pop()' Method
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)    #el metodo .pop() elimina el ultimo elemento de una lista. Y a su vez lo toma y guarda en 
print(motorcycles)          #otro lugar si asi lo deseas.

        #`3- Popping Items From Any Position In A List
position_popped_motorcycle = motorcycles.pop(0)
print(position_popped_motorcycle)   #Introduciendo un numero/parametro (el cual representa un indice) indicamos a que elemento 
#se eliminará, mediante su posicion de indice, en el caso preparado se aplico el metodo .pop() al indice 0  ".pop(0)"

        #`4- Removing An Item By Value
motorcycles = ['honda', 'yamacha', 'suzuki', 'ducati', 'kia', 'subaru']
motorcycles.remove('ducati')# el metodo .remove() remueve el elemento que tenga como valor el mismo valor indicado en el 
print(motorcycles)          # parametro del metodo mencionado, en este caso 'ducati'
#otra manera de hacerlo es con una variable que tenga el valor/elemento que se quiere eliminar de la lista:
una_buena_moto = 'honda'
motorcycles.remove(una_buena_moto)
print(motorcycles)
print(f"\nLa moto {una_buena_moto.title()} es muy caro para mi presupuesto.")


    #🦴 Organizing A List

        #`1-Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #el metodo .sort() ordena de manera alfabetica los elementos de la lista en el orden del alfabeto (A-Z). [valga la redundancia].
print(cars)
#otra manera de hacer es en el orden contrario de el alfabeto:
cars.sort(reverse=True)
print(cars) #es muy util estos datos.

        #`2-Soting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")     #esto crea una array completamente nuevo y momentaneo si es que no lo guardas como variable.
print(sorted(cars))

print("\nHere is the original liest again:")
print(cars)

        #`4- Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()#a la variable cars se le voltea por completo la lista, haciendo los ultimos elementos en los primeros en los primeros en ultimos.
print(cars)

        #`5- Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))    # len(car) te da el largo de la lista, cuantos elementos de largo está. len proviene de a palabra en ingles length

# Dato curioso, si como indice pornes numeros en negativos te mostrara en orden reverrso los elementos de la lista, por ejemplo:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars[-1]) #saldra el ultimo elemento, 'subaru'.


    # CHAPTER 4:                                                        4️⃣ 
    
    #🦴 Working with List

        #`1- Looping Through An Entire List
magicians = ['alice', 'david', 'carolina']  #definimos la lista.
for magician in magicians:                  #definimos el Loop.  Por cada magician/elemento dentro de la lista "magicians"
    print(magician)                         #imprimimos

        #`2- Doing more work within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that eas a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

        #`3- Doing somthing after a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that eas a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")  #como habras notado hay una identacion de espacio en los 
#"print()" anteriores, en las lineas de codigo numero 228 y 229, arriba es esta linea. esta identacion de espacio es un
#tabulador de distancia (por asi decirlo) todo codigo con esa identacion sera parte de el bloque de codigo de la linea
#de codigo que termina con dos puntos ":". Todo lo que este con esa identacion, ser repetira en el Loop.


    #🦴 Making Numerical List

        #`1- Using the range() Function
for value in range(1,5):
    print(value)        #esto hace que se genere el valor numerico en orden acendente deltro de la lista nombrada 'value'
#ojo que los numeros solo llegaron hasta el numero cuatro, y no hasta el cinco.

        #`2- Using range() to make a List of Numbers
numbers = list(range(1, 6)) 
print(numbers)#Aqui hemos usado un nuevo metodo, el de list() que lo que hace es enlistar, en este caso enlista lo que hay en el metodo range()

#incluso pordemos añadir un tercer parametro a el metodo range(), y lo que este hace es definir de cuanto en cuanto avanzaran los numeros, por ejemplo:
even_numbers = list(range(2, 11, 2)) 
print(even_numbers)  #avanzo del "2" al numero "10" por que se detiene al tocar "11" (tienes que ejecutarlo en consola para entender).

#Puede crear casi cualquier conjunto de números que desee utilizando la función range(). Por ejemplo, considere cómo podría 
# hacer una lista de los primeros 10 números cuadrados (es decir, el cuadrado de cada número entero del 1 al 10). En los 
# primeros 10 números cuadrados en una lista:
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#para escribir el codigo anterior de manera mas sutil hacerlo asi:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

        #`3- Simple statistics with a List of Numbers
digits = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 0]
print(min(digits))      #   min() -----> muestra el numero mas chico en la lista
print(max(digits))      #   max() -----> muestra el numero mas grande de la lista
print(sum(digits))      #   sum() -----> muestra la suma de todos los numeros/elementos dentro de la lista

        #`4- List Comprenhensions
players = ['charles', 'martina', 'micael', 'florence', 'eli']   #Una sintaxis similar funciona si desea un segmento que incluya el final de una lista. 
#Por ejemplo, si desea todos los elementos desde el tercer elemento hasta el último elemento. puede comenzar con el índice 2 y omitir el segundo índice:
print(players[2:])

#This syntax allows you to output all of the elements from any point in your list to the end regardless of the length of the list. 
# Recall that a negative index returns an element a certain distance from the end of a list, therefore, you can output any slice 
# from the end of a list. For example, if we want to output the last three players on the roster, we can use the slice players[-3]
players = ['charles', 'martina', 'micael', 'florence', 'eli']
print(players[-3])
#Esto imprime los nombres de los últimos tres jugadores y continuaría funcionando a medida que la lista de jugadores cambia de tamaño.

#Puede incluir un tercer valor entre paréntesis que indique un sector/slice/corte. 
# Si se incluye un tercer valor, esto le dice a Python cuántos elementos omitir entre elementos en el rango especificado.

        #`5- Looping through a Slice
players = ['charles', 'martina', 'micael', 'florence', 'eli']
print("Here are the first three players on mly team:")
for player in players[:3]:
    print(player.title())

        #`6- Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

    #🦴 Tuples

        #`1- Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])        #Que es un Tuple?   Un tuple es una lista ineditable, no lo puedes modificar, la diferencia grafica es que la 
print(dimensions[1])        #lista de un Tuple en vez de llevar brakets/corchetes-cuadrados lleva parentesis. Otra forma de hacerlo para
                            #cuando solo en un elemento, y no nesesariamente una lista, es poner un coma "," , de esta manera estas avisando
dimensions[0] = 250         #que es inmodificable, que es un Tuple. #por ejemplo: dimensions = 200,


        #`2- Looping through all values in a Tuple
dimensions = (200, 50)
for dimension in dimensions:        #los tuple son manipulables como las listas convencionales, cuando de retornar valores de trata.
    print(dimension)

        #`3- Writing over a Tuple
dimensions = (200, 50)
print("Original dimension:")            #no puedes modificar un Tuple, mas sin embargo puedes reasignar el valor de la variable que solia ser un Tuple.
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimension:")
for dimension in dimensions:
    print(dimension)

    #CHAPTER 5                                                                          5️⃣

#🐍IF STATEMENTS

    #🦴 A Simple Example
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

    #🦴 Conditional Test
                    # En el corazón de cada declaración if hay una expresión que se puede evaluar como verdadera o falsa y se llama prueba condicional. 
                    # Python usa los valores True y False para decidir si se debe ejecutar el código en una declaración if. 
                    # Si una prueba condicional se evalúa como True, Python ejecuta el código que sigue a la instrucción if. 
                    # Si la prueba se evalúa como Falso, Python ignora el código que sigue a la instrucción if.
    
        #`1- Checking for equality
car = 'bmw'
car == 'bmw' #True
 
car = 'audi'
car == 'bmw' #False

        #`2- Ignoring case when cheking for equality
car = 'Audi'
car == 'audi' #False

car = 'Audi'
car.lower() == 'audi' #True

        #`3- Checking inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

        #`4- Numnerical comparisons

age = 18
age == 18 #True

answer = 17
if answer != 42:
    print("that is not the correct answer. Please try again!")

age = 19
age < 21 #True
age <= 21 #True
age > 21 #False
age >= 21 #False

    #🦴 Checking Multiple Conditions
                                                        #You may want to check multiple conditions at the same time. For example, sometimes 
                                                        # you might need two conditions to be True to take an action. Other times you might 
                                                        # be satisfied with just one condition being True. The keywords and and or can help 
                                                        # you in these situations.
        #`1- Using "and" to check multiple conditions.
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 #False

age_1 = 22
age_0 >= 21 and age_1 >= 21 #True

#para mejorar la lectura de el codico de multiple condicionales, ecribirlo asi: "(age_0 >= 21) and (age_1 >= 21)"

        #`2- Using "or" to check multiple conditions.
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21  #True

age_0 = 18
age_0 >= 21 or age_1 >=21   #False


    #🦴Checking Whether a Value Is "in" a List
                                                # Comprobar si un valor está en una lista, a veces es importante comprobar si una lista contiene 
                                                # un determinado valor antes de realizar una acción. Por ejemplo, es posible que desee verificar 
                                                # si ya existe un nuevo nombre de usuario en una lista de nombres de usuario actuales antes de 
                                                # completar el registro de alguien en un sitio web. En un proyecto de mapeo, es posible que desee 
                                                # verificar si una ubicación enviada ya existe en una lista de ubicaciones conocidas.

#Para averiguar si un valor en particular ya está en una lista, use la palabra clave in. Consideremos un código que podría escribir para una pizzería. 
# Haremos una lista de ingredientes que un cliente ha solicitado para una pizza y luego verificaremos si ciertos ingredientes están en la lista:
requested_topping = ['mushrooms', 'onieons', 'pineapple']
'mushrooms' in requested_topping    #True   ➡   print('mushrooms' in requested_topping)
'pepperoni' in requested_topping    #False  ➡   print('pepperoni' in requested_topping)



    #🦴 Checking Whether A Value Is Not "in" A List.

banned_users = ['andrew', 'carolina', 'david']
user = 'merie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


    #🦴 Boolean Expression
                        # A medida que aprenda más sobre programación, escuchará el término expresión booleana en algún momento. Una expresión 
                        # booleana es solo otro nombre para una prueba condicional. Un valor booleano es verdadero o falso, al igual que el valor
                        #  de una expresión condicional después de haberla evaluado.
                        #Los valores booleanos a menudo se usan para realizar un seguimiento de ciertas condiciones, como si un juego se está 
                        # ejecutando o si un usuario puede editar cierto contenido en un sitio web:
game_active = True
can_edit = False
#Los valores booleanos proporcionan una manera eficiente de rastrear el estado de un programa o una condición particular que es importante en su programa.








    #🦴 "if" Statements
                    # Cuando comprenda las pruebas condicionales, puede comenzar a escribir sentencias if. 
                    # Existen varios tipos diferentes de sentencias, y su elección de cuál usar depende de la cantidad de condiciones que necesita probar. 
                    # Viste varios ejemplos de declaraciones if en la discusión sobre pruebas condicionales, pero ahora profundicemos en el tema.

        #`1- Simple "if" statements
# El condicional de "if" mas sencillo es el de solo una accion:
#       --|if conditional_test:     |--
#       --|    hacer algo           |--

#Puede poner cualquier prueba condicional en la primera línea y casi cualquier acción en el bloque sangrado que sigue a la prueba. 
# Si la prueba condicional se evalúa como True, Python ejecuta el código que sigue a la instrucción if. Si la prueba se evalúa como Falso, 
# Python ignora el código que sigue a la instrucción if.

#Digamos que tenemos una variable que representa la edad de una persona y queremos saber si esa persona tiene la edad suficiente para votar. 
# El siguiente código prueba si la persona puede votar:
age = 19
if age >= 18:
    print("You are old enough to vote!")


        #`2- "if-else" statements
#A menudo, deseará realizar una acción cuando pase una prueba condicional y una acción diferente en todos los demás casos. 
# La sintaxis if-else de Python lo hace posible. Un bloque if-else es similar a una declaración if simple, pero la 
# declaración else le permite definir una acción o un conjunto de acciones que se ejecutan cuando falla la prueba condicional.

#Mostraremos el mismo mensaje que teníamos anteriormente si la persona tiene la edad suficiente para votar, pero esta vez 
# agregaremos un mensaje para cualquiera que no tenga la edad suficiente para votar:
age = 17
if age >= 18:
    print("You are odl enough to vot!")
    print("Have you registered to vote yet!")
else: 
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18")     #Este código funciona porque solo tiene dos situaciones posibles para evaluar: 
    # Una persona tiene la edad suficiente para votar o no tiene la edad suficiente para votar. 
    # La estructura if-else funciona bien en situaciones en las que desea que Python siempre ejecute una de dos acciones posibles. 
    # En una cadena if-else simple como esta, siempre se ejecutará una de las dos acciones.


        #`3- The "if-else-if" chain
                                    #A menudo, deberá probar más de dos situaciones posibles y, para evaluarlas, puede usar 
                                    # la sintaxis if-elif-else de Python. Python ejecuta solo un bloque en una cadena if-elif-else. 
                                    # Ejecuta cada prueba condicional en orden hasta que pasa una. Cuando pasa una prueba, 
                                    # se ejecuta el código que sigue a esa prueba y Python omite el resto de las pruebas.

# Muchas situaciones del mundo real involucran más de dos condiciones posibles. 
# Por ejemplo, considere un parque de diversiones que cobra diferentes tarifas para diferentes grupos de edad:

#   💨La entrada para cualquier persona menor de 4 años es gratuita.
#   💨La entrada para cualquier persona entre las edades de 4 y 18 años es de $25.
#   💨La entrada para cualquier persona mayor de 18 años es de $40.

#¿Cómo podemos usar una declaración if para determinar la tasa de admisión de una persona? 
# El siguiente código prueba el grupo de edad de una persona y luego imprime un mensaje de precio de admisión:

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# Cualquier edad mayor de 17 años haría que las dos primeras pruebas fallaran. 
# En estas situaciones, se ejecutaría el bloque else y el precio de admisión sería de $40.

#En lugar de imprimir el precio de la entrada dentro del bloque if-elif-else sería más 
# conciso establecer solo el precio dentro de la cadena if-elif-else y luego tener una 
# simple llamada print() que se ejecute después de que la cadena haya sido evaluado:

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")



        #`4- Using multiple "elif" blocks

#Puede usar tantos bloques elif en su código como desee. Por ejemplo, si el parque de diversiones 
# implementara un descuento para personas mayores, podría agregar una prueba condicional más al 
# código para determinar si alguien califica para el descuento para personas mayores. 
# Digamos que cualquier persona mayor de 65 años paga la mitad de la entrada regular, o $20:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}")



        #`5- Omitting the else block

#Python no requiere un bloque else al final de una cadena if-elif. A veces, un bloque else es útil; 
# a veces es más claro usar una declaración elif adicional que capte la condición específica de interés:
age = 12
if age < 4:              #--- El bloque else es una declaración general. ---#
    price = 0                                  
elif age < 18:           #Coincide con cualquier condición que no haya coincidido con una prueba if o elif específica,
    price = 25           # y que a veces puede incluir datos no válidos o incluso maliciosos.
elif age < 65:           # Si tiene una condición final específica que está probando, considere usar un bloque elif final y omita el bloque else.
    price = 40           # Como resultado, obtendrá una mayor confianza en que su código se ejecutará
elif age >= 65:          # solo en las condiciones correctas.
    price = 20



        #`6- Testing multiple conditions

#La cadena if-elif-else es poderosa, pero solo es apropiada para usar cuando solo necesita pasar una prueba. 
# Tan pronto como Python encuentra una prueba que pasa, salta el resto de las pruebas. 
# Este comportamiento es beneficioso porque es eficiente y le permite probar una condición específica.

#Sin embargo, a veces es importante verificar todas las condiciones de interés. 
# En este caso, debe usar una serie de declaraciones if simples sin bloques elif o else. 
# Esta técnica tiene sentido cuando más de una condición puede ser Verdadera y desea actuar en cada condición que sea Verdadera.

#   💨 Reconsideremos el ejemplo de la pizzería 🍕. 
# Si alguien solicita una pizza con dos ingredientes, deberá asegurarse de incluir ambos ingredientes en su pizza:

requested_topping = ['mushrooms', 'extra chesse']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")





    #🦴 Using "if" Statement With Lists
                                            #Puede hacer un trabajo interesante cuando combina listas y sentencias if. 
                                            # Puede buscar valores especiales que deben tratarse de manera diferente a otros valores en la lista. 
                                            # Puede administrar las condiciones cambiantes de manera eficiente, como la disponibilidad de ciertos 
                                            # artículos en un restaurante durante un turno. También puede comenzar a probar que su código funciona 
                                            # como espera en todas las situaciones posibles.

        #`1- Checking for special Items

#Este capítulo comenzó con un ejemplo simple que mostraba cómo manejar un valor especial como 'bmw', que necesitaba imprimirse en un formato 
# diferente al de otros valores en la lista. Ahora que tiene una comprensión básica de las pruebas condicionales y las sentencias if, echemos 
# un vistazo más de cerca a cómo puede observar valores especiales en una lista y manejar esos valores apropiadamente.

#Sigamos con el ejemplo de la pizzería. La pizzería muestra un mensaje cada vez que se agrega un aderezo a su pizza, mientras se prepara. 
# El código para esta acción se puede escribir de manera muy eficiente haciendo una lista de ingredientes que el cliente ha solicitado y 
# usando un bucle para anunciar cada ingrediente a medida que se agrega a la pizza:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#Pero, ¿y si la pizzería se queda sin pimientos verdes? 
# Una declaración if dentro del bucle for puede manejar esta situación de manera adecuada:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")



        #`2- Checking that a List is not empty.

                #Hemos hecho una suposición simple sobre cada lista con la que hemos trabajado hasta ahora: 
                # hemos asumido que cada lista tiene al menos un elemento. Pronto permitiremos que los usuarios proporcionen la información que 
                # está almacenada en una lista, por lo que no podremos asumir que una lista contiene elementos cada vez que se ejecuta un bucle. 
                # En esta situación, es útil verificar si una lista está vacía antes de ejecutar un bucle/loop "for".

#Como ejemplo, verifiquemos si la lista de ingredientes solicitados está vacía antes de construir la pizza. 
# Si la lista está vacía, le preguntaremos al usuario y nos aseguraremos de que quiera una pizza normal. 
# Si la lista no está vacía, construiremos la pizza tal como lo hicimos en los ejemplos anteriores:
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")



        #`3- Using multiple Lists

                        #People will as for just avout anything, especially when it comes from pizza toppings. 
                        # What if a customer actually wants french fries on their pizza? You can use lists and "if" 
                        # statements to make sure your input makes sense before you act on it.

#Let's watch out for unusual topping requests before we build a pizza.
# The following example defines two lists. The first is a list of available 
# toppings at pizzeria, and the second is the list of toppings that the user has requested. 
# This time, each item in requested_toppings is checked against the list of available toppings before it's added to the pizza:

available_toppings = ['mushrooms', 'olives', 'green peppes',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'frech fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")




    #🦴Styling Your "if" Statement

#En cada ejemplo de este capítulo, ha visto buenos hábitos de estilo. 
# La única recomendación que proporciona PEP 8 para la prueba condicional de estilo es 
# un solo espacio alrededor de los operadores de comparación, como ==, >=, <=. Por ejemplo:

#if age < 4: is better than: if age<4: 




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

