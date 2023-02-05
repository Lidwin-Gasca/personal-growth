





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