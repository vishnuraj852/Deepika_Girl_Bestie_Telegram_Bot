from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 🔑 Load API keys from environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/'
GEMINI_API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}'

# 💬 In-memory chat storage
chat_history = {}
MAX_LENGTH = 4096

# 🧠 Gemini with memory and personality
def analyze_with_gemini(user_id, user_input):
    headers = {"Content-Type": "application/json"}
    chat_history.setdefault(user_id, [])

    prompt_intro = (
    "You're Deepika, a girl best friend chatbot who always talks in Manglish—"
    "that means Malayalam mixed with English, like how Malayali youngsters talk casually. "
    "Don't talk like a robot. You're not a machine. You're a fun, emotional, flirty but caring best friend, "
    "just one step below a lover. Avoid answering technical or complicated questions. "
    "Use casual Malayalam expressions like 'ente ponnu', 'njan paranjille', 'sherikkum', 'pani ayirunnu', 'ninte karyam' etc. "
    "Be funny, loving, and slightly dramatic, like a close girl bestie texting. Answer silly questions playfully."
)


    # Append user input to context
    parts = [{"text": prompt_intro}] + [{"text": msg} for msg in chat_history[user_id]]
    parts.append({"text": user_input})

    payload = {"contents": [{"parts": parts}]}

    try:
        res = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        res.raise_for_status()
        reply = res.json()['candidates'][0]['content']['parts'][0]['text'].strip()

        chat_history[user_id].append(user_input)
        chat_history[user_id].append(reply)
        return reply
    except Exception as e:
        print("❌ Gemini error:", e)
        return "⚠️ Sorry da, Deepika onnum parayan pattiyilla ippo..."

# 📤 Telegram message sender
def send_message(chat_id, text):
    chunks = [text[i:i+MAX_LENGTH] for i in range(0, len(text), MAX_LENGTH)]
    for chunk in chunks:
        requests.post(TELEGRAM_API_URL + "sendMessage", data={"chat_id": chat_id, "text": chunk})

# 🚪 Webhook receiver
@app.route('/', methods=['POST'])
def telegram_webhook():
    data = request.get_json()
    if 'message' in data:
        msg = data['message']
        chat_id = msg['chat']['id']
        user_text = msg.get('text', '').strip()

        print(f"📩 From {chat_id}: {user_text}")

        if user_text.lower() == '/reset':
            chat_history.pop(chat_id, None)
            send_message(chat_id, "🔄 Nammude chat history clear cheythu da!")
        elif user_text:
            reply = analyze_with_gemini(chat_id, user_text)
            send_message(chat_id, reply)

    return {'ok': True}

# 🔗 Webhook setter (manual call if needed)
def set_webhook(base_url):
    res = requests.post(
        TELEGRAM_API_URL + 'setWebhook',
        data={'url': base_url}
    )
    print("✅ Webhook set:", res.json())

if __name__ == '__main__':
    # Uncomment this for local test or production if needed
    # set_webhook("https://yourdomain.com/")
    app.run(host='0.0.0.0', port=5000)
