import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    # Render-এর দেওয়া PORT ধরবে, না পেলে 10000 বা 8080 ব্যবহার করবে
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    """
    Runs the Flask server in a separate thread so it won't block python-telegram-bot.
    """
    t = Thread(target=run)
    t.start()
