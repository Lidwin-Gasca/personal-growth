from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout #esto trera una organizacion de espacios dentro de la ventana/laplicacion.
from kivy.uix.textinput import TextInput #de esta libreria importamos "TextInput" para poder crear un espacio que acepte nuestro dato de entrada.
from kivy.uix.button import Button #como ya es ituitivo esto habilita es uso de un boton en nuestra ventana/aplicacion.

class MiPrimerApp(App):
    def build(self):

        #Lista de Entradas guardadas
        self.lista = []

        # Box Layout / Orden de casilla
        casillas = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Etiqueta/Label
        #creacion de la casilla Etiqueta.
        etiqueta = Label(text="Escribe un color:")
        casillas.add_widget(etiqueta)

        # Text Input / Dato de Entrada
        self.entrada = TextInput(hint_text="Ingrese un color", multiline=False)
        casillas.add_widget(self.entrada)

        # Button / Boton
        boton = Button(text="Guardar color")
        boton.bind(on_press=self.color_guardado)
        casillas.add_widget(boton)

        # Result Label / Resolver Etiqueta
        self.resuelve_etiqueta = Label(text="")
        casillas.add_widget(self.resuelve_etiqueta)

        #Lista de colores
        self.mostrar_lista = Label(text="")
        casillas.add_widget(self.mostrar_lista)




        return casillas
    
    # Metodo
    def color_guardado(self, instancia):
        color = self.entrada.text
        self.resuelve_etiqueta.text = f"Color agregado: {color}"
        self.entrada.text = "" #con esto limpiamos de nuevo el campo de entrada.
        self.lista.append(color)
        self.mostrar_lista.text = f"{self.lista}"
        #para una lista mas agradable a los ojos escribir asi:
        self.mostrar_lista.text = f"Colores guardados: {', ' .join(self.lista)}"

app = MiPrimerApp()
app.run()
