import random

from flask import Flask, render_template

app = Flask(__name__)

songs = [
    { "artist": "Sanalejo", "name": "Diablo", "country": "🇨🇴" },
    { "artist": "Les Petits Bâtards", "name": "Señales", "country": "🇪🇨" },
    { "artist": "Cuarteto de Nos", "name": "Vida ingrata", "country": "🇺🇾" },
    { "artist": "Mägo de Oz", "name": "La Costa del Silencio", "country": "🇪🇸" },
    { "artist": "Lolabúm", "name": "Lágrima", "country": "🇪🇨" },
    { "artist": "Esteman", "name": "Mr. Trance", "country": "🇨🇴" },
    { "artist": "Bersuit Vergarabat", "name": "Señor Cobranza", "country": "🇦🇷" },
    { "artist": "Caramelos de Cianuro", "name": "Rubia Sol Morena Luna", "country": "🇻🇪" },
    { "artist": "Molotov", "name": "Voto Latino", "country": "🇲🇽" },
    { "artist": "Los Bunkers", "name": "Miéntele", "country": "🇨🇱" },
]

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/song')
def song():
    song = random.choice(songs)
    return f"<div><p>{song['artist']} - {song['name']} - {song['country']}</p></div>"

# Web 1.0 - Replaces he whole page!

@app.get('/webone')
def webone():
    song = random.choice(songs)
    return render_template('webone.html', song=f"{song['artist']} - {song['name']} - {song['country']}")


if __name__ == "__main__":
    app.run(debug=True)
