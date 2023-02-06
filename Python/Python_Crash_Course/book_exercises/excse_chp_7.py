





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
user = input("\nEscribame un numero, y yo le devolvere una respuesta afirmando si su numero es multipli de 10 o no.  ")
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

while True:
    edad = int(input(prompt))
    
    if edad <= -1:
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




























    #7-7. Infinity:

#Escribe un ciclo que nunca termine y ejecútalo. (Para finalizar el ciclo, presione CTRL-C o cierre la 
# ventana que muestra la salida).