import requests
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    resp = requests.get(f"{URL}/getUpdates", params=params)
    return resp.json()

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

def handle_message(message):
    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/hola":
        send_message(chat_id, "¡Hola!")
    elif text == "/hora":
        hora = datetime.now().strftime("%H:%M:%S")
        send_message(chat_id, f"Hora actual: {hora}")
    elif text == "/contacto":
        send_message(chat_id, "contacto@grupo4.com")
    elif text == "/proyecto":
        send_message(chat_id, "Bot de tarea IA1")

def main():
    offset = None
    while True:
        updates = get_updates(offset)

        for update in updates["result"]:
            offset = update["update_id"] + 1

            if "message" in update:
                handle_message(update["message"])

        time.sleep(1)

if __name__ == "__main__":
    try:
        if not TOKEN:
            raise ValueError("BOT_TOKEN no encontrado en .env")
        print("Bot iniciado. Presiona Ctrl+C para detener.")
        main()
    except KeyboardInterrupt:
        print("\nBot detenido.")
    except Exception as e:
        print(f"Error: {e}")