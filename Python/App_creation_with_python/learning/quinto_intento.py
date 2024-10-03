import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Inicializar la base de datos
def init_db():
    conexion = sqlite3.connect("mi_base_de_datos.db")
    cursor = conexion.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pinturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            color TEXT NOT NULL,
            numDeParte INTEGER NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

# Insertar una nueva pintura
def insertar_pintura(color, numDeParte):
    conexion = sqlite3.connect("mi_base_de_datos.db")
    cursor = conexion.cursor()

    # Insertar una nueva pintura
    cursor.execute("INSERT INTO pinturas (color, numDeParte) VALUES (?, ?)", (color, numDeParte))

    conexion.commit()
    conexion.close()

# Obtener todas las pinturas
def obtener_pinturas():
    conexion = sqlite3.connect("mi_base_de_datos.db")
    cursor = conexion.cursor()

    # Consultar todas las pinturas
    cursor.execute("SELECT * FROM pinturas")
    pinturas = cursor.fetchall()

    conexion.close()
    return pinturas

# Interfaz de usuario con Kivy
class MyGrid(BoxLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Campos de entrada para color y numDeParte
        self.color = TextInput(hint_text="Ingresa el color", multiline=False)
        self.numDeParte = TextInput(hint_text="Ingresa el Número de Parte", multiline=False)
        self.confirmar = Button(text="Confirmar", on_press=self.confirmar_datos)
        self.mostrar_pintura = Button(text="Mostrar todas las pinturas", on_press=self.exhibir_pinturas)
        self.etiqueta_resuelta = Label(text="")

        # Añadir widgets al diseño
        self.add_widget(Label(text="Color:"))
        self.add_widget(self.color)
        self.add_widget(Label(text="Número de Parte"))
        self.add_widget(self.numDeParte)
        self.add_widget(self.confirmar)
        self.add_widget(self.mostrar_pintura)
        self.add_widget(self.etiqueta_resuelta)

    # Función para manejar la acción del botón "Confirmar"
    def confirmar_datos(self, instance):
        color = self.color.text
        numDeParte = int(self.numDeParte.text)
        insertar_pintura(color, numDeParte)
        self.etiqueta_resuelta.text = f"Pintura '{color}' agregada!"
        self.color.text = ""  # Limpiar el campo de entrada
        self.numDeParte.text = ""   # Limpiar el campo de entrada

    # Función para mostrar todas las pinturas
    def exhibir_pinturas(self, instance):
        pinturas = obtener_pinturas()
        pinturas_text = "\n".join([f"ID: {pintura[0]}, color: {pintura[1]}, Numero de parte: {pintura[2]}" for pintura in pinturas])
        self.etiqueta_resuelta.text = pinturas_text if pinturas else "No se encontró ninguna pintura."

# Clase principal de la aplicación Kivy
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    init_db()  # Inicializar la base de datos
    MyApp().run()
