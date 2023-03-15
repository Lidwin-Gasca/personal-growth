


#                               CHAPTER      9





#                  🎭 C L A S S E S






#La programación orientada a objetos es uno de los enfoques más efectivos para escribir software. En la programación orientada a objetos, 
#escribes clases que representan cosas y situaciones del mundo real, y creas objetos basados ​​en estas clases. Cuando escribes una clase, 
#defines el comportamiento general que puede tener toda una categoría de objetos.
#
#Cuando crea objetos individuales de la clase, cada objeto se equipa automáticamente con el comportamiento general; 
#luego puede darle a cada objeto las características únicas que desee. Se sorprenderá de lo bien que se pueden modelar 
#situaciones del mundo real con la programación orientada a objetos.
#
#Crear un objeto a partir de una clase se denomina creación de instancias y se trabaja con instancias de una clase. 
#En este capítulo, escribirá clases y creará instancias de esas clases. Especificará el tipo de información que se puede 
#almacenar en las instancias y definirá las acciones que se pueden realizar con estas instancias. También escribirá clases 
#que amplíen la funcionalidad de las clases existentes, de modo que clases similares puedan compartir código de manera eficiente. 
#Almacenará sus clases en módulos e importará clases escritas por otros programadores en sus propios archivos de programa.
#
#Comprender la programación orientada a objetos te ayudará a ver el mundo como lo hace un programador. 
#Lo ayudará a conocer realmente su código, no solo lo que sucede línea por línea, sino también los conceptos más importantes detrás de él. 
#Conocer la lógica detrás de las clases lo entrenará para pensar lógicamente para que pueda escribir 
#programas que aborden de manera efectiva casi cualquier problema que encuentre.
#
#Las clases también te facilitan la vida a ti y a los demás programadores con los que trabajarás a medida que 
#te enfrentas a desafíos cada vez más complejos. Cuando usted y otros programadores escriban código basado en 
#el mismo tipo de lógica, podrán entender el trabajo de los demás. Sus programas tendrán sentido para muchos 
#colaboradores, lo que permitirá que todos logren más.















            #🦚           Creating and Using a Class

    #Puedes modelar casi cualquier cosa usando clases. Comencemos por escribir una clase simple, Perro, que represente un perro,
    #no un perro en particular, sino cualquier perro. ¿Qué sabemos sobre la mayoría de los perros domésticos? Bueno, todos tienen 
    #un nombre y una edad. También sabemos que la mayoría de los perros se sientan y dan vueltas. 
    #Esas dos piezas de información (nombre y edad) y esos dos comportamientos (sentarse y darse la vuelta) irán en nuestra clase 
    #de perros porque son comunes a la mayoría de los perros. Esta clase le dirá a Python cómo hacer un objeto que represente a un perro. 
    #Después de escribir nuestra clase, la usaremos para crear instancias individuales, cada una de las cuales representa un perro específico.











    


            #`1- Creating the Dog Class

    # Cada instancia creada a partir de la clase Perro almacenará un nombre y una edad, 
    #y le daremos a cada perro la capacidad de sentarse() y darse la vuelta():

class Dog:                                           		    #(1)
    """A simple attempt to model a dog"""             		    #(2)

    def __init__(self, name, age):                    		    #(3)
        """Initialize name and ahe attributes."""
        self.name = name									    #(4)
        self.age = age

    def sit(self):												#(5)
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """"Sumulate rolling over in respone to a command."""
        print(f"{self.name} rolled over!")

    #Hay mucho que notar aquí, pero no te preocupes. 
    # Verá esta estructura a lo largo de este capítulo y tendrá mucho tiempo para acostumbrarse a ella. 
    # En ➡(1)⬅ definimos una clase llamada Perro. Por convención, los nombres en mayúsculas se refieren a clases en Python. 
    # No hay paréntesis en la definición de la clase porque estamos creando esta clase desde cero. 
    # En ➡(2)⬅ escribimos una cadena de documentación que describe lo que hace esta clase.


    #   --- The__init__() Method: ---

    #Una función que es parte de una clase es un método. 
    # Todo lo que aprendió sobre las funciones también se aplica a los métodos; 
    # la única diferencia práctica por ahora es la forma en que llamaremos a los métodos. 
    # El método __init__() en ➡(3)⬅ es un método especial que Python ejecuta automáticamente 
    # cada vez que creamos una nueva instancia basada en la clase Perro. 
    # Este método tiene dos guiones bajos iniciales y dos guiones bajos finales, 
    # una convención que ayuda a evitar que los nombres de métodos predeterminados 
    # de Python entren en conflicto con los nombres de sus métodos. 
    # Asegúrese de usar dos guiones bajos a cada lado de __init__(). 
    # Si usa solo uno en cada lado, el método no se llamará automáticamente cuando use su clase, 
    # lo que puede generar errores que son difíciles de identificar.
    #
    #   Definimos el método the_init_() para que tenga tres parámetros: self, name y age. 
    # El parámetro self es obligatorio en la definición del método y debe aparecer antes que los demás parámetros. 
    # Debe incluirse en la definición porque cuando Python llame a este método más adelante (para crear una instancia de Dog), 
    # la llamada al método pasará automáticamente el argumento self. 
    # Cada llamada de método asociada con una instancia pasa automáticamente a self, 
    # que es una referencia a la instancia misma; le da a la instancia individual acceso a los atributos y métodos de la clase. 
    # Cuando creamos una instancia de Dog, Python llamará al método _init_() de la clase Dog. 
    # Le pasaremos a Dog() un nombre y una edad como argumentos; self se pasa automáticamente, por lo que no necesitamos pasarlo. 
    # Siempre que queramos crear una instancia de la clase Perro, proporcionaremos valores solo para los dos últimos parámetros, 
    # nombre y edad.
    #
    #   Las dos variables definidas en ➡(4)⬅ tienen cada una el prefijo self. 
    # Cualquier variable con el prefijo self está disponible para todos los métodos de la clase, 
    # y también podremos acceder a estas variables a través de cualquier instancia creada a partir de la clase. 
    # La línea self.name = name toma el valor asociado con el nombre del parámetro y lo asigna al nombre de la variable, 
    # que luego se adjunta a la instancia que se está creando. El mismo proceso ocurre con self.age age. 
    # Las variables a las que se puede acceder a través de instancias como esta se denominan atributos.
    #
    #   La clase Dog tiene otros dos métodos definidos: sit() y roll over() ➡(5)⬅. 
    # Debido a que estos métodos no necesitan información adicional para ejecutarse, 
    # solo los definimos para que tengan un parámetro, self. 
    # Las instancias que creemos más tarde tendrán acceso a estos métodos. 
    # En otras palabras, podrán sentarse y darse la vuelta. 
    # Por ahora, sit() y roll over() no hacen mucho. 
    # Simplemente imprimen un mensaje que dice que el perro está sentado o volteándose. 
    #   Pero el concepto se puede extender a situaciones realistas: 
    # si esta clase fuera parte de un juego de computadora real, estos métodos contendrían un código 
    # para hacer que un perro animado se siente y se dé la vuelta. Si esta clase se escribió para controlar un robot, 
    # estos métodos dirigirían los movimientos que hacen que un perro robótico se siente y se dé la vuelta.


























            #`2- Making an Instance from a class

    #Piense en una clase como un conjunto de instrucciones sobre cómo crear una instancia.
    #  La clase Dog es un conjunto de instrucciones que le dice a Python cómo crear instancias 
    # individuales que representen perros específicos.
    #
    #   Hagamos una instancia que represente a un perro específico:
class Dog:
    """Supón que aquí esta todo el codigo de hasta ayá 👆 arriba"""

my_dog = Dog('Willie', 6)                   #(1)
                                            
print(f"My dog's name is {my_dog.name}.")   #(2)
print(f"My dog is {my_dog.age} years old.") #(3)

    # La clase Dog que estamos usando aquí es la que acabamos de escribir en el ejemplo anterior. 
    # En ➡(1)⬅ le decimos a Python que cree un perro cuyo nombre sea 'Willie' y cuya edad sea 6. 
    # Cuando Python lee esta línea, llama al método __init__() en Dog con los argumentos 'Willie' y 6. 
    # El El método __init__() crea una instancia que representa a este perro en particular y establece 
    # los atributos de nombre y edad usando los valores que proporcionamos. 
    # Python luego devuelve una instancia que representa a este perro. 
    # Asignamos esa instancia a la variable mi_perro. 
    # La convención de nomenclatura es útil aquí:
    # generalmente podemos asumir que un nombre en mayúsculas como Dog se refiere a una clase, 
    # y un nombre en minúsculas como my_dog se refiere a una única instancia creada a partir de una clase.


    #   --- Accessing Atributes ---

    #Para acceder a los atributos de una instancia, utiliza la notación de puntos. 
    # En ➡(2)⬅accedemos al valor del nombre del atributo de mi perro escribiendo:
my_dog.name
    #La notación de puntos se usa a menudo en Python. 
    # Esta sintaxis demuestra cómo Python encuentra el valor de un atributo. 
    # Aquí, Python mira la instancia mi_perro y luego encuentra el nombre del atributo asociado con mi perro. 
    # Este es el mismo atributo al que se hace referencia como self.name en la clase Dog. 
    # En ➡(3)⬅utilizamos el mismo enfoque para trabajar con el atributo edad.
    #   El resultado es un resumen de lo que sabemos sobre my_dog:
    #
    #           >>> My dog's name is Willie.
    #           >>> My dog is 6 years old.
    #


    #   --- Calling Methods ---

    #Después de crear una instancia de la clase Dog, podemos usar la notación 
    # de puntos para llamar a cualquier método definido en Dog. 
    # Hagamos que nuestro perro se siente y se dé la vuelta:
class Dog:
    """Imaginemonos que aquí esta el codigo de la 'clase' arriba en el primer tema"""
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

    #Para llamar a un método, proporcione el nombre de la instancia (en este caso, mi_perro) y el método al que desea llamar,
    #  separados por un punto. Cuando Python lee my_dog.sit(), busca el método sit() en la clase Dog y ejecuta ese código. 
    # Python interpreta la línea my_dog.roll_over() de la misma manera.
    #   Ahora Willie hace lo que le decimos:
    #
    #           >>> Willie is now sitting.
    #           >>> willlie rolled over!
    #
    #Esta sintaxis es bastante útil. Cuando a los atributos y métodos se les ha dado nombres descriptivos apropiados como nombre, edad, sit(),
    # y roll_over(), podemos inferir fácilmente lo que se supone que debe hacer un bloque de código, incluso uno que nunca hayamos visto antes.


    #   --- Creating Multiple Instances ---

    #Puede crear tantas instancias de una clase como necesite. Vamos a crear un segundo perro llamado tu_perro:
class Dog:
    """Imaginemonos que aquí esta el codigo de la 'clase' arriba en el primer tema"""
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"your dog is {your_dog.age} years old.")
your_dog.sit()

#En este ejemplo, creamos un perro llamado Willie y un perro llamado Lucy. 
# Cada perro es una instancia separada con su propio conjunto de atributos, 
# capaz de realizar el mismo conjunto de acciones.
#
#Incluso si usamos el mismo nombre y edad para el segundo perro. 
# Python aún crearía una instancia separada de la clase Dog. 
# Puede crear tantas instancias de una clase como necesite, siempre que asigne a 
# cada instancia un nombre de variable único o que ocupe un lugar único en una lista o diccionario.



































                        #🦚           Working with Clases and Instances

    #Puede usar clases para representar muchas situaciones del mundo real. Una vez que escriba una clase, 
    # pasará la mayor parte de su tiempo trabajando con instancias creadas a partir de esa clase. 
    # Una de las primeras tareas que querrá hacer es modificar los atributos asociados con una instancia en particular. 
    # Puede modificar los atributos de una instancia directamente o escribir métodos que actualicen los atributos de formas específicas.
    











            #`1- The Car Class

    #Escribamos una nueva clase que represente un automóvil. 
    # Nuestra clase almacenará información sobre el tipo de automóvil con el 
    # que estamos trabajando y tendrá un método que resuma esta información:
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):                  #(1)
        """Initialize attrivutes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):                         #(2)
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2019)                        #(3)
print(my_new_car.get_descriptive_name())
    #En ➡(1)⬅ en la clase Car, primero definimos el método _init_() con el parámetro self, tal como lo hicimos antes con nuestra clase Dog. 
    # También le damos otros tres parámetros: marca, modelo y año. 
    # El método _init_() toma estos parámetros y los asigna a los atributos que se asociarán con las instancias creadas a partir de esta clase. 
    # Cuando creamos una nueva instancia de Car, necesitaremos especificar una marca, modelo y año para nuestra instancia.
    #
    #En ➡(2)⬅ definimos un método llamado get_descriptive_name() que pone el año, la marca y el modelo de un automóvil en 
    # una cadena que describe claramente el automóvil. Esto nos evitará tener que imprimir el valor de cada atributo individualmente. 
    # Para trabajar con los valores de los atributos en este método, usamos self.make, self.model y self.year.
    #
    # En ➡(3)⬅ creamos una instancia de la clase Car y la asignamos a la variable my new car. 
    # Luego llamamos a get_descriptive_name() para mostrar qué tipo de automóvil tenemos:
    #
    #           >>> 2019 Audi A4
    #
    #Para hacer la clase más interesante, agreguemos un atributo que cambie con el tiempo. 
    # Agregaremos un atributo que almacene el kilometraje total del automóvil.




            #`2- Setting a Default Value for an Attribute

    #Cuando se crea una instancia, los atributos se pueden definir sin pasarlos como parámetros. 
    # Estos atributos se pueden definir en el método __init__(), donde se les asigna un valor predeterminado.

    #Agreguemos un atributo llamado lectura del odómetro que siempre comienza con un valor de 0. 
    # También agregaremos un método read_odometer() que nos ayuda a leer el odómetro de cada automóvil:

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)                        #(3)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()