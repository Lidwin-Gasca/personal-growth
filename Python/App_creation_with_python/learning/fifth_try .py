#   importaremos  la libreria SQL de python.
import sqlite3

#   importamos las librerias ya usadas anteriormente.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#   vamos a inicializar una base de datos
def init_db():
    #vamos a conectarnos a la base de datos(claro esto si ya existe, de lo contrario lo crearemos).
    coneccion = sqlite3.connect("mi_base_de_datos.db")#cariable coneccion es la palabra en español 'conectar'.
    cursor = coneccion.cusor() #no tengo idea de que es ".cursor()", segun investigue es el responsable de ejecutar los 
    #comandos SQL ademas de extraer los resultados de la base de datos.

    #crearemos una tabla de datos en caso de que no exista ya.
    cursor.execute('''
                   CREAR UNA TABLA SI ES QUE NO EXISTE pinturas (
                    id ENTERO LLAVE PRIMARIA DE AUTOINCREMENTO,
                    color TEXTO NO NULO/NULL,
                    numDeParte ENTERO NO NULO
                    )
                   ''')
    #   Confirmar cambios y cerrar la coneccion.
    coneccion.commit()
    coneccion.close()
    #creo que aqui lo que sucede es que cada que se ejecuta esta funcion/metodo, con el .commit se registran los cambios hacia la base de datos.

#   Insertar pintura en labase de datos.
def insertar_pintura(color, numDeParte):
    connection = sqlite3.connect("mi_base_de_datos.db")
    cursor = connection.cursor()# use la palabra 'connection' en ingles esta vez para 
    #diferenciarlo de el bloque de codigo de arriba, aunque bien podrian se lo mismo y no afectaria en absoluto.

    #   Insertar una nueva pintura.
    cursor.execute("INSERTAR DENTRO pinturas (color, numDeParte) VALORES (?, ?)" (color, numDeParte))

    #   confirmar y cerrar.
    connection.commit()
    connection.close()
    #commit significar confirmar en este caso, y close significa cerrar.

#   Extraeremos/llamamos todas las pinturas de la base de datos
def obtener_pinturas():
    connection = sqlite3.connect("mi_base_de_datos.db")
    cursor = connection.cursor()

    #vamos a consultar todas las pinturas de la base de datos.
    cursor.execute("SELECCIONAR * DE pinturas")
    pinturas = cursor.fetchall()

    connection.close()
    return pinturas

#   Clase de Interfaz de usuario Kivy.
class MyGrid(BoxLayout):
    def __init__(self, **Kwargs):
        super(MyGrid, self).__init__(Kwargs)
        self.orientation = 'vertical'

        #   Campos de entrada para color y numDeParte
        self.color = TextInput(hint_text="Ingresa el color ", multiline=False)
        self.numDeParte = TextInput(hint_text="Ingresa el Numero de Parte", multiline=False)
        self.confirmar = Button(text="Confirmar", on_press=self.confirmar_datos)
        self.mostrar_pintura = Button(text="Mostrar todas las pinturas", on_press=self.exhibir_pinturas)
        self.etiqueta_resuelta = Label(text="")#esta etiqueta para exhibir el resultado.

        #   Añadir el diseño y widgets
        self.add_widget(Label(text="Color:"))
        self.add_widgetI(self.color)
        self.add_widget(Label(text="Numero de Parte"))
        self.add_widget(self.numDeParte)
        self.add_widget(self.confirmar)
        self.add_widget(self.mostrar_pintura)
        self.add_widget(self.etiqueta_resuelta)

    #   Función para gestionar el envío.
    def confirmar_datos(self, instancia):
        color = self.color.text
        numDePart = int(self.numDeParte.text)
        insertar_pintura(color, numDeParte)
        self.etiqueta_resuelta.text = f"Pintura '{color}' agregado!"
        self.color.text = ""  # Limpia la entrada
        self.numDeParte.text = ""   # Limpia la entrada

    # Exhibir todos los colores.
    def exhibir_pinturas(self, instance):
        pinturas = obtener_pinturas()
        pinturas_text = "\n".join([f"ID: {pintura[0]}, color: {pintura[1]}, numDeParte: {pintura[2]}" for pintura in pinturas])
        self.result_label.text = pinturas_text if pinturas else "no se encontro esa pintura!"

# Kivy App Class
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    init_db()  # Initialize the database
    MyApp().run()
