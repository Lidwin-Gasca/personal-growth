prompt = "If you  tell us who you are, we, can personalize the messeges you see."
prompt += "\nWhat is your first name?"

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n The number {number} is even.")
else:
    print(f"The number {number} is odd.")