import os
import threading
import asyncio
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

async def run_pyrogram():
    # Start bot
    await bot.start()
    print("Bot Started Successfully")
    await bot.idle()

def start_bot():
    # Create event loop for this thread (fixes your error)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_pyrogram())

# ------------------ Flask Keeper ------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot & Flask Running Successfully!"

if __name__ == "__main__":
    # Start Telegram bot in background thread
    threading.Thread(target=start_bot).start()

    # Start Flask server
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
