
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








# 🦚      Defining a Funtion

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
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='willie')
    #Cambiamos la definición de describe_pet() para incluir un valor predeterminado, 'perro', para animal_type. 
    # Ahora, cuando se llama a la función sin especificar animal_type, Python sabe usar el valor 'perro' para este parámetro:
    #           >>> I have a dog.
    #           >>> My dog's name is Willie.
    #
    #Tenga en cuenta que se tuvo que cambiar el orden de los parámetros en la definición de la función. 
    # Debido a que el valor predeterminado hace innecesario especificar un tipo de animal como argumento, 
    # el único argumento que queda en la llamada de función es el nombre de la mascota. 
    # Python todavía interpreta esto como un argumento posicional, por lo que si se llama a la función 
    # solo con el nombre de una mascota, ese argumento coincidirá con el primer parámetro enumerado en 
    # la definición de la función. Esta es la razón por la que el primer parámetro debe ser pet_name.
    #
    #La forma más sencilla de usar esta función ahora es proporcionar solo el nombre de un perro en la llamada a la función:
    #
    #           desribe_pet('willie')
    #
    #Esta llamada de función tendría el mismo resultado que el ejemplo anterior. 
    # El único argumento proporcionado es 'willie', por lo que se compara con el primer parámetro de la definición, pet_name. 
    # Debido a que no se proporciona ningún argumento para animal_type, Python usa el valor predeterminado 'perro'.
    #
    #Para describir un animal que no sea un perro, podría usar una llamada de función como esta:
    #       
    #           describe_pet(pet_name='harry', animal_type='hamster')
    #
    #Debido a que se proporciona un argumento explícito para animal_type, Python ignora el valor predeterminado del parámetro.
    #
    #   NOTE:
    #       Cuando usa valores predeterminados, 
    #       cualquier parámetro con un valor 
    #       predeterminado debe aparecer después 
    #       de todos los parámetros que no tienen 
    #       valores predeterminados. Esto le 
    #       permite a Python continuar 
    #       interpretando correctamente los 
    #       argumentos posicionales.














        #`9- Equivalent Function Calls

    #Debido a que los argumentos posicionales, los argumentos de palabras clave y los valores predeterminados se pueden usar juntos, a menudo tendrá 
    # varias formas equivalentes de llamar a una función. Considere la siguiente definición para describe_pet() con un valor predeterminado provisto:
    #
    #           def describe_pet(pet_name, animal_type='dog'):
    #
    #Con esta definición, siempre se debe proporcionar un argumento para pet_name, y este valor se puede proporcionar utilizando el formato posicional 
    # o de palabra clave. Si el animal que se describe no es un perro, se debe incluir un argumento para animal_type en la llamada, y este argumento 
    # también se puede especificar usando el formato posicional o de palabra clave.
    #Todas las siguientes llamadas funcionarían para esta función:
    #
    # A dog named Willie. 
describe_pet('willie')
describe_pet (pet_name='willie')
    #
    # A hamster named Harry. 
describe_pet('harry', 'hamster') 
describe_pet (pet_name='harry', animal_type='hamster') 
describe_pet (animal_type='hamster', pet_name='harry')
    # Cada una de estas llamadas de función tendría el mismo resultado que los ejemplos anteriores.
    #NOTE:
    #       Realmente no importa qué estilo de llamada uses. 
    #       Siempre que sus llamadas de función produzcan la 
    #       salida que desea, use el estilo que le resulte 
    #       más fácil de entender.













        #`10- Avoiding Arguments Errors

    #Cuando comience a usar, no se sorprenda si encuentra errores sobre argumentos no coincidentes. 
    # Los argumentos no coincidentes ocurren cuando proporciona menos o más argumentos de los que necesita una función para hacer su trabajo. 
    # Por ejemplo, esto es lo que sucede si tratamos de llamar a describe_pet() sin argumentos:
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet()
    #Python reconoce que falta cierta información en la llamada a la función, y el rastreo nos dice que:
    #
    #
    #        Traceback (most recent call last):
    # (1)        File "c:\Users\memit\OneDrive\Documents\GitHub\personal-growth\Python\Python_Crash_Course\book_chapters\tempCodeRunnerFile.py", line 5, in <module>
    # (2)            describe_pet()
    # (3)    TypeError: describe_pet() missing 1 required positional argument: 'pet_name'
    #
    #
    #
    #
    #En ➡(1)⬅, el rastreo nos dice la ubicación del problema, lo que nos permite mirar hacia atrás y ver que algo salió mal en nuestra llamada de función. 
    # En ➡(2)⬅, la llamada a la función infractora se escribe para que la veamos. 
    # En ➡(3)⬅, el rastreo nos dice que a la llamada le faltan dos argumentos e informa los nombres de los argumentos que faltan. 
    # Si esta función estuviera en un archivo separado, probablemente podríamos reescribir 
    # la llamada correctamente sin tener que abrir ese archivo y leer el código de la función.
    #
    #Python es útil porque lee el código de la función por nosotros y nos dice los nombres de los argumentos que debemos proporcionar. 
    # Esta es otra motivación para darle a sus variables y funciones nombres descriptivos. Si lo hace, 
    # los mensajes de error de Python serán más útiles para usted y cualquier otra persona que pueda usar su código.
    #
    #Si proporciona demasiados argumentos, debería obtener un seguimiento similar que pueda ayudarlo 
    # a hacer coincidir correctamente su llamada de función con la definición de función.
















        #   🦚 Return Values

    #Una función no siempre tiene que mostrar su salida directamente. 
    # En su lugar, puede procesar algunos datos y luego devolver un valor o un conjunto de valores. 
    # El valor que devuelve la función se llama valor de retorno. 
    # La declaración de retorno toma un valor desde dentro de una función y lo envía de vuelta a la línea que llamó a la función. 
    # Los valores devueltos le permiten mover gran parte del trabajo duro de su programa a funciones, lo que puede simplificar el cuerpo de su programa.











        #`1- Returning a Simple Value

#Veamos una función que toma un nombre y apellido, y devuelve un nombre completo con un formato limpio:
def get_formatted_name(first_name, last_name):  #(1)
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"     #(2)
    return full_name.title()                    #(4)

musician = get_formatted_name('jimi', 'hendrix')#(4)
print(musician)
    #La definición de get_formatted_name() toma como parámetros un nombre y apellido ➡(1)⬅. 
    # La función combina estos dos nombres, agrega un espacio entre ellos y asigna el resultado a full_name ➡(2)⬅. 
    # El valor de full_name se convierte en mayúsculas y minúsculas y luego se devuelve a la línea de llamada en ➡(3)⬅.
    #Cuando llama a una función que devuelve un valor, debe proporcionar una variable a la que se le pueda asignar el valor devuelto. 
    # En este caso, el valor devuelto se asigna a la variable músico en ➡(4)⬅. 
    # El resultado muestra un nombre perfectamente formateado formado por las partes del nombre de una persona:
    #
    #           >>> Jimi Hendrix
    #
    #Esto puede parecer mucho trabajo para obtener un nombre bien formateado cuando podríamos haber escrito simplemente:
    #           >>> print("Jimi Hendrix")
    #
    #Pero cuando considera trabajar con un programa grande que necesita almacenar muchos nombres y apellidos por separado, 
    # funciones como get_formatted_name() se vuelven muy útiles. 
    # Usted almacena el nombre y el apellido por separado y luego llama a esta función cada vez que desea mostrar un nombre completo.













        #`2- Making an Argument Optional

    #A veces tiene sentido hacer que un argumento sea opcional para que las personas que usan la función puedan optar por proporcionar 
    # información adicional solo si así lo desean. Puede usar valores predeterminados para hacer que un argumento sea opcional.
    #
    #Por ejemplo, digamos que queremos expandir get_formatted_name() para manejar también los segundos nombres. 
    # Un primer intento de incluir segundos nombres podría verse así:
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jhon', 'lee', 'hooker')
print(musician)

    #Esta función funciona cuando se le asigna un nombre, un segundo nombre y un apellido. 
    # La función toma las tres partes de un nombre y luego construye una cadena a partir de ellas. 
    # La función agrega espacios cuando corresponde y convierte el nombre completo en mayúsculas y minúsculas:
    #
    #           >>> Jhon Lee Hooker
    #
    #Pero los segundos nombres no siempre son necesarios, y esta función, tal como está escrita, 
    # no funcionaría si intentara llamarla solo con un nombre y un apellido. Para hacer que el 
    # segundo nombre sea opcional, podemos darle al argumento segundo_nombre un valor predeterminado 
    # vacío e ignorar el argumento a menos que el usuario proporcione un valor. Para hacer que 
    # get_formatted_name() funcione sin un segundo nombre, establecemos el valor predeterminado 
    # de middle_name en una cadena vacía y lo movemos al final de la lista de parámetros:
def get_formatted_name(first_name, last_name, middle_name=''):  #(1)
    """Return a full name, neatly formatted"""
    if middle_name:                                             #(2)
        full_name = f"{first_name} {middle_name} {last_name}"
    else:                                                       #(3)
        full_name = f"{first_name} {last_name}"
        return full_name.title()

    musician = get_formatted_name("jimi", 'hendrix')
    print(musician)

    musician = get_formatted_name('jhon', 'hooker', 'lee')      #(4)
    print(musician)

    #En este ejemplo, el nombre se construye a partir de tres partes posibles. 
    # Debido a que siempre hay un nombre y un apellido, estos parámetros se enumeran primero en la definición de la función. 
    # El segundo nombre es opcional, por lo que aparece en último lugar en la definición y su valor predeterminado es una cadena vacía ➡(1)⬅.
    #
    #En el cuerpo de la función, verificamos si se ha proporcionado un segundo nombre. 
    # Python interpreta las cadenas no vacías como True, por lo que si middle_name se 
    # evalúa como True si un argumento de segundo nombre está en la llamada de función ➡(2)⬅.
    #Si se proporciona un segundo nombre, el nombre, el segundo nombre y el apellido se combinan 
    # para formar un nombre completo. Luego, este nombre se cambia a mayúsculas y minúsculas y se 
    # devuelve a la línea de llamada de función donde se asigna a la variable músico y se imprime. 
    # Si no se proporciona un segundo nombre, la cadena vacía falla la prueba if y el bloque else 
    # ejecuta ➡(3)⬅. El nombre completo se crea con solo un nombre y un apellido, y el nombre 
    # formateado se devuelve a la línea de llamada donde se asigna al músico y se imprime.
    #
    #Llamar a esta función con un nombre y apellido es sencillo. Sin embargo, si usamos un segundo nombre, 
    # debemos asegurarnos de que el segundo nombre sea el último argumento pasado para que Python haga 
    # coincidir los argumentos posicionales correctamente ➡(4)⬅.
    #
    #Esta versión modificada de nuestra función funciona para personas que solo tienen un nombre y 
    # apellido, y también funciona para personas que tienen un segundo nombre:
    #           >>> Jimi Hendrix
    #           >>> Jhon Lee Hooker
    #
    #Los valores opcionales permiten que las funciones manejen una amplia gama de casos de uso 
    # mientras permiten que las llamadas a funciones sean lo más simples posible.













        #`3- Returning a Dictionary

    #Una función puede devolver cualquier tipo de valor que necesite, incluidas estructuras de datos más complicadas 
    # como listas y diccionarios. Por ejemplo, la siguiente función toma partes de un nombre y devuelve un diccionario 
    # que representa a una persona:
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}           #(1)
    return person                                               #(2)

musician = build_person('jimi', 'hendrix')
print(musician)                                                 #(3)

    #La función build_person() toma un nombre y apellido, y coloca estos valores en un diccionario en ➡(1)⬅. 
    # El valor de first_name se almacena con la clave 'first', y el valor de last_name se almacena con la clave 'last'. 
    # El diccionario completo que representa a la persona se devuelve en ➡(2)⬅. 
    # El valor de retorno se imprime en ➡(3)⬅ con las dos piezas originales de información textual ahora almacenadas en un diccionario:
    #
    #           >>> Jimi Hendrix
    #           >>> Jhon Lee Hooker
    #
    #Esta función toma información textual simple y la coloca en una estructura de datos más significativa que 
    # le permite trabajar con la información más allá de simplemente imprimirla. Las cadenas 'jimi' y 'hendrix' 
    # ahora están etiquetadas como nombre y apellido. Puede extender fácilmente esta función para aceptar valores 
    # opcionales como un segundo nombre, una edad, una ocupación o cualquier otra información que desee almacenar 
    # sobre una persona. Por ejemplo, el siguiente cambio también le permite almacenar la edad de una persona:
def vuil_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendix', age=27)
print(musician)

    #Agregamos un nuevo parámetro opcional edad a la definición de la función y asignamos al parámetro el valor especial Ninguno, 
    # que se usa cuando una variable no tiene un valor específico asignado. Puede pensar en Ninguno como un valor de marcador de posición. 
    # En las pruebas condicionales, Ninguno se evalúa como Falso. Si la llamada a la función incluye un valor para la edad, ese valor 
    # se almacena en el diccionario. Esta función siempre almacena el nombre de una persona, pero también se puede modificar para 
    # almacenar cualquier otra información que desee sobre una persona.










        #`4- Using a Funtion with a while Loop

    #Puede usar funciones con todas las estructuras de Python que ha aprendido hasta ahora. 
    # Por ejemplo, usemos la función get_formatted_name() con un ciclo while para saludar a los usuarios de manera más formal. 
    # Aquí hay un primer intento de saludar a las personas usando su nombre y apellido:
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

            #Este es un bucle/loop infinito!!!!
while True:
    print("\nPlease tell me your name:")                            #(1)
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    #Para este ejemplo, usamos una versión simple de get_formatted_name() que no involucra segundos nombres. 
    # El ciclo while le pide al usuario que ingrese su nombre, y le solicitamos su nombre y apellido por separado ➡(1)⬅.

    #Pero hay un problema con este bucle while: 
    # no hemos definido una condición de salida. 
    # ¿Dónde coloca una condición de salida cuando solicita una serie de entradas? 
    # Queremos que el usuario pueda salir lo más fácilmente posible, por lo que cada mensaje debe ofrecer una forma de salir. 
    # La instrucción break ofrece una forma sencilla de salir del ciclo en cualquiera de los dos indicadores:
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

            
while True:
    print("\nPlease tell me your name:")
    prit("(enter 'q' at any time to quit)")

    f_name = input("First name ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    #Agregamos un mensaje que informa al usuario cómo salir y luego salimos del ciclo si el usuario 
    # ingresa el valor de salida en cualquiera de las indicaciones. Ahora el programa continuará 
    # saludando a las personas hasta que alguien ingrese 'q' para cualquiera de los nombres:
    #
    #           >>> Please tell me your name: 
    #           >>> (enter 'q' at any time to quit) 
    #           >>> First name: eric
    #           >>> Last name: matthes
    #
    #           >>> Hello, Eric Matthes!
    #
    #           >>> Please tell me your name: 
    #           >>> (enter 'q' at any time to quit) 
    #           >>> First name: q























                    #   🦚 Passing a List

    #
    #A menudo le resultará útil pasar una lista a una función, ya sea una lista de nombres, números u objetos más complejos, como diccionarios. 
    # Cuando pasa una lista a una función, la función obtiene acceso directo al contenido de la lista.
    #  Usemos funciones para que trabajar con listas sea más eficiente.
    #
    #Digamos que tenemos una lista de usuarios y queremos imprimir un saludo para cada uno. 
    # El siguiente ejemplo envía una lista de nombres a una función llamada greeting_users(), 
    # que saluda a cada persona en la lista individualmente:
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']          #(1)
greet_users(usernames)

    #Definimos greeting_users() para que espere una lista de nombres, que asigna a los nombres de los parámetros. 
    # La función recorre la lista que recibe e imprime un saludo para cada usuario. 
    # En ➡(1)⬅ definimos una lista de usuarios y luego pasamos la lista de nombres de usuario 
    # para saludar a los usuarios() en nuestra llamada de función:
    #
    #           >>> Hello, Hannah!
    #           >>> Hello, Ty!
    #           >>> Hello, Margot!
    #
    #Esta es la salida que queríamos. 
    # Cada usuario ve un saludo personalizado y puede llamar a la función 
    # en cualquier momento que desee saludar a un grupo específico de usuarios.















        #`1- Modifying a List in a Function

    #Cuando pasa una lista a una función, la función puede modificar la lista. Cualquier cambio realizado 
    # en la lista dentro del cuerpo de la función es permanente, lo que le permite trabajar de manera 
    # eficiente incluso cuando se trata de grandes cantidades de datos.

    #Considere una empresa que crea modelos impresos en 3D de los diseños que envían los usuarios. 
    # Los diseños que deben imprimirse se almacenan en una lista y, después de imprimirse, se mueven 
    # a una lista separada. El siguiente código hace esto sin usar funciones:

#start with some designs that need o be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left.
# move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

#Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

    #Este programa comienza con una lista de diseños que deben imprimirse y una lista vacía llamada complete_models 
    # a la que se moverá cada diseño después de que se haya impreso. Siempre que los diseños permanezcan en unprinted_designs, 
    # el bucle while simula la impresión de cada diseño eliminando un diseño del final de la lista, almacenándolo en 
    # current_design y mostrando un mensaje de que se está imprimiendo el diseño actual. Luego agrega el diseño a la 
    # lista de modelos completos. Cuando el bucle termina de ejecutarse, se muestra una lista de los diseños que se han impreso.
    #
    #
    #Podemos reorganizar este código escribiendo dos funciones, cada una de las cuales hace un trabajo específico. 
    # La mayor parte del código no cambiará; simplemente lo estamos estructurando con más cuidado. 
    # La primera función se encargará de imprimir los diseños, y la segunda resumirá las impresiones que se han realizado:

def print_models(unprinted_designs, completed_models):          #(1)
    """
    Simulate printing each design, until non are left.
    Move each desing to completed_models afer printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):                    #(2)
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

    #At ➡(1)⬅ we define the function print_models() with two parameters: 
    # a list of designs that need to be printed and a list of completed models. 
    # Given these two lists, the function simulates printing each design by emptying 
    # the list of unprinted designs and filling up the list of completed models. 
    # At ➡(2)⬅ we define the function show completed models() with one parameter: 
    # the list of completed models. Given this list, show_completed_models() displays the name of each model that was printed.
    #
    #This program has the same output as the version without functions, but the code is much more organized. 
    # The code that does most of the work has been moved to two separate functions, which makes the main part 
    # of the program easier to understand. Look at the body of the program to see how much easier it is to 
    # understand what this program is doing:
    #
    #           >>> unprinted designs ['phone case', 'robot pendant', 'dodecahedron'] 
    #           >>> completed models []
    #           >>> 
    #           >>> print_models (unprinted designs, completed_models) 
    #           >>> show_completed models (completed_models)
    #
    #Configuramos una lista de diseños sin imprimir y una lista vacía que contendrá los modelos Completados.
    # Entonces, como ya hemos definido nuestras dos funciones, todo lo que tenemos que hacer es llamarlas y pasarles los argumentos correctos.
    # Llamamos modelos de impresión) y le pasamos las dos listas que necesita; Como era de esperar, print_models() mula la impresión de los diseños.
    # Luego llamamos a mostrar modelos completos () y le pasamos la lista de modelos completos para que pueda informar los modelos que se han impreso.
    # Los nombres de funciones descriptivos permiten que otros lean este código y lo entiendan, incluso sin comentarios.
    #
    #Este programa es más fácil de ampliar y mantener que la versión sin funciones.
    # Si necesitamos imprimir más diseños más adelante, simplemente podemos volver a llamar a print models().
    # Si nos damos cuenta de que el código de impresión debe modificarse, podemos cambiar el código una vez, y
    # nuestros cambios tendrán lugar en todas partes donde se llame a la función.
    # Esta técnica es más eficiente que tener que actualizar el código por separado en varios lugares del programa.
    #
    #Este ejemplo también demuestra la idea de que cada función debe tener un trabajo específico.
    # La primera función imprime cada diseño y la segunda muestra los modelos completos.
    # Esto es más beneficioso que usar una función para hacer ambos trabajos.
    # Si está escribiendo una función y nota que la función está haciendo demasiadas tareas diferentes,
    # intenta dividir el código en dos funciones.
    # Recuerde que siempre puede llamar a una función desde otra función, lo que puede ser útil
    # al dividir una tarea compleja en una serie de pasos.













        #`2- Preventing a Function from Modifying a List

    #A veces querrá evitar que una función modifique una lista. 
    # Por ejemplo, suponga que comienza con una lista de diseños sin imprimir y escribe una función para 
    # moverlos a una lista de modelos completos, como en el ejemplo anterior. 
    # Puede decidir que, aunque haya impreso todos los diseños, desea conservar la lista original de diseños no impresos para sus registros.
    #
    #Pero debido a que movió todos los nombres de diseño fuera de unprinted_designs, la lista 
    # ahora está vacía y la lista vacía es la única versión que tiene; el original ha desaparecido. 
    # En este caso, puede solucionar este problema pasando a la función una copia de la lista, no el original. 
    # Cualquier cambio que la función haga en la lista afectará solo a la copia, dejando intacta la lista original.
    #
    #Puede enviar una copia de una lista a una función como esta:
function_name(list_name[:])
    #The slice notation [:] makes a copy of the list to send to the function. 
    # If we didn't want to empty the list of unprinted designs in printing_models.py we could call print_models () like this:
print_models(unprinted_designs[:], completed_models)
    #La función print_models() puede hacer su trabajo porque todavía recibe los nombres de todos los diseños no impresos. 
    # Pero esta vez usa una copia de la lista original de diseños no impresos, no la lista actual de diseños no impresos. 
    # La lista de modelos completados se llenará con los nombres de los modelos impresos como antes, pero la lista original
    #  de diseños no impresos no se verá afectada por la función.

    #Aunque puede conservar el contenido de una lista pasando una copia a sus funciones, debe pasar la lista original 
    # a funciones a menos que tenga una razón específica para pasar una copia. Es más eficiente que una función trabaje 
    # con una lista existente para evitar usar el tiempo y la memoria necesarios para hacer una copia separada, 
    # especialmente cuando trabaja con listas grandes.














                # 🦚    Passing an Arbitarary Number of Arguments
        
    #A veces, no sabrá de antemano cuántos argumentos debe aceptar una función.
    # Afortunadamente, Python permite que una función recopile un número arbitrario de argumentos de la declaración de llamada.
    #
    #Por ejemplo, considere una función que construye una pizza. 
    # Necesita aceptar una cantidad de ingredientes, pero no se puede saber de antemano cuántos ingredientes querrá una persona. 
    # La función del siguiente ejemplo tiene un parámetro, *toppings, pero este parámetro 
    # recopila tantos argumentos como proporciona la línea de llamada:

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

    make_pizza('pepperoni')
    make('mushrooms', 'green peppers', 'extra cheese')

    #El asterisco en el nombre del parámetro "toppings" le dice a Python que cree una tupla vacía llamada toppings
    # y empaquete cualquier valor que reciba en esta tupla. 
    # La llamada print() en el cuerpo de la función produce un resultado que muestra que Python puede manejar 
    # una llamada de función con un valor y una llamada con tres valores. Trata las diferentes llamadas de manera similar. 
    # Tenga en cuenta que Python empaqueta los argumentos en una tupla, incluso si la función recibe solo un valor:
    #
    #           >>> ('pepperoni',)
    #           >>> ('mushrooms', 'green peppers', 'extra cheese')
    #
    #Ahora podemos reemplazar la llamada print() con un bucle que recorre la lista de ingredientes y describe la pizza que se pide:

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the follolwing toppings:")
    for topping in toppings:
        print(f"- {toppings}")

    make_pizza('pepperoni')
    make('mushrooms', 'green peppers', 'extra cheese')

    #La función responde apropiadamente, ya sea que reciba un valor o tres valores:
    #
    #           >>> Making a pizza with the following toppings:
    #           >>> - pepperoni
    #
    #           >>> Making a pizza with the following toppings:
    #           >>> - mushrooms
    #           >>> - green peppers=
    #           >>> - extra cheese
    #
    #Esta sintaxis funciona sin importar cuántos argumentos reciba la función.
















        #`1- Mixing Positional and Arbitrary Arguments

    #Si desea que una función acepte varios tipos diferentes de argumentos, el parámetro que acepta un número 
    # arbitrario de argumentos debe colocarse en último lugar en la definición de la función. 
    # Python primero hace coincidir los argumentos posicionales y de palabras clave y luego recopila los 
    # argumentos restantes en el parámetro final.

    #Por ejemplo, si la función necesita tomar un tamaño para la pizza, ese parámetro debe estar antes del parámetro *toppings:
def make_pizza(size, *toppings):
    """ Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {toppings}")

make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    #En la definición de la función, Python asigna el primer valor que recibe al tamaño del parámetro. 
    # Todos los demás valores que vienen después se almacenan en la tupla the toppings. 
    # Las llamadas de función incluyen un argumento para el tamaño primero, seguido de tantos ingredientes como sea necesario.
    #
    #Ahora cada pizza tiene un tamaño y una cantidad de ingredientes, y cada información se 
    # imprime en el lugar adecuado, mostrando el tamaño primero y los ingredientes después:
    #
    #           >>> Making a 16-inch pizza with the following toppings: - pepperoni
    #
    #           >>> Making a 12-inch pizza with the following toppings:
    #           >>> - mushrooms
    #           >>> - green peppers
    #           >>> - extra cheese
    #NOTE: A menudo verá el nombre de parámetro genérico *args, que recopila argumentos posicionales arbitrarios como este.

















        #`2- Using Arbitrary Keyword Arguments
    
    #A veces querrá aceptar un número arbitrario de argumentos, pero no sabrá de antemano qué tipo de información se pasará a la función. 
    # En este caso, puede escribir funciones que acepten tantos pares clave-valor como proporcione la declaración de llamada. 
    # Un ejemplo implica la creación de perfiles de uso: sabe que obtendrá información sobre un usuario, pero no está seguro de qué tipo de información recibirá. 
    # La función build profile() en el siguiente ejemplo siempre toma un nombre y apellido, pero también acepta un número arbitrario de argumentos de palabras clave:
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    














                # 🦚    Passing an Arbitrary Number of Arguments

    # A veces no sabrá de antemano cuántos argumentos debe aceptar una función. 
    # Afortunadamente, Python permite que una función recopile un número arbitrario de argumentos de la declaración de llamada.

    #Por ejemplo, considere una función que construye una pizza. 
    # Necesita aceptar una cantidad de ingredientes, pero no se puede saber de antemano cuántos ingredientes querrá una persona. 
    # La función del siguiente ejemplo tiene el parámetro *toppings, pero este parámetro recopila tantos argumentos como proporciona la línea de llamada:

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')