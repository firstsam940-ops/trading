import streamlit as st
import time
import random

st.title("📈 AI OSCAR BOT")

if "button_pressed" not in st.session_state:
    st.session_state.button_pressed = False

# Полный список популярных валютных пар Форекс
forex_pairs = [
    'EUR/USD', 'USD/JPY', 'GBP/USD', 'USD/CHF', 'AUD/USD', 'USD/CAD',
    'NZD/USD', 'EUR/GBP', 'EUR/JPY', 'GBP/JPY', 'CHF/JPY', 'EUR/AUD',
    'AUD/JPY', 'CAD/JPY', 'NZD/JPY', 'GBP/CAD', 'EUR/CAD', 'AUD/CAD',
    'NZD/CAD', 'USD/SEK', 'USD/NOK', 'USD/DKK', 'EUR/NZD', 'GBP/NZD',
    'AUD/NZD', 'EUR/CHF', 'GBP/CHF', 'AUD/CHF'
]

pair = st.selectbox("Выбери валютную пару:", forex_pairs)

expiration_times = ["15 сек", "30 сек", "1 мин", "3 мин", "5 мин"]
expiration = st.selectbox("Время экспирации:", expiration_times)

def press_button():
    st.session_state.button_pressed = True

if st.button("Получить сигнал", on_click=press_button):
    pass

if st.session_state.button_pressed:
    placeholder = st.empty()
    placeholder.info("🤖 Думаю...")

    # Имитация задержки "думания" 3 секунды
    for i in range(3):
        time.sleep(1)
        placeholder.info(f"🤖 Думаю{'.' * ((i + 1) % 4)}")

    signal = random.choice(["📈 ВВЕРХ", "📉 ВНИЗ"])
    placeholder.success(f"🎯 Сигнал для {pair} на {expiration}: {signal}")

    st.session_state.button_pressed = False
