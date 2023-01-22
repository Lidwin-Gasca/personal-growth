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
