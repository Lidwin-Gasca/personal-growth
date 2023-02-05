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







        #HOW THE INPUT() FUNTION WORKS

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
