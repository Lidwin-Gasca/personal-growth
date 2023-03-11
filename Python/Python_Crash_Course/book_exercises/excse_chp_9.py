



	#9-1. Restaurante: 
#Haz una clase llamada Restaurante. 
#El método _init_() para Restaurante debe almacenar dos atributos: un nombre_restaurante y un tipo_de_cocina. 
#Cree un método llamado descripcion_restaurante() que imprima estas dos piezas de información, 
#y un método llamado abierto_restaurante() que imprima un mensaje que indique que el restaurante está abierto.

#Cree una instancia llamada restaurante de su clase. 
#Imprima los dos atributos individualmente y luego llame a ambos métodos. 


class Restaurante:
    """Aimple descripcion de una cocina."""

    def __init__(self, nombre_restaurante, tipo_de_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_de_cocina = tipo_de_cocina
        
    def descripcion_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} se especializa en {self.tipo_de_cocina}.")

    def abierto_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} se encuentra abierto en este momento.")

restaurante_1 = Restaurante('El pollo loco', 'pollo rostizado')

restaurante_1.descripcion_restaurante()
restaurante_1.abierto_restaurante()
    















	#9-2. Tres Restaurantes: 
#Comience con su clase del Ejercicio 9-1. 
#Cree tres instancias diferentes de la clase y llame a describe_restaurant() para cada una instancia.

class Restaurante:
    """Simple descripcion de una cocina."""

    def __init__(self, nombre_restaurante, tipo_de_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_de_cocina = tipo_de_cocina
        
    def descripcion_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} se especializa en {self.tipo_de_cocina}.")

    def abierto_restaurante(self):
        print(f"El restaurante de nombre {self.nombre_restaurante} se encuentra abierto en este momento.")

restaurante_1 = Restaurante('El pollo loco', 'pollo rostizado')
restaurante_2 = Restaurante('El Barril', 'mariscos')
restaurante_3 = Restaurante('stella', 'economica')

restaurante_1.descripcion_restaurante()
restaurante_1.abierto_restaurante()
restaurante_2.descripcion_restaurante()
restaurante_2.abierto_restaurante()
restaurante_3.descripcion_restaurante()
restaurante_3.abierto_restaurante()



















	#9-3. Usuarios: 
#Haz una clase llamada Usuario. 
#Crea dos atributos llamados nombre y apellido, y luego crea varios otros atributos que normalmente se 
#almacenan en un perfil de usuario. Haz un método llamado describir_usuario() que imprima un resumen de la 
#información del usuario. Cree otro método llamado saludando_usuario() que imprima un saludo personalizado al usuario. 
#Cree varias instancias que representen a diferentes usuarios y llame a ambos métodos para cada usuario.

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def describir_usuario(self):
        print(f"\nNombre: {self.nombre}\nApellido: {self.apellido}")
    
    def saludando_usuario(self):
        print(f"\tHola {self.nombre}, bienvenido a Python.\n")


user_1 = Usuario('Lidwin', 'Gasca')
user_2 = Usuario('Aritzi', 'Hernandez')
user_3 = Usuario('Abel', 'Garcia')



user_1.describir_usuario()
user_1.saludando_usuario()

user_2.describir_usuario()
user_2.saludando_usuario()

user_3.describir_usuario()
user_3.saludando_usuario()









    #9-4.   Number Served:

#Comience con su programa del Ejercicio 9-1 (página 162). Agregue un atributo llamado número servido con un valor predeterminado de 0. 
# Cree una instancia llamada restaurante de esta clase. 
# Imprime el número de clientes que ha servido el restaurante y luego cambia este valor e imprímelo de nuevo. 
# 
# Agregue un método llamado set_number_served() que le permita establecer el número 
# de clientes que han sido atendidos. Llame a este método con un nuevo número y imprimir el valor de nuevo. 
#
# Agregue un método llamado increment_number_served() que le permita incrementar la cantidad de clientes que han sido atendidos. 
# Llame a este método con cualquier número que desee que pueda representar cuántos clientes se atendieron, digamos, en un día hábil.













    #9-5.   Login Attemps:

#Agregue un atributo llamado intentos de inicio de sesión a su clase de Usuario del Ejercicio 9-3 (página 162). 
# Escriba un método llamado increment_login_attempts() que incremente el valor de los intentos de inicio de sesión en 1. 
# Escriba otro método llamado reset_login_attempts() que restablezca el valor de los intentos de inicio de sesión a 0.
#
#Cree una instancia de la clase Usuario y llame a los intentos de inicio de sesión de incremento () varias veces. 
# Imprima el valor de los intentos de inicio de sesión para asegurarse de que se incrementó correctamente y luego llame a reset_login_attempts(). 
# Imprima los intentos de inicio de sesión nuevamente para asegurarse de que se restableció a 0.