    #importamos aquellas librerias que nos ayudaran a rascar la pagina web:
#el que toma la pagina.
from urllib.request import urlopen as uReq
#el HTML parser
from bs4 import BeautifulSoup as soup

    #creamos una variable que mantendra como contenido el link de la pagina web.
mi_url = 'https://books.toscrape.com/'

    #tomamos la paginda web y lo metemos en la variable ➡️ "uclient"
uClient = uReq(mi_url)

    #vamos a leer y a su vez verrar la pagina web.
page_html = uClient.read()
uClient.close()

    #llamamos a BeautifulSoup para que haga el parsing.
page_soup = soup(page_html, "html.parser")

    #tomamos todos los productos bajo las etiquetas de nombre lista "li"
bookshelf = page_soup.findAll(
    "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"}
)

    # crearemos un archivo csv de todos los productos.
filename = ("Book.csv")
f = open(filename,"w")

headers = "Book title, Price\n"
f.write(headers)


    # Hare una un listado usando el metodo "for"
for books in bookshelf:

    #recolectamos el titulo de todos los libros.
    book_title = books.h3.a["title"]

    #recolectamos tambien los precios de los libros.
    book_price = books.findAll("p", {"class": "price_color"})
    price = book_price[0].text.strip()

    print("Title of the book : " + book_title)
    print(f"Price of the book : {price}")

    f.write(f"{book_title}, {price}\n")

f.close()
