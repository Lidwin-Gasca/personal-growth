#vamos a empezar importando de kivy para crar una aplicacion kivy, despues importamos la etiqueta.
from kivy.app import App
from kivy.uix.label import Label

class BasicApp(App): #la palabra App es una subclase de Basic App, asi que lo que anademos a App se hereda a AasicApp
    def build(self):
        label = Label(text="hello Word")
        return label
    
app = BasicApp()
app.run()