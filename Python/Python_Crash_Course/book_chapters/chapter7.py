            #CAPITULO 7         
#  🐍                     USER INPUT AND WHILE LOOPS


#La mayoría de los programas están escritos para resolver el problema de un usuario final. 
# Para hacerlo, generalmente necesita obtener cierta información del usuario. 
# Para un ejemplo simple, digamos que alguien quiere saber si tiene la edad suficiente para votar.
#Si escribe un programa para responder a esta pregunta, necesita saber la edad del usuario antes de poder proporcionar una respuesta. 
# El programa deberá pedirle al usuario que ingrese/'input', su edad; una vez que el programa tiene esta entrada, 
# puede compararla con la edad de votación para determinar si el usuario tiene la edad suficiente y luego informar el resultado.

#En este capítulo, aprenderá cómo aceptar la entrada del usuario para que su programa pueda trabajar con ella. 
# Cuando su programa necesite un nombre, podrá pedirle al usuario un nombre. Cuando su programa necesite una 
# lista de nombres, podrá solicitar al usuario una serie de nombres. Para ello, utilizará la función input().

#You'll also learn how to keep programs running as long as users want them to, so they can enter as much 
# information as they need to; then, your program can work with that information. 
# You'll use Python's while loop to keep programs running as long as certain conditions remain true.

#Con la capacidad de trabajar con la entrada del usuario y la capacidad de controlar cuánto tiempo 
# se ejecutan sus programas, podrá escribir programas totalmente interactivos.







        #🦚HOW THE INPUT() FUNTION WORKS

#La función input() pausa su programa y espera a que el usuario ingrese algún texto. 
# Una vez que Python recibe la entrada del usuario, asigna esa entrada a una variable para que sea conveniente para usted trabajar con ella.

#Por ejemplo, el siguiente programa le pide al usuario que ingrese algún texto, luego muestra ese mensaje al usuario:
message = input("Telll me something, and I will repeat it back to you:")
print(message)

#La función input() toma un argumento: el mensaje o las instrucciones que queremos mostrar al usuario para que sepa qué hacer. 
# En este ejemplo, cuando Python ejecuta la primera línea, el usuario ve el mensaje Dime algo y te lo repetiré:. 
# El programa espera mientras el usuario ingresa su respuesta y continúa después de que el usuario presiona ENTER. 
# La respuesta se asigna al mensaje variable, luego print (mensaje) muestra la entrada al usuario.

#Sublime Text and many other editors don't run programs that prompt the user for input. 
# You can use these editors to write programs that prompt for input, but you'll need to run these programs from a terminal. 
# See "Running Python Programs from a Terminal" on page 12.











        #`1- Writing Clear Prompts.

# Cada vez que utilice la función input(), debe incluir un aviso claro y fácil de seguir que le diga al usuario exactamente 
# qué tipo de información está buscando. Cualquier declaración que le diga al usuario qué ingresar debería funcionar. 
# Por ejemplo:
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#Agregue un espacio al final de sus avisos (después de los dos puntos en el ejemplo anterior) para separar el 
# aviso de la respuesta del usuario y dejarle claro a su usuario dónde ingresar su texto.

#A veces, querrá escribir un aviso que sea más largo que una línea. Por ejemplo, es posible que desee decirle 
# al usuario por qué está solicitando cierta entrada. Puede asignar su aviso a una variable y pasar esa 
# variable a la función input(). Esto le permite construir su solicitud en varias líneas, luego escribir 
# una declaración de entrada () limpia.
prompt = "If you  tell us who you are, we, can personalize the messeges you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello,{name}") #El mensaje ahora ocupa dos líneas, nuevamente con un espacio después del signo de interrogación para mayor claridad.
#Este ejemplo muestra una forma de construir una cadena de varias líneas. 
# La primera línea asigna la primera parte del mensaje al aviso variable. 
# En la segunda línea, el operador += toma la cadena que se asignó a prompt y agrega la nueva cadena al final.







        #`2- Using int() to Accept Numerical input.

#Cuando usa la función input(), Python interpreta todo lo que el usuario ingresa como una cadena. 
# Considere la siguiente sesión de interpretación, que solicita la edad del usuario:
age = input("How old are you? ")
#el valor de "age" seria un valor de tipo string. y no de numeros (entero/float).

#El usuario ingresa el número 21, pero cuando le preguntamos a Python por el valor de la edad, devuelve '21', 
# la representación de cadena del valor numérico ingresado. 
# Sabemos que Python interpretó la entrada como una cadena porque el número ahora está entre comillas. 
# Si todo lo que quiere hacer es imprimir la entrada, esto funciona bien. 
# Pero si intenta usar la entrada como un número, obtendrá un error: ↘
#age = input("How old are you? ")                                     ⬇
#age >= 18                                                           ↙
#Traceback (most recent call last): File "<stdin>", line 1, in <module>
#TypeError: unorderable types: str() >= int()

#Podemos resolver este problema usando la función int(), que le dice a Python que trate la entrada como un valor numérico. 
# La función int() convierte una representación de cadena de un número en una representación numérica, como se muestra aquí:
age == input("How old are you? ")
#>>>How old are you? 21
age = int(age)
age >= 18
#True

#En este ejemplo 👆, cuando ingresamos 21 en el indicador, Python interpreta el número como una cadena, 
# pero el valor se convierte en una representación numérica mediante int().

#¿Cómo se usa la función int() en un programa real? 
# Considere un programa que determina si las personas son lo suficientemente altas como para subirse a una montaña rusa:
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
#El programa puede comparar la altura con 48 porque altura = int(altura) convierte el valor de 
# entrada en una representación numérica antes de realizar la comparación. 
# Si el número ingresado es mayor o igual a 48, le decimos al usuario que es lo suficientemente alto:
    #>>>How tall are you, in inches? 71
    #>>>You're tall enough to ride!
#Cuando usa entradas numéricas para hacer cálculos y comparaciones. 
# asegúrese de convertir primero el valor de entrada a una representación numérica.







    #  THE MODULO OPERATOR 

#Una herramienta útil para trabajar con información numérica es el operador módulo (*). 
# que divide un número por otro número y devuelve el resto.

4 % 3 # = 1

5 % 3 # = 2

6% 3 # 0

7 % 3 # = 1

#El operador módulo no te dice cuántas veces cabe un número en otro; simplemente te dice cuál es el resto.

#Cuando un número es divisible por otro número, el resto es 0, por lo que el operador de módulo siempre 
# devuelve 0. Puedes usar este hecho para determinar si un número es par o impar:
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n The number {number} is even.")
else:
    print(f"The number {number} is odd.")
#Los números pares siempre son divisibles por dos, por lo que si el módulo de un número y 
# dos es cero (aquí, si el número % 2 == 0) el número es par. De lo contrario, es raro.





#🦚Introducing "while" Loops



    #El bucle for toma una colección de elementos y ejecuta un bloque de código una vez para cada elemento de la colección. 
    # Por el contrario, el bucle while se ejecuta mientras una determinada condición sea verdadera.





        #`1- The While Loop in Ation

#Puede usar un bucle while para contar una serie de números. Por ejemplo, el siguiente ciclo while cuenta de 1 a 5:
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1
#En la primera línea, comenzamos a contar desde 1 asignando número_actual el valor 1. 
# El ciclo while se configura para seguir ejecutándose siempre que el valor del número actual sea menor o igual a 5. 
# El código dentro del ciclo imprime el valor de current_number y luego agrega 1 a ese valor con el número actual

#  += 1. (El operador += es una abreviatura de número_actual número actual + 1.) = Python repite el bucle siempre que la 
# condición número_actual <= 5 sea verdadera. Como 1 es menor que 5, Python imprime 1 y luego suma 1, haciendo el número actual 2. 
# Como 2 es menor que 5, Python imprime 2 y suma 1 nuevamente, haciendo el número actual 3, y así sucesivamente.
#  Una vez que el valor de current_number es mayor que 5, el ciclo deja de ejecutarse y el programa finaliza:
#   |1       |                           ⬇
#   |2       |                         ↙
#   |3       |                       ↙
#   |4       |⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅
#   |5       |
#    ---------
#Es muy probable que los programas que usa todos los días contengan bucles while. 
# Por ejemplo, un juego necesita un bucle while para seguir ejecutándose todo el tiempo que desee seguir jugando y, 
# por lo tanto, puede dejar de ejecutarse tan pronto como le pida que lo abandone. 
# Los programas no serían divertidos de usar si dejaran de ejecutarse antes de que se lo indiquemos o continuaran 
# ejecutándose incluso después de que quisiéramos salir, por lo que los bucles while son muy útiles.




    #`2- Letting the User Choose When to Quit

#Podemos hacer que el programa parrot.py se ejecute todo el tiempo que el usuario desee colocando la mayor parte del programa
#  dentro de un ciclo while. 
# Definiremos un valor de salida y luego mantendremos el programa ejecutándose mientras el usuario no haya ingresado el valor de salida:
prompt = "\nTell me somethin, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""

while message != 'quit':
    message = input(prompt)
    print(message)
#La primera vez que pasa por el ciclo, el mensaje es solo una cadena vacía, por lo que Python ingresa al ciclo. 
# En la entrada del mensaje (solicitud), Python muestra la solicitud y espera a que el usuario ingrese su entrada. 
# Todo lo que ingresan se asigna a un mensaje y se imprime; luego, Python vuelve a evaluar la condición en la instrucción while. 
# Siempre que el usuario no haya ingresado la palabra 'salir', el aviso se muestra nuevamente y Python espera más información. 
# Cuando el usuario finalmente ingresa 'salir', Python deja de ejecutar el ciclo while y el programa finaliza.





#Este programa funciona bien, excepto que imprime la palabra 'salir' como si fuera un mensaje real. 
# Una simple prueba if soluciona esto:
prompt = "\nTell me somethin, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
#Ahora el programa realiza una verificación rápida antes de mostrar el mensaje y solo imprime 
# el mensaje si no coincide con el valor de salida.









        #`3- Using a Flag

#En el ejemplo anterior, hicimos que el programa realizara ciertas tareas mientras una condición determinada era verdadera. 
# Pero, ¿qué pasa con los programas más complicados en los que muchos eventos diferentes pueden hacer que el programa deje de ejecutarse?

#Por ejemplo, en un juego, varios eventos diferentes pueden terminar el juego. 
# Cuando el jugador se queda sin barcos, se acaba el tiempo o las ciudades que se suponía que debían proteger son destruidas, 
# el juego debería terminar. Debe terminar si ocurre cualquiera de estos eventos. 
# Si pueden ocurrir muchos eventos posibles para detener el programa, tratar de probar todas estas condiciones 
# en una instrucción while se vuelve complicado y difícil.

#Para un programa que debe ejecutarse solo mientras muchas condiciones sean verdaderas, puede definir una variable 
# que determine si todo el programa está activo o no. Esta variable, llamada bandera, actúa como una señal para el programa. 
# Podemos escribir nuestros programas para que se ejecuten mientras el indicador esté establecido en Verdadero y 
# dejen de ejecutarse cuando cualquiera de varios eventos establezca el valor del indicador en Falso. Como resultado, 
# nuestra declaración while general necesita verificar solo una condición: si la bandera es actualmente True o no.
#  Luego, todas nuestras otras pruebas (para ver si ha ocurrido un evento que debería establecer el indicador en Falso) 
# se pueden organizar ordenadamente en el resto del programa.

#Agreguemos una bandera a parrot.py de la sección anterior.
#  Este indicador, al que llamaremos activo (aunque puede llamarlo como quiera), 
# controlará si el programa debe continuar ejecutándose o no:
prompt = "\nTell me somethin, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
#Este programa tiene el mismo resultado que el ejemplo anterior donde colocamos la prueba condicional directamente 
# en la instrucción while. Pero ahora que tenemos una bandera para indicar si el programa general está en un estado
# activo, sería fácil agregar más pruebas (como declaraciones elif) para eventos que deberían causar que active se 
# convierta en False. Esto es útil en programas complicados como juegos en los que puede haber muchos eventos que 
# deberían hacer que el programa deje de ejecutarse. Cuando cualquiera de estos eventos hace que la bandera activa 
# se vuelva Falsa, el bucle principal del juego se cerrará, se mostrará un mensaje de Fin del juego y se le dará al
# jugador la opción de volver a jugar.







        #`4- Using break to Exit a Loop

#Para salir de un ciclo while inmediatamente sin ejecutar ningún código restante en el ciclo, independientemente de 
# los resultados de cualquier prueba condicional, use la instrucción break. La instrucción break dirige el flujo de 
# su programa; puede usarlo para controlar qué líneas de código se ejecutan y cuáles no, por lo que el programa solo 
# ejecuta el código que desea, cuando lo desea.

#Por ejemplo, considere un programa que le pregunta al usuario sobre los lugares que ha visitado. Podemos detener el 
# ciclo while en este programa llamando a break tan pronto como el usuario ingrese el valor 'quit':
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")

#Un ciclo que comienza con while True se ejecutará para siempre a menos que llegue a una declaración de ruptura. 
# El ciclo en este programa continúa pidiéndole al usuario que ingrese los nombres de las ciudades en las que ha 
# estado hasta que ingresa 'salir'. 
# Cuando ingresan "quit", se ejecuta la instrucción break, lo que hace que Python salga del bucle.
#NOTE:
#Puede usar la instrucción break en cualquiera de los bucles de Python. 
# Por ejemplo, podría usar break para salir de un bucle for que está trabajando en una lista o un diccionario.







        #`5-   Using continue in a Loop

#En lugar de salir de un bucle por completo sin ejecutar el resto de su código, puede usar la instrucción 
# continuar para volver al principio del bucle en función del resultado de una prueba condicional. 
# Por ejemplo, considere un ciclo que cuenta del 1 al 10 pero imprime solo los números impares en ese rango:
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
#Si el módulo es 0 (lo que significa que número_actual es divisible por 2), la declaración de continuación 
# le dice a Python que ignore el resto del ciclo y regrese al principio. Si el número actual no es divisible 
# por 2, se ejecuta el resto del ciclo y Python imprime el número actual.








        #`6- Avoiding Infinite Loops

# Cada ciclo while necesita una forma de dejar de ejecutarse para que no continúe ejecutándose para siempre. 
# Por ejemplo, este ciclo de conteo debería contar del 1 al 5:
x = 1
while x <= 5:
    print(x)
    x += 1
#Pero si accidentalmente omite la línea x += 1 (como se muestra a continuación), el ciclo se 
# ejecutará para siempre:
x = 1 
while x <= 5:   #este loop/bucle correra por siempre!!!
    print(x)
#Ahora el valor de x comenzará en 1 pero nunca cambiará. Como resultado, la prueba condicional x <= 5 siempre 
# se evaluará como True y el ciclo while se ejecutará para siempre, imprimiendo una serie de 1, como este.

#Todos los programadores escriben accidentalmente un bucle while infinito de vez en cuando, especialmente cuando 
# los bucles de un programa tienen condiciones de salida sutiles. Si su programa se atasca en un bucle infinito, 
# presione CTRL-C o simplemente cierre la ventana de terminal que muestra la salida de su programa.

#Para evitar escribir bucles infinitos, pruebe cada bucle while y asegúrese de que el bucle se detenga cuando lo 
# espere. Si desea que su programa finalice cuando el usuario ingrese un cierto valor de entrada, ejecute el 
# programa e ingrese ese valor. Si el programa no finaliza, analice la forma en que su programa maneja el valor 
# que debería causar la salida del ciclo. Asegúrese de que al menos una parte del programa pueda hacer que la 
# condición del ciclo sea Falsa o que llegue a una declaración de interrupción.

















