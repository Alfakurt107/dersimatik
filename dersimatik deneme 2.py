from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
from kivy.uix.image import Image
from kivy.core.window import Window

#turkce_not_deg = NumericProperty(0)

class Plan(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        label2 = Label(text="Süre:", size_hint=(0.2, 0.2), pos_hint={"center_x":0.2, "center_y":0.3})
        label3 = Label(text="mola:", size_hint=(0.2, 0.2), pos_hint={"center_x":0.2, "center_y":0.1})
        geri1 = Button(text="geri", size_hint=(0.1, 0.1), pos_hint={"center_x":0.1, "center_y":0.9})
        geri1.bind(on_release=lambda x: setattr(screen_manager, "current", "Menu"))
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(geri1)
        self.add_widget(layout)

class Notlar(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        label1 = Label(text="Türkçe", size_hint=(0.1,0.1), pos_hint={"center_x":0.1, "center_y":0.7})
        label2 = Label(text="Matematik", size_hint=(0.1,0.1), pos_hint={"center_x":0.1, "center_y":0.6})
        label3 = Label(text="Fen", size_hint=(0.1,0.1), pos_hint={"center_x":0.1, "center_y":0.5})
        label4 = Label(text="Sosyal", size_hint=(0.1,0.1), pos_hint={"center_x":0.1, "center_y":0.4})
        label5 = Label(text="Din", size_hint=(0.1,0.1), pos_hint={"center_x":0.1, "center_y":0.3})
        label6 = Label(text="Yabancı Dil", size_hint=(0.1,0.1), pos_hint={"center_x":0.1, "center_y":0.2})
        geri = Button(text="geri", size_hint=(0.1, 0.1), pos_hint={"center_x":0.1, "center_y":0.9})
        turkce_not = Label(text="turkce_not_deg", size_hint=(0.1,0.1), pos_hint={"center_x":0.2, "center_y":0.7})
        self.turkce_not_deg = TextInput(text="")

        geri.bind(on_release=lambda x: setattr(screen_manager, "current", "Menu"))
        
        #if(101 > turkce_not_deg > -4):
        #    layout.add_widget(turkce_not)
        #else:
        #    layout.add_widget(self.turkce_not_deg)
        
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        layout.add_widget(label5)
        layout.add_widget(label6)
        layout.add_widget(geri)
        self.add_widget(layout)

class Bot(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        label = Label(text="Bot", size_hint=(0.3,0.2), pos_hint={"center_x":0.5, "center_y":0.5})
        geri = Button(text="geri", size_hint=(0.1, 0.1), pos_hint={"center_x":0.1, "center_y":0.9})
        geri.bind(on_release=lambda x: setattr(screen_manager, "current", "Menu"))
        layout.add_widget(label)
        layout.add_widget(geri)
        self.add_widget(layout)

class Tablo(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        label4 = Label(text="En yüksek:", size_hint=(0.2, 0.1), pos_hint={"center_x":0.2, "center_y":0.3})
        label5 = Label(text="En düşük:", size_hint=(0.2, 0.1), pos_hint={"center_x":0.2, "center_y":0.2})
        label6 = Label(text="Başarı(%):", size_hint=(0.2, 0.1), pos_hint={"center_x":0.2, "center_y":0.1})
        button15 = Button(text="geri", size_hint=(0.1, 0.1), pos_hint={"center_x":0.1, "center_y":0.9})
        button15.bind(on_release=lambda x: setattr(screen_manager, "current", "Menu"))
        layout.add_widget(label4)
        layout.add_widget(label5)
        layout.add_widget(label6)
        layout.add_widget(button15)
        self.add_widget(layout)

class Ders(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        matematik = Button(text="Matematik", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.8})
        turkce = Button(text="Türkçe", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.8})
        fen = Button(text="Fen", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.6})
        sosyal = Button(text="Sosyal", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.6})
        din = Button(text="Din", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.4})
        yabanci_dil = Button(text="Yabancı Dil", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.4})
        geri2 = Button(text="geri", size_hint=(0.1, 0.1), pos_hint={"center_x":0.1, "center_y":0.9})
        geri2.bind(on_release=lambda x: setattr(screen_manager, "current", "Menu"))

        layout.add_widget(matematik)
        layout.add_widget(turkce)
        layout.add_widget(fen)
        layout.add_widget(sosyal)
        layout.add_widget(din)
        layout.add_widget(yabanci_dil)
        layout.add_widget(geri2)
        self.add_widget(layout)
        

class MenuScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        label1 = Label(text="Dersimatik", size_hint=(0.5, 0.3), pos_hint={"center_x":0.5, "center_y":0.9})
        plan = Button(text="Plan", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.7})
        ders = Button(text="Ders", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.7})
        notlar = Button(text="Notlar", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.5})
        bot = Button(text="Bot", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.5})
        tablo = Button(text="Tablo", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.3})
        plan.bind(on_release=lambda x: setattr(screen_manager, "current", "Plan"))
        ders.bind(on_release=lambda x: setattr(screen_manager, "current", "Ders"))
        notlar.bind(on_release=lambda x: setattr(screen_manager, "current", "Notlar"))
        bot.bind(on_release=lambda x: setattr(screen_manager, "current", "Bot"))
        tablo.bind(on_release=lambda x: setattr(screen_manager, "current", "Tablo"))
        layout.add_widget(label1)
        layout.add_widget(plan)
        layout.add_widget(ders)
        layout.add_widget(notlar)
        layout.add_widget(bot)
        layout.add_widget(tablo)
        self.add_widget(layout)


class Dersimatik(App):

    
    def build(self):
        self.screen_manager = ScreenManager(transition=SlideTransition())
        self.screen_manager.add_widget(MenuScreen(self.screen_manager, name="Menu"))
        self.screen_manager.add_widget(Plan(self.screen_manager, name="Plan"))
        self.screen_manager.add_widget(Ders(self.screen_manager, name="Ders"))
        self.screen_manager.add_widget(Notlar(self.screen_manager, name="Notlar"))
        self.screen_manager.add_widget(Bot(self.screen_manager, name="Bot"))
        self.screen_manager.add_widget(Tablo(self.screen_manager, name="Tablo"))
        self.screen_manager.current = "Menu"
        
        return self.screen_manager

if __name__ == "__main__":
    Dersimatik().run()
