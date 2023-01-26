   
   
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
