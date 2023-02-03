   
   
    #6-1. Persona: 

# Use un diccionario para almacenar información sobre una persona que conoce. 
# Almacene su nombre, apellido, edad y la ciudad en la que vive. Debe tener claves como nombre, apellido, edad y ciudad. 
# Imprima cada pieza de información almacenada en su diccionario.
persona = []
padre = {}
persona.append(padre)

padre['nombre'] = 'luis'
padre['apellido'] = 'gasca'
padre['ape_materno'] = 'castillo'
padre['edad'] = 51
padre['ciudad'] = 'las golondrinas'

print(f"Mi padre se llama {padre['nombre'].title()} {padre['apellido'].title()} {padre['ape_materno'].title()}, tiene {padre['edad']} anos de edad y reside en {padre['ciudad'].title()}.")
#podemos usarr cualquiera de estos dos "print()"
print(f"Mi padre se llama {persona[0]['nombre'].title()} {persona[0]['apellido'].title()} {persona[0]['ape_materno'].title()}, tiene {persona[0]['edad']} anos de edad y reside en {persona[0]['ciudad'].title()}.")













    #6-3. Glosario: 

# Se puede usar un diccionario de Python para modelar un diccionario real. 
# Sin embargo, para evitar confusiones, llamémoslo glosario.

#    🕳     Piense en cinco palabras de programación que haya aprendido en los capítulos anteriores. 
#           Utilice estas palabras como claves en su glosario y almacene sus significados como valores.

#    🕳     Imprima cada palabra y su significado como una salida con un formato ordenado. 
#           Puede imprimir la palabra seguida de dos puntos y luego su significado, o imprimir la 
#           palabra en una línea y luego imprimir su significado con sangría en una segunda línea. 
#           Utilice el carácter de nueva línea (\n) para insertar una línea en blanco entre cada 
#           par de palabra y significado en su salida.
glosario = {}
glosario['get()'] = 'En lenguaje de programacion Python:\nEs el metodo que se utiliza para llamar el valor de una clave que no existe en un diccionario.'
glosario['item()'] = 'En lenguaje de programacion Python:\nUn metodo que retorna un listado de las parejas clave-valor de un diccionario/dictionary.'
glosario['key()'] = 'En lenguaje de programacion Python:\nEl metodo key() se usa para extraer solo las claves/keys de un diccionario/dictionary. Comun en loops "for".'
glosario['value()'] = 'En lenguaje de programacion Python:\nSimilar al metodo key(), este extre solo los valores dentro de un diccionario/dictionary.'
glosario['set()'] = 'En lenguaje de programacion Python:\n[puede ser usado en la misma linea de codigo que los otros metodos enlistados en este glosario] \nEs una coleccion de item, las cueles deben ser unicos e irrepetibles. La lista cuyos items queres\norganizar en un set(), ira envuelto dentro de esta misma:\n     set(lista)' 

for variable_clave, variable_valor in glosario.items():
    print(f"\n{variable_clave}:\n  {variable_valor}")












    #6-5 Rios

#Haz un diccionario que contenga tres ríos 
# principales y el país por el que pasa cada río. 
# Un par clave-valor podría ser 'nilo': 'egipto'

#           • Use un bucle para imprimir una oración sobre cada río, como El Nilo atraviesa Egipto.

#           • Utilice un bucle para imprimir el nombre de cada río incluido en el diccionario.

#           • Utilice un bucle para imprimir el nombre de cada país incluido en el diccionario.
rivers = {}
rivers['nilo'] = 'egipto'
rivers['amazon'] = 'brasil'
rivers['bravo'] = 'mexico'
rivers['volga'] = 'russia'
rivers['mississippi'] = 'usa'

for clave_key, valor_value in rivers.items():
    if len(valor_value) == 3:
        print(f"El rio {clave_key.title()} corre por el pais {valor_value.upper()}.")
    else:
        print(f"El rio {clave_key.title()} corre por el pais {valor_value.title()}.")

print('\nNombres de los rios:')
for key in rivers.keys():
    print(f"\t{key.title()}")

print('\nNombres de los paises:')
for value in rivers.values():
    print(f"\t{value.title()}")



    
    






    
    

    #6-6. Encuesta: 
    
# Use el código en favorite_languages.py (página 97 de el libro -Crash Python Course -Erick Matthes-).

#           • Haz una lista de las personas que deberían participar en la encuesta de idiomas favoritos. 

#           • Incluye algunos nombres que ya estén en el diccionario y otros que no.

#           • Recorra la lista de personas que deberían realizar la encuesta. 
#             Si ya han realizado la encuesta, imprima un mensaje agradeciéndoles por responder.
#             Si no han realizado la encuesta, imprima un mensaje invitándoles a realizar la encuesta.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
favorite_languages['omar'] = 'html'
favorite_languages['abelardo'] = 'java'
favorite_languages['erique'] = 'jacva script'
favorite_languages['marvin'] = 'plc'

print(favorite_languages)

for key, value in favorite_languages.items():
    print(f"\n{key.title()} voto por el lenguaje {value.title()}")

if 'erin' not in favorite_languages.keys():
    print(f"\nErin, porfavor toma tu voto de leguaje de programacion preferido")
    













        #6-7. People:
#Comience con el programa que escribió para el ejercicio 6-1 (página 99). 
# Cree dos nuevos diccionarios que representen a diferentes personas y almacene los tres diccionarios en una lista llamada personas. 
# Recorra su lista de personas. Mientras recorre la lista, imprima todo lo que sabe sobre cada persona. 
personas = []
padre = {}
madre = {}
hermano = {}
personas.append(padre)
personas.append(madre)
personas.append(hermano)


padre['nombre'] = 'luis'
padre['apellido'] = 'gasca'
padre['ape_materno'] = 'castillo'
padre['edad'] = 51
padre['ciudad'] = 'las golondrinas'
padre['parentesco'] = 'padre'

madre['nombre'] = 'patricia'
madre['apellido'] = 'garcia'
madre['ape_materno'] = 'leon'
madre['edad'] = 49
madre['ciudad'] = 'michoacan'
madre['parentesco'] = 'madre'


hermano['nombre'] = 'javier'
hermano['apellido'] = 'garcia'
hermano['ape_materno'] = 'leon'
hermano['edad'] = 28
hermano['ciudad'] = 'norte carolina'
hermano['parentesco'] = 'hermano'


for cada_persona in personas:
    print(f"Mi {cada_persona['parentesco']} se llama {cada_persona['nombre'].title()} {cada_persona['apellido'].title()} {cada_persona['ape_materno'].title()}, tiene {cada_persona['edad']} anos de edad y reside en {cada_persona['ciudad'].title()}.")



















    #6-8. Pets:

#Haga varios diccionarios, donde cada diccionario represente una mascota diferente. 
# En cada diccionario, incluya el tipo de animal y el nombre del dueño. Guarde estos diccionarios en una lista llamada mascotas. 
# A continuación, recorra su lista y, mientras lo hace, imprima todo lo que sepa sobre cada mascota.
mascotas = []
perro = {}
gato = {}
venado = {}
mascotas.append(perro)
mascotas.append(gato)
mascotas.append(venado)

perro['nombre'] = 'rosmi'
perro['edad'] = '18'
perro['dueño'] = 'adriana'
perro['caracter'] = 'agotado'
perro['mascota'] = 'perro'
perro['parentescoDelDueño'] = 'prima'

gato['nombre'] = 'sombra'
gato['edad'] = '16'
gato['dueño'] = 'paola'
gato['caracter'] = 'agotado'
gato['mascota'] = 'gato'
gato['parentescoDelDueño'] = 'prima'

venado['nombre'] = 'bambi'
venado['edad'] = '5'
venado['dueño'] = 'guillermo'
venado['caracter'] = 'territorial'
venado['mascota'] = 'venado'
venado['parentescoDelDueño'] = 'abuelo'

for each in mascotas:
    print(f"El {each['mascota']} de mi {each['parentescoDelDueño']} {each['dueño'].title()} se llama {each['nombre'].title()}, tiene {each['edad']} años de edad, y es de caracter {each['caracter']}.") 














    #6-9. Favorite Places:

#Haz un diccionario llamado lugares_favoritos. 
# Piense en tres nombres para usar como claves en el diccionario y almacene de uno a tres lugares favoritos para cada persona. 
# Para hacer este ejercicio un poco más interesante, pídales a algunos amigos que mencionen algunos de sus lugares favoritos. 
# Recorre el diccionario e imprime el nombre de cada persona y sus lugares favoritos.
lugares_favoritos = {}
lugares_favoritos['jhon'] = 'hogar'
lugares_favoritos['limber'] = 'cyber'
lugares_favoritos['nacaranda'] = 'mar'

for clave, valor in lugares_favoritos.items():
    print(f"A mi amistad {clave.title()} le gusta el {valor} como su lugar favorito.")









    #6-10. Favorite Numbers:

#Modifique su programa del Ejercicio 6-2 (página 99) para que cada persona pueda tener más de un número favorito. 
# Luego escriba el nombre de cada persona junto con sus números favoritos.
personas = []

for persona in range(3):
    nueva_persona = {'nombre': '', 'numero_favorito': '', 'num_fav_2': ''}
    personas.append(nueva_persona)

personas[0]['nombre'] = 'Lucia'
personas[1]['nombre'] = 'Fernando'
personas[2]['nombre'] = 'Hernesto'
personas[0]['numero_favorito'] = 1
personas[1]['numero_favorito'] = 3
personas[2]['numero_favorito'] = 5
personas[0]['num_fav_2'] = 2
personas[1]['num_fav_2'] = 4
personas[2]['num_fav_2'] = 6

for cada_persona in personas:
    print(f"A mi amistad {cada_persona['nombre'].title()} le encanta el numero {cada_persona['num_fav_2']}, pero su numero favorito es {cada_persona['numero_favorito']}.")
















    #6-11 Cities:

#Haz un diccionario llamado ciudades. Usa los nombres de tres ciudades como claves en tu diccionario. 
# Cree un diccionario de información sobre cada ciudad e incluya el país en el que se encuentra la 
# ciudad, su población aproximada y un dato sobre esa ciudad. Las claves para el diccionario de cada 
# ciudad deben ser algo como país, población y un hecho curioso de tal ciudad. Imprime el nombre de cada ciudad y toda la 
# información que tengas guardada sobre ella.
cities = {
    "London": {
        "country": "England",
        "population": 8787892,
        "fact": "London is home to the Big Ben and the Tower of London."
    },
    "Paris": {
        "country": "France",
        "population": 2141000,
        "fact": "Paris is known as the City of Love and is famous for its Eiffel Tower."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13395000,
        "fact": "Tokyo is the most populous city in the world and is known for its technology and vibrant street life."
    }
}

for city in cities:
    print(f"City: {city}")
    print(f"Country: {cities[city]['country']}")
    print(f"Population: {cities[city]['population']}")
    print(f"Fact: {cities[city]['fact']}")
    print("\n")








    #6-12. Extensions:

#Ahora estamos trabajando con ejemplos que son lo suficientemente complejos como para que puedan extenderse de muchas maneras. 
# Utilice uno de los programas de ejemplo de este capítulo y amplíelo agregando nuevas claves y valores, 
# cambiando el contexto del programa o mejorando el formato de la salida.

 








    #7-1. Rental Car:

#Escriba un programa que le pregunte al usuario qué tipo de coche de alquiler le gustaría.
# Imprime un mensaje sobre ese auto, como "Déjame ver si puedo encontrarte un Subaru".







    #7-2. Restaurant Seating:

#Escriba un programa que le pregunte al usuario cuántas personas hay en su grupo de cena. 
# Si la respuesta es más de ocho, imprima un mensaje diciendo que tendrán que esperar por una mesa. 
# De lo contrario, informe que su mesa está lista.







    #7-3. Multiples of Ten:

#Solicite al usuario un número y luego informe si el número es un múltiplo de 10 o no.