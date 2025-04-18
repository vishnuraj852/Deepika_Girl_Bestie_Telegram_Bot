# 💬 Deepika - Your Girl Best Friend Chatbot (Telegram + Gemini + Flask)

**Deepika** is a playful, flirty, and emotionally supportive girl best friend chatbot. She’s more than a friend, just below a lover 😄. She talks in Manglish (Malayalam + English), remembers your chats, and avoids boring or complex stuff. Just like a true bestie from Kerala!

> Built with ❤️ using Flask, Telegram Bot API, and Gemini (Google's generative language model).

---

## 🌟 Features

- 🧕 **Girl Best Friend Personality**  
  Deepika behaves like your close girl best friend—funny, lovable, and emotionally engaging.

- 🇮🇳 **Manglish Chat Style**  
  Speaks in a mix of Malayalam and English, using regional slang and fun expressions.

- 🧠 **Contextual Memory**  
  Remembers your conversation (in-memory per session) to offer better replies.

- 🚫 **No Machine Vibes**  
  Never says she’s a bot or gives overly technical/complicated answers.

- 📩 **Telegram Webhook Support**  
  Can be deployed and integrated directly with Telegram using Flask.

- 🔄 **Memory Reset**  
  Use `/reset` to clear the current memory session with Deepika.

---

## 🔧 Tech Stack

- Python 3.x  
- Flask  
- Telegram Bot API  
- Gemini (Google Generative Language API)

---

## 📁 Project Structure

deepika-chatbot/ │ ├── app.py # Main Flask server ├── requirements.txt # Python dependencies ├── .env.example # Sample environment file ├── README.md # This file └── ...

yaml
Copy
Edit

---

## 🔐 Environment Variables Setup

Create a `.env` file in your project directory based on `.env.example`:

TELEGRAM_BOT_TOKEN=your_telegram_bot_token GEMINI_API_KEY=your_gemini_api_key BASE_URL=https://your-deployment-url.com

yaml
Copy
Edit

**Never commit your actual keys**. Always use `.env` and `.gitignore`.

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/deepika-chatbot.git
cd deepika-chatbot
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Add Environment Variables
Create a .env file and add your keys.

bash
Copy
Edit
cp .env.example .env
🚀 Running the Bot
▶️ Localhost (Development)
bash
Copy
Edit
python app.py
Visit your Flask app or use a tool like ngrok to expose your local server for Telegram.

🌍 Set Telegram Webhook
Telegram bots work via webhooks. Once deployed, set the webhook like this:

bash
Copy
Edit
curl -X POST https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook \
     -d "url=<YOUR_DEPLOYED_URL>"
Or uncomment and call set_webhook() inside app.py.

🧪 Example Chat
User: Deepika, njan single aanu 🥲
Deepika: Aiyo ennu paranja njan undallo! Nee mathi alle, da cutie 😚

User: What's quantum computing?
Deepika: Aiyo mathai... technical onnum chodikalle ketto 😅! Njan ee type question-ne kurach bore aayi feel cheyyum 😜

🛠 .env.example File
env
Copy
Edit
# .env.example

TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
BASE_URL=https://your-deployment-url.com
🧾 requirements.txt
txt
Copy
Edit
flask
python-dotenv
requests
👩‍❤️‍👩 Credits
Built by Vishnuraj CR
Inspired by late-night chats and emotional bestie moments.

📜 License
This project is licensed under the MIT License. Use it, remix it, and make someone smile.

“Sometimes all we need is a silly, sweet girl best friend who speaks in Manglish and tells us everything will be okay 😌”

yaml
Copy
Edit

---

You can now save this as `README.md` in your project folder. Let me know if you'd like me to generate the `.env.example`, `requirements.txt`, or push the project structure to GitHub for you.







