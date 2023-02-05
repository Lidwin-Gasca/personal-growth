


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






