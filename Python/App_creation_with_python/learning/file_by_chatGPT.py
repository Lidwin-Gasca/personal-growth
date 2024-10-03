import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Database initialization
def init_db():
    # Connect to the database (creates if it doesn't exist)
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    
    # Commit changes and close the connection
    connection.commit()
    connection.close()

# Insert user into the database
def insert_user(name, age):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    
    # Insert a new user
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    
    # Commit and close
    connection.commit()
    connection.close()

# Fetch all users from the database
def get_users():
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    
    # Query all users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()  # Fetch all rows
    
    connection.close()
    return users

# Kivy UI Class
class MyGrid(BoxLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Input fields for Name and Age
        self.name = TextInput(hint_text="Enter Name", multiline=False)
        self.age = TextInput(hint_text="Enter Age", multiline=False)
        self.submit = Button(text="Submit", on_press=self.submit_data)
        self.show_users = Button(text="Show All Users", on_press=self.display_users)
        self.result_label = Label(text="")  # Label to display results

        # Add widgets to the layout
        self.add_widget(Label(text="Name:"))
        self.add_widget(self.name)
        self.add_widget(Label(text="Age:"))
        self.add_widget(self.age)
        self.add_widget(self.submit)
        self.add_widget(self.show_users)
        self.add_widget(self.result_label)
        
    # Function to handle submission
    def submit_data(self, instance):
        name = self.name.text
        age = int(self.age.text)
        insert_user(name, age)
        self.result_label.text = f"User '{name}' added!"
        self.name.text = ""  # Clear input
        self.age.text = ""   # Clear input
    
    # Function to display all users
    def display_users(self, instance):
        users = get_users()
        users_text = "\n".join([f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}" for user in users])
        self.result_label.text = users_text if users else "No users found!"

# Kivy App Class
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    init_db()  # Initialize the database
    MyApp().run()
