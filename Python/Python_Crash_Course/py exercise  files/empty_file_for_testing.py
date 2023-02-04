prompt = "If you  tell us who you are, we, can personalize the messeges you see."
prompt += "\nWhat is your first name?"

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n The number {number} is even.")
else:
    print(f"The number {number} is odd.")




import requests
import datetime
import time

def retrieve_news():
    url = "https://api.example.com/north-carolina-news"
    response = requests.get(url)
    news = response.json()

    print("Latest News from North Carolina:")
    for article in news["articles"]:
        print("\n" + article["title"])
        print(article["description"])

while True:
    current_time = datetime.datetime.now()
    if current_time.hour == 7 and current_time.minute == 5:
        retrieve_news()
    time.sleep(60)