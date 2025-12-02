import os
import threading
from flask import Flask
from pyrofork import Client

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ------------------ Telegram Bot ------------------
bot = Client(
    "mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def start_bot():
    bot.run()

# ------------------ Flask Keeper ------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Running Successfully!"

if __name__ == "__main__":
    # Start Telegram bot in background thread
    threading.Thread(target=start_bot).start()

    # Start Flask server
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
