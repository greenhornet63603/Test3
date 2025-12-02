import os
import threading
import asyncio
from flask import Flask
from pyrofork import Client

# ------------------ Environment Variables ------------------
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

async def run_bot_async():
    """Start the bot asynchronously and keep it running."""
    await bot.start()
    print("Bot Started Successfully")
    await bot.idle()

def start_bot():
    """Run the bot in a separate thread with its own event loop."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot_async())

# ------------------ Flask App ------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot & Flask Running Successfully!"

# ------------------ Main Entry Point ------------------
if __name__ == "__main__":
    # Start the bot in a background thread
    threading.Thread(target=start_bot, daemon=True).start()

    # Start Flask server
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
