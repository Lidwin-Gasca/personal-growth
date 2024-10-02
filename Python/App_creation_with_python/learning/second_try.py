from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.text_input = TextInput(hint_text='Enter text here', multiline=False)
        button = Button(text='Submit')
        button.bind(on_press=self.on_button_click)
        self.label = Label(text='')

        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.label)

        return layout

    def on_button_click(self, instance):
        self.label.text = f'You entered: {self.text_input.text}'

if __name__ == '__main__':
    MyApp().run()