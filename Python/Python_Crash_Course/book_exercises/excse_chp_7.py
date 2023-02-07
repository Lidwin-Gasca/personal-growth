





    #7-1. Rental Car:

#Escriba un programa que le pregunte al usuario qué tipo de coche de alquiler le gustaría.
# Imprime un mensaje sobre ese auto, como "Déjame ver si puedo encontrarte un Subaru".
user = input("Diganos que marca de coche le gustaria alquilar?  ")
if len(user) <= 3:
    print(f"\n\tTenemos la siguiente lista de choches para la marca {user.upper()}.\n")
else:
    print(f"\n\tTenemos la siguiente lista de choches para la marca {user.title()}.\n")






    #7-2. Restaurant Seating:

#Escriba un programa que le pregunte al usuario cuántas personas hay en su grupo de cena. 
# Si la respuesta es más de ocho, imprima un mensaje diciendo que tendrán que esperar por una mesa. 
# De lo contrario, informe que su mesa está lista.
user = input("\nCuantas personas mayores de seis años estaran cenando con usted (usted incluido)?  ")
user = int(user)

if user >= 8:
    print(f"El tiempo de espera es una hora\n")
else:
    print("Porfavor pase, su mesa esta lista\n")






    #7-3. Multiples of Ten:

#Solicite al usuario un número y luego informe si el número es un múltiplo de 10 o no.
user = input("\nEscribame un numero, y yo le devolvere una respuesta afirmando si su numero es multiplo de 10 o no.  ")
user = int(user)

if user % 10 == 0:
    print("\tSu numeor Si es multiplo de 10")
else:
    print("\tSu numero No es multiplo de 10")












    #7-4. Pizza Toppings:

#Escriba un ciclo que solicite al usuario que ingrese una serie de ingredientes para la pizza hasta que ingrese 
# un valor de 'salir'. 
# A medida que ingresen cada ingrediente, imprima un mensaje que diga que agregará ese ingrediente a su pizza.

coberturas = []
prompt = "\nIngrese su vuberturas para su pizza."
prompt += "\n(Escriba 'salir' para dejar de dar coberturas.)\n\t\t\t\t\t\t"
while True:
    cobertura = input(prompt)

    if cobertura == 'salir':
        print(f"Muy bien las coberturas que escogio son: {coberturas}")
        break
    else:
        coberturas.append(cobertura)
        print(f"Muy bien, {cobertura.title()} agregado.")






















    #7-5. Movie Tickets:

#Un cine cobra diferentes precios de boletos dependiendo de la edad de la persona. 
# Si una persona es menor de 3 años, la entrada es gratuita; si son entre 3 y 12, el boleto cuesta $10; 
# y si son mayores de 12 años, el boleto cuesta $15. Escriba un ciclo en el que pregunte a los usuarios 
# su edad y luego dígales el costo de su boleto de cine.


prompt = "\n\nCual es su edad?.  "
max_ = 0
while True:
    edad = int(input(prompt))
    max_ = max_ + 1
    if max_ == 5:
        print("\nSolo caben 4 personas, vuelva a la fila.")
        break
    elif edad <= -1:
        print("\nEsto no es broma, es en serio ( •̀ ω •́ )✧")
    elif edad <= 3:
        print(f"\nSu crio puede entrar gratis.")
    elif edad <= 12:
        print("\nEl pase del niño tiene un costo de $10 dolares.")
    elif edad <= 115:
        print("\nEl pase de entrada le será de 15 dolares.")
    else:
        print("\nNo te mames mery jain")



















    #7-6. Three Exits:

#Escriba diferentes versiones del Ejercicio 7-4 o del Ejercicio 7-5 que hagan cada uno de los 
# siguientes al menos una vez:

#   🕳 Use una prueba condicional en la instrucción while para detener el ciclo.

#   🕳 Use una variable activa para controlar cuánto tiempo se ejecuta el ciclo.

#   🕳 Use una declaración de interrupción para salir del ciclo cuando el usuario ingrese un valor de 'salir'.

coberturas = []
prompt = "\nIngrese su coberturas para su pizza."
prompt += "\n(Escriba 'salir' para dejar de dar coberturas.)\n\t\t\t\t\t\t"
prompt += "\nPuede tener un maximo de 5 coberturas"
max_ = 0
while True:
    cobertura = input(prompt)

    if cobertura == 'salir' or max_ == 4:                                       #⬅En esta linea de codigo agregue el or max_ == 5 para cumplir
        print(f"Muy bien las coberturas que escogio son: {coberturas}")        #con la regla "2" de este ejercicio y a su vez cuple la primera
        break                                                                  #regla, y la tercera ya estaba implementada.
    else:
        coberturas.append(cobertura)
        max_ = max_ + 1
        print(f"Muy bien, {cobertura.title()} agregado.")
        print(max_)


























    #7-7. Infinity:

#Escribe un ciclo que nunca termine y ejecútalo. (Para finalizar el ciclo, presione CTRL-C o cierre la 
# ventana que muestra la salida).
max_ = 0
while max_ < 5:
    #max_ = max_ + 1
    print("Este bucle es infinito por que 'max_' vale cero y nunca llegara a valer 5 y para parar el bucle.")


#ejemplo dos:
num = 0
while True:
    # num = num + 1
    if num == 5:
        break
    else:
        print("Este bucle es infinito porque la variable 'num' no puede activar el 'if' si su valor nunca se convierte a 5.")