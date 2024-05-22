import random

from flask import Flask, render_template, request

app = Flask(__name__)

songs = [
    { "id": 1, "artist": "Sanalejo", "name": "Diablo", "country": "🇨🇴" },
    { "id": 2, "artist": "Les Petits Bâtards", "name": "Señales", "country": "🇪🇨" },
    { "id": 3, "artist": "Cuarteto de Nos", "name": "Vida ingrata", "country": "🇺🇾" },
    { "id": 4, "artist": "Mägo de Oz", "name": "La Costa del Silencio", "country": "🇪🇸" },
    { "id": 5, "artist": "Lolabúm", "name": "Lágrima", "country": "🇪🇨" },
    { "id": 6, "artist": "Esteman", "name": "Mr. Trance", "country": "🇨🇴" },
    { "id": 7, "artist": "Bersuit Vergarabat", "name": "Señor Cobranza", "country": "🇦🇷" },
    { "id": 8, "artist": "Caramelos de Cianuro", "name": "Rubia Sol Morena Luna", "country": "🇻🇪" },
    { "id": 9, "artist": "Molotov", "name": "Voto Latino", "country": "🇲🇽" },
    { "id": 10, "artist": "Soda Estereo", "name": "Prófugos", "country": "🇦🇷" },
    { "id": 11, "artist": "Zoe", "name": "Poli", "country": "🇲🇽" },
    { "id": 12, "artist": "Los Bunkers", "name": "Miéntele", "country": "🇨🇱" },
    { "id": 13, "artist": "Los Prisioneros", "name": "Tren al Sur", "country": "🇨🇱" },
]

def render_songs(q = '') -> str:
    return "".join(
        [render_template('song.html', song=song)
         for song in songs
         if q.lower() in f"{song['artist']}{song['name']}".lower()
        ]
    )

@app.get('/')
def index():
    return render_template('index.html', songs=songs)

@app.get('/songs/search')
def songs_search():
    q = request.args.get('q') or ''
    return render_songs(q)

@app.delete('/songs/<int:id_>')
def remove_song(id_: int):
    for song in songs:
        if song['id'] == id_:
            songs.remove(song)
            break
    return ""

if __name__ == "__main__":
    app.run(debug=True)
