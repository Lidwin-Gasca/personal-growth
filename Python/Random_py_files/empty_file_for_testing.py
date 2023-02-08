
# import requests
# import datetime
# import time

# def retrieve_news():
#     url = "https://api.example.com/north-carolina-news"
#     response = requests.get(url)
#     news = response.json()

#     print("Latest News from North Carolina:")
#     for article in news["articles"]:
#         print("\n" + article["title"])
#         print(article["description"])

# while True:
#     current_time = datetime.datetime.now()
#     if current_time.hour == 7 and current_time.minute == 5:
#         retrieve_news()
#     time.sleep(60)


encuesta = {}

while True:
    nombre = input("Como te llamas? ")
    respuesta = input("A donde te gustaria ir de vacariones? ")
    repetir = input("Alguien mas tomara la encuesta? (si / no) ")
    encuesta[nombre] = respuesta

    if repetir.lower() == 'no':
        break

print("\n---Resultados de Encuesta---\n")
for nombre, respuesta in encuesta.items():
    print(f"A {nombre.title()} le gustaria ir {respuesta} de vacaciones")