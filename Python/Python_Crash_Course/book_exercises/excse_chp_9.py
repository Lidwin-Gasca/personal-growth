



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





















	#9-3. Usuarios: 
#Haz una clase llamada Usuario. 
#Crea dos atributos llamados first_name y apellido, y luego crea varios otros atributos que normalmente se 
#almacenan en un perfil de usuario. Haz un método llamado describe_user() que imprima un resumen de la 
#información del usuario. Cree otro método llamado greeting_user() que imprima un saludo personalizado al usuario. 
#Cree varias instancias que representen a diferentes usuarios y llame a ambos métodos para cada usuario.