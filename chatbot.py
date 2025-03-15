import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Load Chatbot Model (DialoGPT)
@st.cache_resource
def load_chatbot():
    model_name = "microsoft/DialoGPT-small"
    chat_tokenizer = AutoTokenizer.from_pretrained(model_name)
    chat_model = AutoModelForCausalLM.from_pretrained(model_name)
    return chat_tokenizer, chat_model

chat_tokenizer, chat_model = load_chatbot()

# Load Sentiment Analysis Model (DistilBERT)
@st.cache_resource
def load_sentiment_analyzer():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiment_analyzer = load_sentiment_analyzer()

# Function to Generate Chatbot Response
def get_bot_reply(user_message):
    input_text = chat_tokenizer.encode(user_message + chat_tokenizer.eos_token, return_tensors="pt")  
    output_tokens = chat_model.generate(input_text, max_length=100, pad_token_id=chat_tokenizer.eos_token_id)  
    bot_reply = chat_tokenizer.decode(output_tokens[:, input_text.shape[-1]:][0], skip_special_tokens=True)  
    return bot_reply

# Function to Analyze Sentiment of Bot Response
def get_sentiment(response_text):
    result = sentiment_analyzer(response_text)
    return f"{result[0]['label']} (Confidence: {result[0]['score']:.2f})"

# Streamlit UI
st.title("🤖 Bro Bot: Sentiment Analyzer")
st.write("### Talk with an AI like your bro and see if its response is positive or negative!")

# User Input
st.subheader("💬 Chat with Bro Bot")
user_message = st.text_input("You:", "")  

if st.button("Send", use_container_width=True):  
    if user_message.strip():  
        bot_reply = get_bot_reply(user_message)  # Generate chatbot reply
        sentiment_result = get_sentiment(bot_reply)  # Analyze sentiment
        
        st.success(f"**Bro:** {bot_reply}")  
        st.info(f"**Bro's Sentiment:** {sentiment_result}")

st.markdown("---")

st.write("### 🚀 Want a response from ChatGPT instead?")
st.write("We've automated the process! Enter your prompt, and we'll get a precise answer from ChatGPT right here.")

user_prompt = st.text_input("🔍 Enter your prompt:")
if st.button("Ask ChatGPT", use_container_width=True):
    driver = webdriver.Chrome()
    driver.get("https://chatgpt.com/")
    time.sleep(5)

    try:
        search_box = driver.find_element(By.CLASS_NAME, "placeholder")
        search_box.send_keys(f"{user_prompt} answer in one line")
        search_box.send_keys(Keys.ENTER)
        
        # Wait for ChatGPT to respond
        time.sleep(10)
        response_paragraphs = driver.find_elements(By.XPATH, "//p")
        
        if response_paragraphs:
            chatgpt_reply = response_paragraphs[-1].text
            if chatgpt_reply=="":
                chatgpt_reply=get_bot_reply(user_prompt)  #if error occurs then your own bot replies
                st.success(f"**ChatGPT:** {chatgpt_reply}")
        else:
            st.error("❌ Couldn't fetch ChatGPT's response. Try again!")
    except Exception as error:
        st.error(f"⚠️ Oops! Something went wrong: {error}")
    
    driver.quit()
