



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

#Comience con su programa del Ejercicio 9-1 (página 162). Agregue un atributo llamado número_servido con un valor predeterminado de 0. 
# Cree una instancia llamada restaurante de esta clase. 
# Imprime el número de clientes que ha servido el restaurante y luego cambia este valor e imprímelo de nuevo. 
# 
# Agregue un método llamado establecer_numero_servido() que le permita establecer el número 
# de clientes que han sido atendidos. Llame a este método con un nuevo número y imprimir el valor de nuevo. 
#
# Agregue un método llamado incrementar_numero_servido() que le permita incrementar la cantidad de clientes que han sido atendidos. 
# Llame a este método con cualquier número que desee que pueda representar cuántos clientes se atendieron, digamos, en un día hábil.


class Restaurante:
    """Simple descripcion de una cocina."""

    def __init__(self, nombre_restaurante, tipo_de_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_de_cocina = tipo_de_cocina
        self.numero_servido = 0 #⬅codigo nuevo
        
    def descripcion_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} se especializa en {self.tipo_de_cocina}.")

    def abierto_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} se encuentra abierto en este momento.")

    def establecer_numero_servido(self, num_servido):   #⬅codigo nuevo
        self.numero_servido = num_servido               #⬅codigo nuevo
        print(f"El restaurante {self.nombre_restaurante} ha servido a {self.numero_servido} clientes.") #⬅codigo nuevo

    def incrementar_numero_servido(self, num_inc):      #⬅codigo nuevo
        self.numero_servido += num_inc                  #⬅codigo nuevo
        print(f"El restaurante {self.nombre_restaurante}, vendio {self.numero_servido} platillos el dia de hoy.") #⬅codigo nuevo

restaurante_1 = Restaurante('El pollo loco', 'pollo rostizado')
restaurante_2 = Restaurante('El burrito', 'comida mexicana')
restaurante_1.descripcion_restaurante()
restaurante_1.abierto_restaurante()
restaurante_1.establecer_numero_servido(7)
restaurante_1.incrementar_numero_servido(2)
restaurante_2.incrementar_numero_servido(3)














    #9-5.   Login Attemps:

#Agregue un atributo llamado login_attempts a su clase de Usuario del Ejercicio 9-3 (página 162). 
# Escriba un método llamado increment_login_attempts() que incremente el valor de los intentos de inicio de sesión en 1. 
# Escriba otro método llamado reset_login_attempts() que restablezca el valor de los intentos de inicio de sesión a 0.
#
#Cree una instancia de la clase Usuario y llame a increment_login_attempts() varias veces. 
# Imprima el valor de los login_attempts para asegurarse de que se incrementó correctamente y luego llame a reset_login_attempts(). 
# Imprima login_attempts nuevamente para asegurarse de que se restableció a 0. 


class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.login_attempts = 0                         #⬅codigo nuevo 

    def describir_usuario(self):
        print(f"\nNombre: {self.nombre}\nApellido: {self.apellido}")
    
    def saludando_usuario(self):
        print(f"\tHola {self.nombre}, bienvenido a Python.\n")

    def increment_login_attempts(self):                 #⬅codigo nuevo
        self.login_attempts = self.login_attempts + 1   #⬅codigo nuevo

    def reset_login_attempts(self): #⬅codigo nuevo
        self.login_attempts = 0     #⬅codigo nuevo


user_1 = Usuario('Lidwin', 'Gasca')
user_2 = Usuario('Aritzi', 'Hernandez')
user_3 = Usuario('Abel', 'Garcia')
user_4 = Usuario('Yjaira', 'rico')


user_1.describir_usuario()
user_1.saludando_usuario()

user_2.describir_usuario()
user_2.saludando_usuario()

user_3.describir_usuario()
user_3.saludando_usuario()


print(user_4.login_attempts)        #⬅codigo nuevo
user_4.increment_login_attempts()   #⬅codigo nuevo
print(user_4.login_attempts)        #⬅codigo nuevo
user_4.increment_login_attempts()   #⬅codigo nuevo
print(user_4.login_attempts)        #⬅codigo nuevo
user_4.increment_login_attempts()   #⬅codigo nuevo
print(user_4.login_attempts)        #⬅codigo nuevo
user_4.increment_login_attempts()   #⬅codigo nuevo
print(user_4.login_attempts)        #⬅codigo nuevo

user_4.reset_login_attempts()       #⬅codigo nuevo
print(user_4.login_attempts)        #⬅codigo nuevo














    #9-6.   Ice Cream Stand:
#Un puesto de helados es un tipo específico de restaurante. Escriba una clase llamada IceCreamStand que herede de la clase Restaurante 
# que escribió en el Ejercicio 9-1 (página 162) o el Ejercicio 9-4 (página 167). Cualquiera de las versiones de 
# la clase funcionará, solo elige la que más te guste. Agregue un atributo llamado sabores que almacene una lista de sabores 
# de helado. Escribe un método que muestre estos sabores. Cree una instancia de IceCreamStand y llame a este método.

class Restaurante:
    """Simple descripcion de una cocina."""

    def __init__(self, nombre_restaurante, tipo_de_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_de_cocina = tipo_de_cocina
        self.numero_servido = 0
        
    def descripcion_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} se especializa en {self.tipo_de_cocina}.")

    def abierto_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} se encuentra abierto en este momento.")

    def establecer_numero_servido(self, num_servido):
        self.numero_servido = num_servido            
        print(f"El establecimiento {self.nombre_restaurante} ha servido a {self.numero_servido} clientes.")

    def incrementar_numero_servido(self, num_inc):   
        self.numero_servido += num_inc               
        print(f"El establecimiento {self.nombre_restaurante}, vendio {self.numero_servido} platillos el dia de hoy.")



            #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇codigo nuevo⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
class IceCreamStand(Restaurante):
    """
        Una clase hijo llamado 'IceCreamStand' para la clase Restaurante.

    """


    def __init__(self, nombre_restaurante, tipo_de_cocina):
        super().__init__(nombre_restaurante, tipo_de_cocina)
        sabores = ['valnilla', 'chocolate', 'fresa']
        self.sabores = sabores

    def mostrar_sabores(self):
        """Llamar a imprimir la lista de sabores de helados"""
        print(f"Lista de sabores: {self.sabores}.")


    def descripcion_heladeria(self):
        print(f"La heladeria {self.nombre_restaurante} se especializa en {self.tipo_de_cocina}.")

    def abierto_heladeria(self):
        print(f"La heladeria {self.nombre_restaurante} se encuentra abierto en este momento.")

            #⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆codigo nuevo⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆



restaurante_1 = Restaurante('El pollo loco', 'pollo rostizado')
restaurante_2 = Restaurante('El burrito', 'comida mexicana')
restaurante_1.descripcion_restaurante()
restaurante_1.abierto_restaurante()
restaurante_1.establecer_numero_servido(7)

#⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇codigo nuevo⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
heladeria_1 = IceCreamStand('la guadalupana', 'heladeria')
heladeria_1.descripcion_heladeria()
heladeria_1.mostrar_sabores()
heladeria_1.abierto_heladeria()
heladeria_1.establecer_numero_servido(5)
#⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆codigo nuevo⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆























    #9-7. Admin:
#Un administrador es un tipo especial de usuario. 
# Escriba una clase llamada Admin que herede de la clase Usuario que escribió en el Ejercicio 9-3 (página 162)
# o el Ejercicio 9-5 (página 167). Agregue un atributo, privilegios, que almacene una lista de cadenas como 
# "puede agregar una publicación", "puede eliminar una publicación", "puede prohibir a un usuario", etc. 
# Escriba un método llamado mostrar privilegios() que enumere el conjunto de privilegios del administrador. 
# Cree una instancia de Admin y llame a su método.



































    #9-8.   Privileges:
#Escriba una clase de Privilegios separada. 
# La clase debe tener un atributo, privilegios, que almacene una lista de cadenas como se describe en el Ejercicio 9.7. 
# Mueva el método show_privileges() a esta clase. Cree una instancia de Privilegios como un atributo en la clase Admin. 
# Cree una nueva instancia de Admin y use su método para mostrar sus privilegios.





















    #9-9.   Battery Upgrade:
#Utilice la versión final de electric_car.py de esta sección. Agregue un método a la clase Batería llamado upgrade_battery(). 
# Este método debería verificar el tamaño de la batería y establecer la capacidad en 100 si aún no lo está. 
# Haga un automóvil eléctrico con un tamaño de batería predeterminado, llame a get_range() una vez y luego llame a 
# get range() una segunda vez después de actualizar la batería. Debería ver un aumento en el alcance del automóvil.




































