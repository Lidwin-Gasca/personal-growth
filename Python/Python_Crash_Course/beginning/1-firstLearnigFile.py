#CHAPTER 2
    #Changing Case In String In Methods#

name = "tu mamaTambien"
print (name.title())  #al poner el .title hace que la primera letra de cada palabra sea mayuscula, 
#si hay una mayuscala en medio de la misma palabra, ésta se vuelve minúscula. 
print (name.upper())    #al poner .upper convierte todas las letras en mayusculas.
print (name.lower())    #al poner .lower convierte toda letra de las palabras en minusculas.

    #Using Variables in Strings#

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

    #Adding Whitespace To Strings with Tabs or Newlines

print("Python") #para agregar un tabulador a tu texto, usa una combinacion de caracteres como el mostrado 
#abajo de esta linea \t .
print("\tPython")   
#para agregar una nueva linea en un string, usa la combinacion de caracteres \n .
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript") #  tambien se pueden combinar ambas combinaciones.


    #Stripping Whitespace

favorite_language = ' python '
print(favorite_language)    #imprimimos el valor tal cual sin alterar.

fav_right_lang = favorite_language.rstrip() #usamos el metodo .rstrip() para quitar el espacio a la derecha 
print(fav_right_lang)                       #de la palabra de dicho valor, y lo imprimimos.

fav_left_lang = favorite_language.lstrip()  #con el metodo .lstrip() quitamos espacio en blaco que se encuentren
print(fav_left_lang)                        #a la izquierda de el valor de nuestra variable (solo si el valor es
                                            #de formato string claro).


    # Avoiding Syntax Errors With Strings
#here's how to use a single and double quotes correctly. apostrophe
messege_1 = "One of Python's strengths is its diverse community."
print(messege_1)

    # Integers/Enteros
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

    # Floats
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

    #Integers and Floats
#cuando divides dos numeros, incluso si son numeros enteros, y que reultado tambien da numero entero, sin 
#imprtar ello, el resultado arrojado por Python sera en formato Float, es decir decimal.Ejemplo:
4/2 ##2.0
print(f"Cuatro entre dos da como resultado:\n {4/2}") ##2.0
#si revuelves enteros (integer) con decimales (float) en cualquier operacion, aun asi recibiras tu resultado
#arrojado en formato Float (decimal).

    #Underscores In Numbers
universe_age = 14_000_000_000
#pudes usar guiones bajos en los numeros largos o incluso cortos, siempre y cuando no terminen en los extremos, 
#ya sea izquierda o derecha.
print(14_000_000_000) ##14000000000

    #Multiple Assignment
x, y, z = 0, 0, 0  #puedes inicializar varias variables en la misma linea, en decir crear variables y darle valor
#debes separar las variables con comas, al inicializar el valor seguir el orden de las variables al dar el valor

    #Constants/constantes
#una contante es aquella variable cuyo valor jamás cambiara durante la vida del programa, como buena practica 
#los programadores usan todas la letras en el nombre de cuya variable en mayusculas. De esta manera quien lo lea
#en un futuro sabra que es una constante. Un ejemplo seria el siguiente:
MAX_CONNECTIONS = 5000

    #The Zen of Python
import this #corre esta linea de codigo en tu consola.


#CHAPTER 3

    #What Is A List ?

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #this is a list
print(bicycles)

    # Accessing Elements In A List

print(bicycles[0]) #los elementos de una lista tienen un  numerado de lista, un indice, no im porta el valor de el 
#elementro de una lista, el primer elemento en ella tendra el indice "0", el sgundo el indice "1" el tercero el 
# indice "2" y asi sucesivamente, por ejmplo el elemento de la lista en el lugar octavo, tendria un indice de "7"
#otgro ejemplo: un elemento en el lugar 32 de la lista tendra un indice "31".
#al escribir el nombre de la variable que tiene una lista como su valor, si escribes el caracter de las casillas 
# #"[]" con un numero adentro, ese numero representara el indice del elemento que deseas visualizar o seleccionar
print(bicycles[0].title()) #tambien puedes alterar los valores/elementos de una lista.

    # Modifying Elements In A List
    
#por ejemplo tenemos una lista de motocicletas, el primer item de la lista en 'honda', Como cambiarias el valor de 
# el primer item?
motorcycles = ['honda', 'yamacha', 'suzuki']
print(motorcycles)
#en la linea debajo esta cambiaremos el valor de el primer item de la lista.
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements To The List
    
    #`1- Appending Elements To The End Of A List
motorcycles.append('subaru')
print(motorcycles)  #el metodo append.() agrega un nuevo valor al final de la lista sin afectar ningun elemento en la lista.
    
    #`2- Inserting Elements Into A List
motorcycles.insert(0, 'kia')    #para usar el metodo insert.() en necesario especificar los parametros del mismo, este 
#metodo tiene dos parametros los cuales se respetan su orden y significado, el primer parametro es para tu como usuario 
#escogas la posicion de el nuevo elemento que estas insertando, vas a declar en que indice deseas posicionar tu nuevo 
#valor. El segundo parametro es para definir el valor que esta siendo insertado/agregado.
print(motorcycles)

    # Removing Elements From A List
    
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
motorcycles.pop(una_buena_moto)
print(motorcycles)


    # Organizing A List

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


    # CHAPTER 4: 
    
    #Working with List

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


    # Making Numerical List

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

        #`4- Looping through a Slice
