from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.core.window import Window
import random

# Устанавливаем фон приложения
Window.clearcolor = (0.1, 0.1, 0.1, 1)  # тёмно-серый фон

# Форекс валютные пары
FOREX_PAIRS = (
    'EUR/USD', 'GBP/USD', 'USD/JPY', 'USD/CHF',
    'AUD/USD', 'NZD/USD', 'USD/CAD', 'EUR/GBP',
)

EXPIRATION_TIMES = (
    '1 мин', '5 мин', '15 мин', '30 мин', '1 час',
)

class TradingApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        # Заголовок
        self.title_label = Label(
            text='📊 Трейдинг Бот',
            font_size=32,
            size_hint=(1, None),
            height=60,
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.title_label)

        # Выбор валютной пары
        self.pair_spinner = Spinner(
            text='Выбери валютную пару',
            values=FOREX_PAIRS,
            size_hint=(1, None),
            height=50,
            background_color=(0.3, 0.3, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size=18
        )
        self.add_widget(self.pair_spinner)

        # Выбор времени экспирации
        self.time_spinner = Spinner(
            text='Выбери время экспирации',
            values=EXPIRATION_TIMES,
            size_hint=(1, None),
            height=50,
            background_color=(0.3, 0.3, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size=18
        )
        self.add_widget(self.time_spinner)

        # Результат сигнала
        self.result_label = Label(
            text='🎯 Сигнал появится здесь',
            font_size=24,
            size_hint=(1, None),
            height=60,
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.result_label)

        # Кнопка получить сигнал
        self.signal_button = Button(
            text='🔍 Получить сигнал',
            size_hint=(1, None),
            height=60,
            background_color=(0.2, 0.6, 0.2, 1),
            font_size=20,
            color=(1, 1, 1, 1)
        )
        self.signal_button.bind(on_press=self.get_signal)
        self.add_widget(self.signal_button)

        # Пустое место внизу
        self.add_widget(Widget())

    def get_signal(self, instance):
        signal = random.choice(['📈 ВВЕРХ', '📉 ВНИЗ'])
        self.result_label.text = f'🎯 Сигнал: {signal}'


class TradingSignalApp(App):
    def build(self):
        self.title = 'Forex Signal App'
        return TradingApp()


if __name__ == '__main__':
    TradingSignalApp().run()
