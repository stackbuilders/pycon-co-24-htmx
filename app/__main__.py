import random

from flask import Flask, render_template

app = Flask(__name__)


songs = [
    { "artist": "Sanalejo", "name": "Diablo" },
    { "artist": "Les Petits Bâtards", "name": "Señales" },
    { "artist": "Cuarteto de Nos", "name": "Vida ingrata" },
    { "artist": "Mägo de Oz", "name": "La Costa del Silencio" },
    { "artist": "Lolabúm", "name": "Lágrima" },
    { "artist": "Esteman", "name": "Mr. Trance" },
    { "artist": "Bersuit Vergarabat", "name": "Señor Cobranza" },
    { "artist": "Caramelos de Cianuro", "name": "Rubia Sol Morena Luna" },
    { "artist": "Molotov", "name": "Voto Latino" },
    { "artist": "Los Bunkers", "name": "Miéntele" },
]

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/song')
def song():
    song = random.choice(songs)
    return f"<div><p>{song['artist']} - {song['name']}</p></div>"

# Web 1.0 - Replaces he whole page!

@app.get('/webone')
def webone():
    song = random.choice(songs)
    return render_template('webone.html', song=f"{song['artist']} - {song['name']}")


if __name__ == "__main__":
    app.run(debug=True)
