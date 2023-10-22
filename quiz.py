from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

class HomeScr(Screen):
    def __init__(self, **kwargs):
        super().init(**kwargs)
        lbl1 = Label(text='Викторина', halign='right', font_size = 25)
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5}, font_size = 20)
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.9, None), height='1000sp')
        line2 = BoxLayout(size_hint=(1, None), height='30sp')
        line1.add_widget(lbl1)
        line2.add_widget(self.btn)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line1)
        outer.add_widget(line2)
        self.add_widget(outer)

    def next(self):
        self.manager.current = 'quiz1'


class Incorrect(Screen):
    def __init__(self, **kwargs):
        super().init(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.results = Label(text = 'Это неверный ответ.')
        self.btn1 = Button(text='В начало', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn1.on_press = self.back
        self.outer.add_widget(self.results)
        self.outer.add_widget(self.btn1)
        self.add_widget(self.outer)
    def back(self):
        self.manager.current = 'firstpage1'
class QuizScr(Screen):
    def __init__(self, **kwargs):
        super().init(**kwargs)
        
        question1 = Label(text='Сколько хромосом у человека?')
        
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.in_result = TextInput(text='0', multiline=False)
        
        line.add_widget(question1)
        self.btn1 = Button(text='46', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn1.on_press = self.next
        self.btn2 = Button(text='23', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn2.on_press = self.incorrect
        self.btn3 = Button(text='48', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn3.on_press = self.incorrect
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line)
        outer.add_widget(self.btn1)
        outer.add_widget(self.btn2)
        outer.add_widget(self.btn3)
        self.add_widget(outer)
    
    def next(self):
        self.manager.current = 'quiz2'
    def incorrect(self):
        self.manager.current = 'incorrect'

class QuizScr2(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        
        question1 = Label(text='Кто убил Марка?')
        
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.in_result = TextInput(text='0', multiline=False)
        
        line.add_widget(question1)
        self.btn1 = Button(text='Секретная информация', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn1.on_press = self.incorrect
        self.btn2 = Button(text='Егор', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn2.on_press = self.next
        self.btn3 = Button(text='Эдуард', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn3.on_press = self.incorrect
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line)
        outer.add_widget(self.btn1)
        outer.add_widget(self.btn2)
        outer.add_widget(self.btn3)
        self.add_widget(outer)
    
    def next(self):
        self.manager.current = 'quiz3'
    def incorrect(self):
        self.manager.current = 'incorrect'

class QuizScr3(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        
        question1 = Label(text='Столица Исландии?')
        
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.in_result = TextInput(text='0', multiline=False)
        
        line.add_widget(question1)
        self.btn1 = Button(text='Варшава', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn1.on_press = self.incorrect
        self.btn2 = Button(text='Стокгольм', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn2.on_press = self.incorrect
        self.btn3 = Button(text='Рейкъявик', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn3.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line)
        outer.add_widget(self.btn1)
        outer.add_widget(self.btn2)
        outer.add_widget(self.btn3)
        self.add_widget(outer)
    
    def next(self):
        self.manager.current = 'quiz4'
    def incorrect(self):
        self.manager.current = 'incorrect'

class QuizScr4(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        
        question1 = Label(text='В чем сила, брат?')
        
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.in_result = TextInput(text='0', multiline=False)
        
        line.add_widget(question1)
        self.btn1 = Button(text='В друзьях', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn1.on_press = self.incorrect
        self.btn2 = Button(text='В семье', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn2.on_press = self.incorrect
        self.btn3 = Button(text='В Ньютонах', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn3.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line)
        outer.add_widget(self.btn1)
        outer.add_widget(self.btn2)
        outer.add_widget(self.btn3)
        self.add_widget(outer)
    def next(self):
        self.manager.current = 'resultend'
    def incorrect(self):
        self.manager.current = 'incorrect'

class Result(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.results = Label(text = '4/4, вот это мощь.')
        self.outer.add_widget(self.results)
        self.add_widget(self.outer)

class Strangequiz(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScr(name='firstpage1'))
        sm.add_widget(QuizScr(name='quiz1'))
        sm.add_widget(QuizScr2(name='quiz2'))
        sm.add_widget(QuizScr3(name='quiz3'))
        sm.add_widget(QuizScr4(name='quiz4'))
        sm.add_widget(Result(name='resultend'))
        sm.add_widget(Incorrect(name='incorrect'))

        return sm

app = Strangequiz()
app.run()