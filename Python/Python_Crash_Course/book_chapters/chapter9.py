


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
        self.odometer_reading = 0                                   #(1)

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):                                        #(2)
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)                        
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

    #Esta vez, cuando Python llama al método __init__() para crear una nueva instancia, 
    # almacena los valores de marca, modelo y año como atributos, como lo hizo en el ejemplo anterior. 
    # Luego, Python crea un nuevo atributo llamado lectura del odómetro y establece su valor inicial en 0 ➡(1)⬅. 
    # También tenemos un nuevo método llamado read_odometer() en ➡(2)⬅ que facilita la lectura del kilometraje de un automóvil.
    #
    #Nuestro coche arranca con un kilometraje de 0:
    #
    #           >>> 2019 Audi A4
    #           >>> This car has 0 miles on it.
    #
    #No se venden muchos autos con exactamente 0 millas en el odómetro, 
    #por lo que necesitamos una forma de cambiar el valor de este atributo.




















                #🦚           Modifying Attribute Values

    #Puede cambiar el valor de un atributo de tres maneras: puede cambiar el valor directamente a través de una instancia, 
    # establecer el valor a través de un método o incrementar el valor (agregarle una cierta cantidad) a través de un método. 
    # Veamos cada uno de estos enfoques.











            #`1- Modifying an Attribute's Value Directly
    
    #The simplest way to modify the value of an attribute is to access the attribute directly through an instance. 
    # Here we set the odometer reading to 23 directly:

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

my_new_car = Car('audi', 'a4', 2019)                        
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23    #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅ #(1)
my_new_car.read_odometer()          #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅

    #En ➡(1)⬅ usamos la notación de puntos para acceder al atributo odometer_reading del automóvil y establecer su valor directamente.
    # Esta línea le dice a Python que tome la instancia my_new_car, encuentre el atributo de odometer_reading asociado con él,
    # y establezca el valor de ese atributo en 23:
    #
    #           >>> 2019 Audi A4
    #           >>> This car has 23 miles on it.
    #
    #A veces querrás acceder a los atributos directamente como este, pero otras veces querrás escribir un método que actualice el valor por ti.

















            #`2-    Modifying an Attribute's Value Through a Method

    #Puede ser útil tener métodos que actualicen ciertos atributos por usted. 
    # En lugar de acceder al atributo directamente, pasa el nuevo valor a un método que maneja la actualización internamente. 
    # Aquí hay un ejemplo que muestra un método llamado update_odometer():

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

    def update_odometer(self, mileage):                             #⬅  #(1)
        """Set the odometer reading in to the given value."""       #⬅
        self.odometer_reading = mileage                             #⬅

my_new_car = Car('audi', 'a4', 2019)                        
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(23)                                       #⬅ #(2)
my_new_car.read_odometer()

    #La única modificación a Car es la adición de update odometer() en ➡(1)⬅. 
    # Este método toma un valor de kilometraje y lo asigna a la self.odometer_reading.
    #  En ➡(2)⬅ llamamos a update_odometer() y le damos 23 como argumento (correspondiente al parámetro de kilometraje en la definición del método). 
    # Establece read_odometer en 23, y read odometer() imprime la lectura/reading:
    #
    #           >>> 2019 Audi A4
    #           >>> This car has 23 miles on it.
    #
    #Podemos extender el método update_odometer() para hacer un trabajo adicional cada vez que se modifica la lectura del odómetro. 
    # Agreguemos un poco de lógica para asegurarnos de que nadie intente hacer retroceder la lectura del odómetro:

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

    def update_odometer(self, mileage):                                 #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅       
        """
        Set the odometer reading to the giving value.
        Reject the chang if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:                            #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅    #(1)
            self.odometer_reading = mileage                             #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅
        else:                                                           #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅    #(2)
            print("You can't roll back an odometer!")                   #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅

    #Ahora actualizar el odómetro() verifica que la nueva lectura tenga sentido antes de modificar el atributo. 
    # Si el nuevo kilometraje, el kilometraje, es mayor o igual que el kilometraje existente, la lectura del self.odometer, 
    # puede actualizar la lectura del odómetro al nuevo kilometraje ➡(1)⬅. 
    # Si el nuevo kilometraje es menor que el kilometraje existente, recibirá una advertencia de que 
    # no puede retroceder un odómetro que incremente el valor de un atributo a través de un método ➡(2)⬅.



























            #`3- Incrementing an Attribute's Value Through a Method

    #A veces querrá incrementar el valor de un atributo en cierta cantidad en lugar de establecer un valor completamente nuevo.
    # Digamos que compramos un automóvil usado y acumulamos 100 millas entre el momento en que lo compramos y el momento en que lo registramos. 
    # Aquí hay un método que nos permite pasar esta cantidad incremental y agregar ese valor a la lectura del odómetro:
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

    def update_odometer(self, mileage):                                      
        """
        Set the odometer reading to the giving value.
        Reject the chang if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:                            
            self.odometer_reading = mileage                             
        else:                                                          
            print("You can't roll back an odometer!")

            #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇codigo nuevo⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
    def increment_odometer(self, miles):                                        #(1)
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
my_used_car = Car('subaru', 'outback', 2015)                                    #(2)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)                                             #(3)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)                                             #(4)
my_used_car.read_odometer()

    # El nuevo método de incremento del odómetro() en ➡(1)⬅ toma un número de millas y agrega este valor a la lectura de self.odometer. 
    # En ➡(2)⬅ creamos un auto usado, my_used_car. 
    # Establecemos su cuentakilómetros en 23 500 llamando a update_odometer() y pasándole 23 500 en ➡(3)⬅. 
    # En ➡(4)⬅ llamamos a increment odometer() y le pasamos 100 para sumar las 100 millas que recorrimos entre comprar el auto y registrarlo:
    #
    #           >>> 2015 Subaru Outback
    #           >>> This car has 23500 miles on it.
    #           >>> This car has 23600 miles on it.
    #
    #Puede modificar fácilmente este método para rechazar incrementos negativos para que nadie use esta función para retroceder un odómetro.


    #NOTE: 
    #Puede usar métodos como este para controlar cómo los usuarios de su programa 
    # actualizan valores como la lectura del odómetro, pero cualquier persona con 
    # acceso al programa puede establecer la lectura del odómetro en cualquier 
    # valor accediendo directamente al atributo. 
    # La seguridad eficaz exige una atención extrema a los detalles además de las 
    # comprobaciones básicas como las que se muestran aquí.




















                #🦚           Inheritance / Herencia

    #No siempre tienes que empezar desde cero al escribir una clase. 
    # Si la clase que está escribiendo es una versión especializada de otra clase que escribió, puede usar la herencia. 
    # Cuando una clase hereda de otra, toma los atributos y métodos de la primera clase. 
    # La clase original se llama clase padre y la nueva clase es la clase hija. 
    # La clase secundaria puede heredar cualquiera o todos los atributos y métodos de su clase principal, 
    # pero también es libre de definir sus propios atributos y métodos nuevos.
    



            #`1- The  __init__()Method for a Child Class
        #Cuando está escribiendo una nueva clase basada en una clase existente, a menudo querrá llamar al método __init__() desde la clase principal. 
        # Esto inicializará todos los atributos que se definieron en el método parent_init_() y los hará disponibles en la clase secundaria.

        #Como ejemplo, modelemos un coche eléctrico. Un automóvil eléctrico es solo un tipo específico de automóvil, 
        # por lo que podemos basar nuestra nueva clase "ElectricCar" en la clase "Car" que escribimos anteriormente. 
        # Entonces solo tendremos que escribir código para los atributos y el comportamiento específico de los autos eléctricos.

    # Comencemos por hacer una versión simple de la clase ElectricCar, que hace todo lo que hace la clase Car:
class Car:  #(1)
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

    def update_odometer(self, mileage):                                      
        """
        Set the odometer reading to the giving value.
        Reject the chang if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:                            
            self.odometer_reading = mileage                             
        else:                                                          
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


            #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇codigo nuevo⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
class ElectricCar(Car):                                                 #(2)
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):                              #(3)
        """Initialize attributes of parent class"""
        super().__init__(make, model, year)                             #(4)

my_tesla = ElectricCar('tesla', 'model s', 2019)                        #(5)
print(my_tesla.get_descriptive_name())

    #En ➡(1)⬅ comenzamos con Car. 
    # Cuando crea una clase secundaria, la clase principal debe ser parte del archivo actual y debe aparecer antes que la clase secundaria en el archivo. 
    # En ➡(2)⬅ definimos la clase secundaria, ElectricCar. 
    # El nombre de la clase principal debe incluirse entre paréntesis en la definición de una clase secundaria. 
    # El método __init__() en ➡(3)⬅ toma la información necesaria para crear una instancia de Car.
    #
    #La función super() en ➡(4)⬅ es una función especial que le permite llamar a un método de la clase principal. 
    # Esta línea le dice a Python que llame al método __init__() desde Car, lo que le da a una instancia de ElectricCar todos los atributos definidos en ese método. 
    # El nombre super proviene de una convención de llamar a la clase principal una superclase y a la clase secundaria una subclase.
    #
    #Probamos si la herencia funciona correctamente al intentar crear un automóvil eléctrico con el mismo tipo de información que proporcionaríamos al 
    # fabricar un automóvil normal. En ➡(5)⬅creamos una instancia de la clase ElectricCar y la asignamos a mi tesla. 
    # Esta línea llama al método __init__() definido en ElectricCar, que a su vez le dice a Python que llame al método _init_() definido en la clase padre Car. 
    # Proporcionamos los argumentos 'tesla', 'model s' y 2019.
    #
    #Aparte de_init_(), todavía no hay atributos o métodos que sean particulares de un automóvil eléctrico. 
    # En este punto, solo nos estamos asegurando de que el automóvil eléctrico tenga los comportamientos de automóvil apropiados:
    #
    #           >>> 2019 Tesla Model s
    # La instancia de ElectricCar funciona como una instancia de Car, por lo que ahora 
    # podemos comenzar a definir atributos y métodos específicos para autos eléctricos.















            #`2- Defining Attributes and Methods for the Child Class

        #Una vez que tenga una clase secundaria que herede de una clase principal, puede agregar los 
        # nuevos atributos y métodos necesarios para diferenciar la clase secundaria de la clase principal.

#Agreguemos un atributo que sea específico para los autos eléctricos (una batería, por ejemplo) y un método para informar sobre este atributo. 
# Guardaremos el tamaño de la batería y escribiremos un método que imprima una descripción de la batería:
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

    def update_odometer(self, mileage):                                      
        """
        Set the odometer reading to the giving value.
        Reject the chang if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:                            
            self.odometer_reading = mileage                             
        else:                                                          
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75          #⬅⬅⬅⬅⬅⬅codigo nuevo (1)

    def describe_battery(self):         #⬅⬅⬅⬅⬅⬅codigo nuevo (2)
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

    #En ➡(1)⬅ agregamos un nuevo atributo self.battery_size y establecemos su valor inicial en, por ejemplo, 75. 
    # Este atributo se asociará con todas las instancias creadas a partir de la clase ElectricCar pero no se asociará con ninguna instancia de Car. 
    # También agregamos un método llamado describe_battery() que imprime información sobre la batería en ➡(2)⬅. 
    # Cuando llamamos a este método, obtenemos una descripción que es claramente específica de un coche eléctrico:
    #
    #           >>> 2019 Tesla Model S
    #           >>> This car has a 75-kwh battery.
    #
    #No hay límite en cuánto puede especializarse en la clase ElectricCar. 
    # Puede agregar tantos atributos y métodos como necesite para modelar un automóvil eléctrico con el grado de precisión que necesite. 
    # Un atributo o método que podría pertenecer a cualquier automóvil, en lugar de uno que sea específico de un automóvil eléctrico, 
    # debe agregarse a la clase Car en lugar de a la clase ElectricCar. 
    # Entonces, cualquiera que use la clase Car también tendrá esa funcionalidad disponible, 
    # y la clase ElectricCar solo contendrá el código para la información y el comportamiento específico de los vehículos eléctricos.














            #`3- Overriding Methods from the Parent Class

        #Puede anular cualquier método de la clase principal que no se ajuste a lo que intenta modelar con la clase secundaria. 
        # Para hacer esto, defina un método en la clase secundaria con el mismo nombre que el método que desea anular en la clase principal. 
        # Python ignorará el método de la clase principal y solo prestará atención al método que defina en la clase secundaria.

#Digamos que la clase Car tenía un método llamado fill_gas_tank(). 
# Este método no tiene sentido para un vehículo totalmente eléctrico, 
# por lo que es posible que desee anular este método. Aquí hay una forma de hacerlo:
class ElectricCar(Car):
    #--Codigo Recortado--
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas thank")
#Ahora, si alguien intenta llamar a fill_gas_tank() con un automóvil eléctrico, 
# Python ignorará el método fill_gas_tank() en Car y ejecutará este código en su lugar. 
# Cuando usa la herencia, puede hacer que sus clases secundarias conserven 
# lo que necesita y anule todo lo que no necesite de la clase principal.















            #`4- Instances as Attributes

        #Al modelar algo del mundo real en código, es posible que descubra que está agregando más y más detalles a una clase. 
        # Descubrirá que tiene una lista creciente de atributos y métodos y que sus archivos son cada vez más largos. 
        # En estas situaciones, es posible que reconozca que parte de una clase se puede escribir como una clase separada. 
        # Puede dividir su clase grande en clases más pequeñas que trabajen juntas.

        #Por ejemplo, si continuamos agregando detalles a la clase ElectricCar, podemos notar que estamos agregando muchos atributos y 
        # métodos específicos para la batería del automóvil. Cuando vemos que esto sucede, podemos detener y mover esos atributos y 
        # métodos a una clase separada llamada Batería.
         
# Entonces podemos usar una instancia de Batería como atributo en la clase ElectricCar:
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

    def update_odometer(self, mileage):                                      
        """
        Set the odometer reading to the giving value.
        Reject the chang if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:                            
            self.odometer_reading = mileage                             
        else:                                                          
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles



            #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇codigo nuevo⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇

class Battery:                                                                                  #(1)
    """Asimple attemp to model a battery for an electric car."""

    def __init__(self, battery_size=75):                                                          #(2)
        """Initialize the battery's attributs."""
        self.battery_size = battery_size

    def describe_battery(self):                                                                 #(3)
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

            #⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆codigo nuevo⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()       #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅codigo nuevo (5)

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()    #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅codigo nuevo




#En ➡(1)⬅ definimos una nueva clase llamada Batería que no hereda de ninguna otra clase. 
# El método __init__() en ➡(2)⬅ tiene un parámetro, battery_size, además de self. 
# Este es un parámetro opcional que establece el tamaño de la batería en 75 si no se proporciona ningún valor. 
# El método describe_battery() también se ha movido a esta clase ➡(3)⬅.

#En la clase ElectricCar, ahora agregamos un atributo llamado self.battery ➡(4)⬅. 
# Esta línea le dice a Python que cree una nueva instancia de Batería (con un tamaño predeterminado de 75, 
# porque no estamos especificando un valor) y asigne esa instancia al atributo self.battery. 
# Esto sucederá cada vez que se llame al método init_(); cualquier instancia de ElectricCar ahora 
# tendrá una instancia de batería creada automáticamente.

#Creamos un coche eléctrico y lo asignamos a la variable my_tesla. 
# Cuando queremos describir la batería, necesitamos trabajar con el atributo de la batería del automóvil:
my_tesla.battery.describe_battery()
#Esta línea le dice a Python que mire la instancia my tesla, busque su atributo de batería y llame al 
# método describe_battery() que está asociado con la instancia de batería almacenada en el atributo.

#La salida es idéntica a lo que vimos anteriormente:
#
#           >>> 2019 Tesla Model S
#           >>> This car has a 75-kwh battery.
#
#Esto parece mucho trabajo extra, pero ahora podemos describir la batería con tanto detalle como queramos 
# sin saturar la clase ElectricCar. Agreguemos otro método a Batería que informe el alcance del automóvil 
# según el tamaño de la batería:
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

    def update_odometer(self, mileage):                                      
        """
        Set the odometer reading to the giving value.
        Reject the chang if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:                            
            self.odometer_reading = mileage                             
        else:                                                          
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles




class Battery:                                                                              
    """Asimple attemp to model a battery for an electric car."""

    def __init__(self, battery_size=75):                                                          
        """Initialize the battery's attributs."""
        self.battery_size = battery_size

    def describe_battery(self):                                                                 
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")


            #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇codigo nuevo⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
    def get_range(self):                                                                        #(1)
        """print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge.")
            #⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆codigo nuevo⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()       
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()    
my_tesla.battery.get_range()  #⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅codigo nuevo          #(2)

#El nuevo método get_range() en ➡(1)⬅ realiza un análisis simple. 
# Si la capacidad de la batería es de 75 kWh, get_range() establece el alcance en 260 millas, 
# y si la capacidad es de 100 kWh, establece el alcance en 315 millas. Luego informa este valor. 
# Cuando queramos usar este método, nuevamente tenemos que llamarlo a través del atributo de batería del automóvil en ➡(2)⬅. 
# 
# La salida nos dice la autonomía del coche en función del tamaño de la batería:
#
#           >>> 2019 Tesla Model S
#           >>> This car has a 75-kwh battery.
#           >>> This car can go about 260 miles on full charge.


   