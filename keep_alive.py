from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!", 200

def run():
    app.run(host='0.0.0.0', port=5000)

def start():
    thread = Thread(target=run, daemon=True)
    thread.start()
