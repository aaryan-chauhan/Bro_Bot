# Bro Bot & ChatGPT Automation

This project is a chatbot with sentiment analysis and also an auto tool for asking ChatGPT for answer. It is made using Streamlit for UI, DialoGPT for chatting, and Selenium for web automation.

## 📌 Features
- **Chat with Bro Bot** - A chatbot that reply to your text.
- **Sentiment Analysis** - It checks if bot's reply is positive or negative.
- **ChatGPT Auto Ask** - You enter prompt, it go to ChatGPT website and get answer for you.

## 🚀 How It Work
1. User type message and click "Send", then Bro Bot reply.
2. Bro Bot's reply is check for positive or negative.
3. If user want ChatGPT answer, they enter prompt and click "Ask ChatGPT".
4. Selenium open ChatGPT website, enter prompt, and get last answer.
5. If ChatGPT fail, then Bro Bot will reply instead.

## 🛠️ Tech Used
- **Streamlit** - For web UI
- **DialoGPT** - AI chatbot model
- **DistilBERT** - Sentiment analysis
- **Selenium** - Web automation
- **Python** - Main language

## 📥 Install & Run
1. Install required libraries:
   ```sh
   pip install streamlit transformers torch selenium
   ```
2. Run the script:
   ```sh
   streamlit run your_script.py
   ```
3. Open the link in browser.

## 🔥 Notes
- You need **Chrome WebDriver** installed for Selenium to work.
- ChatGPT site layout may change, which can break automation.
- Bro Bot is a small model, so replies may not be perfect.

Enjoy chatting with your bro bot! 🤖🔥

