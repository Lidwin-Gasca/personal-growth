
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




