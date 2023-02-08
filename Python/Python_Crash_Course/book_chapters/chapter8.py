
        # CHAPTER 8

#                          _____ Fucntions ____

#                                 ____________
#                               /              \
#                              /                \
#                             |                  |
#                             |                  |
#                              \                /
#                               \  ___________ /
#                               /              \
#                              /                \
#                             |                  |
#                             |                  |
#                              \                /
#                               \  ___________ /


                    #En este capítulo, aprenderá a escribir funciones, que son bloques de código con nombre que están diseñados 
                    # para realizar un trabajo específico. Cuando desea realizar una tarea particular que ha definido en una 
                    # función, llama a la función responsable de la misma. Si necesita realizar esa tarea varias veces a lo largo 
                    # de su programa, no necesita escribir todo el código para la misma tarea una y otra vez; simplemente llama a 
                    # la función dedicada a manejar esa tarea, y la llamada le dice a Python que ejecute el código dentro de la 
                    # función. Descubrirá que el uso de funciones hace que sus programas sean más fáciles de escribir, leer, probar 
                    # y corregir.

                    #En este capítulo también aprenderá formas de pasar información a las funciones. Aprenderá a escribir ciertas 
                    # funciones cuyo trabajo principal es mostrar información y otras funciones diseñadas para procesar datos y 
                    # devolver un valor o conjunto de valores. Finalmente, aprenderá a almacenar funciones en archivos separados 
                    # llamados módulos para ayudar a organizar sus archivos de programa principales.








#   🦚  Defining a Funtion

    #Aqui hay una funcion/function llamado greet_user() que imprime saludos (en ingles).
    
def greet_user():                           #(1)
    """Display a simple greeting."""        #(2)
    print("Hello!")                         #(3)
greet_user()                                #(4)

#Este ejemplo muestra la estructura más simple de una función. 

# La línea en ➡(1)⬅ 
# usa la palabra clave def para informar a Python que está definiendo una función. 
# Esta es la definición de la función, que le dice a Python el nombre de la función y, si corresponde, 
# qué tipo de información necesita la función para hacer su trabajo. Los paréntesis contienen esa información. 
# En este caso, el nombre de la función es greeting_user() y no necesita información para hacer su trabajo, p
# or lo que sus paréntesis están vacíos. (Aún así, los paréntesis son obligatorios). 
# Finalmente, la definición termina en dos puntos.

#Cualquier línea sangrada que siga a def greeting_user(): constituye el cuerpo de la función. 
# El texto en ➡(2)⬅ es un comentario llamado docstring, que describe lo que hace la función. 
# Las cadenas de documentos están encerradas entre comillas triples, 
# que Python busca cuando genera documentación para las funciones en los programas.

#La línea ➡(3)⬅ 
# print("¡Hola!") es la única línea de código real en el cuerpo de esta función, 
# por lo que Greet_user() solo tiene un trabajo: print("¡Hola!").


#Cuando quiera usar esta función, llámela. 
# Una llamada de función le dice a Python que ejecute el código en la función. 
# Para llamar a una función, escribe el nombre de la función, seguido de cualquier información necesaria entre paréntesis, 
# como se muestra en linea ➡(4)⬅. Debido a que no se necesita información aquí, 
# llamar a nuestra función es tan simple como ingresar greeting_user(). 
# Como era de esperar, imprime Hello!:







        #`1- Passing Information to a Function
    #
    #Modificada ligeramente, la función greeting_user() no solo puede decirle al usuario ¡Hola! sino también saludarlos por su nombre. 
    # Para que la función haga esto, ingrese 'nombre de usuario' entre paréntesis de la definición de la función en def greeting_user(). 
    # Al agregar 'nombre de usuario' aquí, permite que la función acepte cualquier valor de nombre de usuario que especifique. 
    # La función ahora espera que proporcione un valor para 'nombre de usuario' cada vez que la llame. 
    # Cuando llamas a greeting_user(), puedes pasarle un nombre, como 'jesse', entre paréntesis:
def greet_user(username):
    """Display a simple greting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
    #Ingresar a greeting_user('jesse') llama a greeting_user() y le da a la función la información que necesita para ejecutar la llamada print().
    #La función acepta el nombre que le pasó y muestra el saludo para ese nombre: 
    #           >>> Hello, Jesse!
    #Del mismo modo, al ingresar greeting_user('sarah') llama a greeting_user(), 
    # le pasa 'sarah' e imprime ¡Hola, Sarah! Puede llamar a greeting_user() tantas 
    # veces como desee y pasarle cualquier nombre que desee para producir un resultado predecible cada vez.









        #`2- Arguments and Parameters
    #
    #En la función de saludo_usuario() anterior, definimos saludo_usuario() para requerir un valor para la variable nombre de usuario. 
    # Una vez que llamamos a la función y le dimos la información (el nombre de una persona), imprimió el saludo correcto.

    #El nombre de usuario variable en la definición de greeting_user() es un ejemplo de un parámetro, 
    # una información que la función necesita para hacer su trabajo. 
    # El valor 'jesse' en greeting_user('jesse') es un ejemplo de un argumento. 
    # Un argumento es una pieza de información que se pasa de una llamada de función a una función. 
    # Cuando llamamos a la función, colocamos el valor con el que queremos que trabaje la función entre paréntesis. 
    # En este caso, el argumento 'jesse' se pasó a la función greeting_user() y el valor se asignó al parámetro nombre de usuario.

                #NOTE
    #                La gente a veces habla de argumentos y parámetros indistintamente. 
    #                No se sorprenda si ve las variables en una definición de función 
    #                referidas como argumentos o las variables en una llamada de función 
    #                referidas como parámetros.                    
    #
    #
    #           ⬇
    #           ⬇
    #           ⬇
    #           ⬇
    #           ⬇
    #           ⬇
    #           ⬇
    #           ⬇
    #           ⬇
    #           ⬇
    #           ⬇
    

        #`3-  Passing Arguments

    #Debido a que una definición de función puede tener múltiples parámetros, una llamada de función puede necesitar múltiples argumentos. 
    # Puede pasar argumentos a sus funciones de varias maneras. 
    # Puede usar argumentos posicionales, que deben estar en el mismo orden en que se escribieron los parámetros; 
    # argumentos de palabras clave, donde cada argumento consta de un nombre de variable y un valor; y listas y diccionarios de valores. 
    # Veamos cada uno de estos a su vez.











        #`4- Positional Arguments

    #Cuando llama a una función, Python debe hacer coincidir cada argumento en la llamada a 
    # la función con un parámetro en la definición de la función. La forma más sencilla de 
    # hacerlo se basa en el orden de los argumentos proporcionados. Los valores emparejados 
    # de esta manera se denominan argumentos posicionales.

    #Para ver cómo funciona esto, considere una función que muestre información sobre mascotas. 
    # La función nos dice qué tipo de animal es cada mascota y el nombre de la mascota, como se muestra aquí:

def describe_pet(animal_type, pet_name):                        #(1)
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')                                #(2)

    #La definición muestra que esta función necesita un tipo de animal y el nombre del animal ➡(1)⬅. 
    # Cuando llamamos a describe_pet(), necesitamos proporcionar un animal_type y un nombre, en ese orden. 
    # Por ejemplo, en la llamada de función, el argumento 'hamster' se asigna al parámetro animal_type y el 
    # argumento 'harry' se asigna al parámetro pet_name ➡(2)⬅. En el cuerpo de la función. 
    # estos dos parámetros se utilizan para mostrar información sobre la mascota que se describe.
    #El resultado describe a un hámster llamado Harry:
    #
    #               >>> I have a hamster.
    #               >>> My hamster's name is Harry














        #`5- Multiple Function Calls

    #Puede llamar a una función tantas veces como sea necesario. 
    # Describir una segunda mascota diferente requiere solo una llamada más a describe_pet():
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry') 
describe_pet('dog', 'willie')
    #En esta segunda llamada de función, pasamos describe_pet() los argumentos dog' y 'willie'. 
    # Al igual que con el conjunto anterior de argumentos que usamos, Python hace coincidir 
    # 'perro' con el parámetro tipo_animal y 'willie' con el parámetro nombre_mascota como antes, 
    # la función hace su trabajo, pero esta vez imprime valores para un perro llamado Willie. 
    # Ahora tenemos un hámster llamado Harry y un perro llamado Willie:
    #
    #               >>> I have a hamster.
    #               >>> My hamster's name is Harry
    #
    #               >>> I have a dog.
    #               >>> My dog's name is willie
    #
    #Llamar a una función varias veces es una forma muy eficiente de trabajar. 
    # El código que describe una mascota se escribe una vez en la función. 
    # Luego, cada vez que desee describir una nueva mascota, llame a la función con la información de la nueva mascota. 
    # Incluso si el código para describir una mascota se expandiera a diez líneas, 
    # aún podría describir una nueva mascota en una sola línea llamando a la función nuevamente.
    #
    #Puede usar tantos argumentos posicionales como necesite en sus funciones. 
    # Python funciona a través de los argumentos que proporciona al llamar a la función y 
    # hace coincidir cada uno con el parámetro correspondiente en la definición de la función.



















        #`6- Order Matters in Positional Arguments

    #Puede obtener resultados inesperados si mezcla el orden de los argumentos en una llamada de función cuando usa argumentos posicionales:
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('harry', 'hamster')
    #En esta llamada de función enumeramos primero el nombre y segundo el tipo de animal. 
    # Debido a que el argumento 'harry' aparece primero esta vez, ese valor se asigna al parámetro animal_type. 
    # Asimismo, se asigna 'hámster' al nombre de la mascota. Ahora tenemos un "harry" llamado "Hamster":
    #
    #           >>> I have a harry.
    #           >>> My harry's name is Hamster.
    #
    #Si obtiene resultados divertidos como este, asegúrese de que el orden de los argumentos en 
    # su llamada a la función coincida con el orden de los parámetros en la definición de la función.
















        #`7-  Keyword Arguments

    #Un argumento de palabra clave/keyword es un par de nombre y valor que pasa a una función. 
    # Asocias directamente el nombre y el valor dentro del argumento, así que cuando 
    # pasas el argumento a la función, no hay confusión (no terminarás con un harry llamado Hamster). 
    # Los argumentos de palabras clave/keyword lo liberan de tener que preocuparse por ordenar 
    # correctamente sus argumentos en la llamada a la función y aclaran el rol de cada valor en la llamada a la función.
    #
    #Reescribamos pets.py usando argumentos de palabras clave/keyword para llamar a describe_pet():
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    #
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
    #NOTE
    #   Cuando utilice argumentos de palabras clave, asegúrese de utilizar 
    #   los nombres exactos de los parámetros en la definición de la función.
    #















        #`8- Default Values

    #Al escribir una función, puede definir un valor predeterminado para cada parámetro. 
    # Si se proporciona un argumento para un parámetro en la llamada a la función, Python usa el valor del argumento. 
    # Si no, utiliza el valor predeterminado del parámetro. 
    # Entonces, cuando define un valor predeterminado para un parámetro, puede excluir el argumento 
    # correspondiente que normalmente escribiría en la llamada a la función. 
    # El uso de valores predeterminados puede simplificar sus llamadas a funciones 
    # y aclarar las formas en que se usan normalmente sus funciones.

    #Por ejemplo, si observa que la mayoría de las llamadas a describe_pet() se utilizan para describir perros, 
    # puede establecer el valor predeterminado de animal_type en 'perro'. 
    # Ahora cualquiera que llame a describe_pet() para un perro puede omitir esa información:
