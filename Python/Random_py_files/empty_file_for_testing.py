
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




albumes = []

def make_album(name, artist=None, songs=None):
    """Returning a album"""
    album = {'name': name}
    if artist:
        album['artist'] = artist
    if songs:
        album['songs'] = songs
    
    albumes.append(album)
    return album


while True:
    print("\n\t---Describa un album---")
    print("(ingrese la letra 'q' en cualquier momento para cerrar el programa)\n")

    n_album = input("El nombre del album: ")
    if n_album == 'q'.lower():
        break
    a_album = input("El artista/banda del album: ")
    if a_album == 'q'.lower():
        make_album(n_album)
        break
    s_album = input("Cuantas pistas/canciones tiene el album: ")
    if s_album == 'q'.lower():
        make_album(n_album, a_album)
        break
    make_album(n_album, a_album, s_album)

for album in albumes:
    name = album['name']
    artist = album.get('artist', 'Unknown Artist')
    songs = album.get('songs', 'Unknown')
    print(f"\nAlbum: {name.title()}\nBand/Artist: {artist.title()}\nNumber of Songs: {songs}")