
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



