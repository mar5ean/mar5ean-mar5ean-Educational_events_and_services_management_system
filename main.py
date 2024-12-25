import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from functools import partial

# Импортируем функции для работы с базой данных
import db

# Классы экрана
class EventScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Кнопка для возвращения
        self.back_button = Button(text="Назад", size_hint=(1, 0.1), font_size=18, background_normal='', background_color=(0.3, 0.5, 0.7, 1))
        self.back_button.bind(on_press=self.back_to_main)
        self.layout.add_widget(self.back_button)

        # Заголовок
        self.label = Label(text="Список мероприятий", size_hint=(1, 0.1), font_size=24, color=(0.1, 0.5, 0.7, 1), bold=True)
        self.layout.add_widget(self.label)

        # Прокручиваемая область
        self.scroll_view = ScrollView()
        self.event_list_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.event_list_layout.bind(minimum_height=self.event_list_layout.setter('height'))

        # Загружаем мероприятия
        self.load_events()

        self.scroll_view.add_widget(self.event_list_layout)
        self.layout.add_widget(self.scroll_view)
        self.add_widget(self.layout)

    def load_events(self):
        # Получаем список мероприятий из базы данных
        events = db.load_events()

        for event in events:
            event_button = Button(text=event[1], size_hint_y=None, height=40, font_size=18, background_normal='', background_color=(0.6, 0.7, 1, 1), color=(0, 0, 0, 1))
            event_button.bind(on_press=partial(self.show_event_details, event))
            self.event_list_layout.add_widget(event_button)

    def show_event_details(self, event, instance):
        # Переход на экран с деталями
        self.manager.current = 'event_details'
        self.manager.get_screen('event_details').show_event(event)

    def back_to_main(self, instance):
        self.manager.current = 'main'

class EventDetailsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Кнопка назад
        self.back_button = Button(text="Назад", size_hint=(1, 0.1), font_size=18, background_normal='', background_color=(0.3, 0.5, 0.7, 1))
        self.back_button.bind(on_press=self.back_to_events)
        self.layout.add_widget(self.back_button)

        # Место для отображения деталей
        self.details_label = Label(text="Детали мероприятия", size_hint=(1, 0.9), font_size=20, color=(0.1, 0.5, 0.7, 1))
        self.layout.add_widget(self.details_label)

        self.add_widget(self.layout)

    def show_event(self, event):
        # Обновление текста с деталями мероприятия
        event_details = f"Название: {event[1]}\nОписание: {event[2]}\nДата: {event[3]}\nМесто: {event[4]}"
        self.details_label.text = event_details

    def back_to_events(self, instance):
        self.manager.current = 'events'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Добро пожаловать в систему управления мероприятиями", size_hint=(1, 0.1), font_size=24, color=(0.1, 0.5, 0.7, 1), bold=True)
        self.layout.add_widget(self.label)

        self.event_button = Button(text="Список мероприятий", size_hint=(1, 0.2), font_size=18, background_normal='', background_color=(0.6, 0.7, 1, 1))
        self.event_button.bind(on_press=self.go_to_events)
        self.layout.add_widget(self.event_button)

        self.add_widget(self.layout)

    def go_to_events(self, instance):
        self.manager.current = 'events'

class EventApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(EventScreen(name='events'))
        self.sm.add_widget(EventDetailsScreen(name='event_details'))
        return self.sm


if __name__ == '__main__':
    db.create_db()  # Создание базы данных
    EventApp().run()
