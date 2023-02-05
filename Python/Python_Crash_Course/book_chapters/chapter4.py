
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
print("Here are the first three players on my team:")
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

