#Haz un diccionario que contenga tres ríos 
# principales y el país por el que pasa cada río. 
# Un par clave-valor podría ser 'nilo': 'egipto'

#           • Use un bucle para imprimir una oración sobre cada río, como El Nilo atraviesa Egipto.

#           • Utilice un bucle para imprimir el nombre de cada río incluido en el diccionario.

#           • Utilice un bucle para imprimir el nombre de cada país incluido en el diccionario.


#Antes de llevar a acabo el ejercicio veamos:

#Que es una lista???
        #Una lista es el conjunto de item, objetos, datos, variables o incluso otras listas dentre de esta.
#se representa de la siguinte manera:
[]
#son dos corchetes

#############  ejemplo:    ##############

    #Declaramos una variable y le damos el valor de una lista vacia
familia = []
familia_gasca = []


    #Indtroducir valores a esa lista usando el metodo "append()"
familia.append('padre')

    #para comprobar que todo ha salido bien mandamos a imprimir
print(familia)

    #continuamos insertando datos
familia.append('madre')
familia.append('hermano')
familia.append('hermana')
familia.append('hijo')
familia.append('hija')

familia_gasca.append('madre')
familia_gasca.append('hermano')
familia_gasca.append('hermana')
familia_gasca.append('hijo')
familia_gasca.append('hija')




    #Declarar un arbol genialogico
arbol_genialogico = []
familia_x = ['padre', 'madre', 'hijo', 'etc']

    #Introducir familia en arbol
arbol_genialogico.append(familia)
arbol_genialogico.append(familia_gasca)
arbol_genialogico.append(familia_x)


print(arbol_genialogico)





        #Que es un diccionario
diccionario = {}
{'nombre': 'valor', 'nom_2': 'val_2', 'nom_3': 'val_3'}

    #para insertar valor y nombre en diccionario es asi:
diccionario["nombre_chavo_del _ocho"] = 'valor_barril'

print(diccionario)




