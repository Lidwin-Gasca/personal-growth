from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout #esto trera una organizacion de espacios dentro de la ventana/laplicacion.
from kivy.uix.textinput import TextInput #de esta libreria importamos "TextInput" para poder crear un espacio que acepte nuestro dato de entrada.
from kivy.uix.button import Button #como ya es ituitivo esto habilita es uso de un boton en nuestra ventana/aplicacion.

class MiPrimerApp(App):
    def build(self):

        # Box Layout / Orden de casilla
        #vamos a especificar los espacios esparcidos en nuestra ventana/aplicacion, mas bien asignar los bordes de cada elemento de esta ventana/aplicacion.
        #dandolo como un valor para "casillas".
        casillas = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Etiqueta/Label
        #creacion de la casilla Etiqueta.
        etiqueta = Label(text="Escribe un color:")
        casillas.add_widget(etiqueta)

        # Text Input / Dato de Entrada
        #crearemnos una variable cuyo valor es un recuadro que tenga un mensaje temporal que indica una instruccion al usiario, 
        #para tener ese mensaje hay que usar hint_text='mensaje', ahora el "multiline" no se que significa.
        # Cabe notar que se debe usar "self" al declarar la variable  'self.entrada', sin esta, no funcionara, ya el el 'self.' hara que 'entrada' se
        #convierta en una instancia, para asi poder usar el metodo 'color_guardo' que se usara mas abajo en el codigo.
        self.entrada = TextInput(hint_text="Ingrese un color", multiline=False)
        casillas.add_widget(self.entrada)

        # Button / Boton
        #creamos un boton que a su vez contenga un texto dentro de el mismo.
        #con '.bind' lo enlazaremos a el metodo 'color_guardado' al momento de ejecutar la accion 'on_press'.
        #al final dicho boton se añade a la ventana/aplicacion usando la variable 'casillas' y atribuyendole la libreria '.add_widget(el wid_get que estamos añadiendo)'.
        #al presionar este boton se ejecutara el metodo 'color_guardado'
        boton = Button(text="Guardar color")
        boton.bind(on_press=self.color_guardado)
        casillas.add_widget(boton)

        # Result Label / Resolver Etiqueta
        #creamos la instancia de devolucion de etiqueta (creo, no estoy eguro de esto)
        #y porque es instancia debemos usar el 'self.'
        self.resuelve_etiqueta = Label(text="")
        casillas.add_widget(self.resuelve_etiqueta)

        #al escribir el siguiente codigo, estamos pidiendo visualizar 'casillas' que es la organizacion y demostracion de el contenido de el mismo.
        return casillas
    
    # Metodo
    #creamos un metodo llamado 'color_guardado' como atributo ponemos el fiel de siempre 'self' e 'instancia' 
    #(instancia supongo son las variables que recibimos de el codigo de arriba que convertimos en instancia al agregar 'self.').
    #declaramos la variable 'color' asignandole la instancia de 'entrada'.
    #al presionar el boton en la aplicacion, se ejecutara este metodo, creando asi una frase que estara posisionado en la parte inferior de la ventana/aplicacion
    #la razon por la que este aparece abajo es por el orden en que fuimos añadiendo wid_gets a la variable 'casilla'.
    def color_guardado(self, instancia):
        color = self.entrada.text
        self.resuelve_etiqueta.text = f"Color guardado: {color}"
        self.entrada.text = "" #con esto limpiamos de nuevo el campo de entrada.



app = MiPrimerApp()
app.run()
