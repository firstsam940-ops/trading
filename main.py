from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import random


class TradingApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.pair_spinner = Spinner(
            text='Выбери валютную пару',
            values=('EUR/USD', 'BTC/USDT', 'ETH/USDT'),
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.pair_spinner)

        self.time_spinner = Spinner(
            text='Выбери время экспирации',
            values=('15 сек', '30 сек', '1 мин', '5 мин', '15 мин'),
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.time_spinner)

        self.result_label = Label(text='🎯 Сигнал появится здесь', font_size=20)
        self.add_widget(self.result_label)

        self.signal_button = Button(text='Получить сигнал', size_hint=(1, None), height=50)
        self.signal_button.bind(on_press=self.start_timer)
        self.add_widget(self.signal_button)

        self.timer_event = None
        self.remaining_seconds = 0

    def start_timer(self, instance):
        time_text = self.time_spinner.text

        time_mapping = {
            '15 сек': 15,
            '30 сек': 30,
            '1 мин': 60,
            '5 мин': 300,
            '15 мин': 900
        }

        if time_text not in time_mapping:
            self.result_label.text = '❌ Выбери корректное время!'
            return

        self.remaining_seconds = time_mapping[time_text]
        self.result_label.text = f'⏳ Ожидаем {self.remaining_seconds} сек...'
        self.signal_button.disabled = True

        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.remaining_seconds -= 1
        if self.remaining_seconds <= 0:
            Clock.unschedule(self.timer_event)
            self.show_signal()
        else:
            self.result_label.text = f'⏳ Осталось: {self.remaining_seconds} сек'

    def show_signal(self):
        signal = random.choice(['📈 ВВЕРХ', '📉 ВНИЗ'])
        self.result_label.text = f'🎯 Сигнал: {signal}'
        self.signal_button.disabled = False


class TradingSignalApp(App):
    def build(self):
        return TradingApp()


if __name__ == '__main__':
    TradingSignalApp().run()
