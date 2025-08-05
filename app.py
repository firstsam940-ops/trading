import streamlit as st
import random

st.set_page_config(page_title="Forex Signal App", page_icon="📈", layout="centered")

st.title("📊 Oscar Trade Bot")

# Валютные пары
forex_pairs = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'USD/CHF',
               'AUD/USD', 'NZD/USD', 'USD/CAD', 'EUR/GBP']

# Время экспирации
expiration_times = ['1 мин', '5 мин', '15 мин', '30 мин', '1 час']

pair = st.selectbox("Выбери валютную пару:", forex_pairs)
timeframe = st.selectbox("Выбери время экспирации:", expiration_times)

if st.button("🔍 Получить сигнал"):
    signal = random.choice(['📈 ВВЕРХ', '📉 ВНИЗ'])
    st.success(f"🎯 Сигнал: {signal}")
else:
    st.info("Нажми кнопку, чтобы получить сигнал")
