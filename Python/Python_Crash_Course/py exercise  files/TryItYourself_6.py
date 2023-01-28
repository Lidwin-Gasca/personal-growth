   
   
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
glosario['key()'] = 'En lenguaje de programacion Python:\nEl metodo key() se usa para extraer solo la/las claves de un diccionario/dictionary. Comun en loops "for".'
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
    