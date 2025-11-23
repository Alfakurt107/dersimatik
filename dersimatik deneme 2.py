from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout



class Plan(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        layout = FloatLayout()
        label2 = Label(text="Süre:", size_hint=(0.2, 0.2), pos_hint={"center_x":0.2, "center_y":0.3})
        label3 = Label(text="mola:", size_hint=(0.2, 0.2), pos_hint={"center_x":0.2, "center_y":0.1})
        geri1 = Button(text="geri", size_hint=(0.1, 0.1), pos_hint={"center_x":0.1, "center_y":0.9})
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(geri1)


class Notlar(Screen):
    pass

class Bot(Screen):
    pass

class Tablo(Screen):
    layout = FloatLayout()
    label4 = Label(text="En yüksek:", size_hint=(0.2, 0.1), pos_hint={"center_x":0.2, "center_y":0.3})
    label5 = Label(text="En düşük:", size_hint=(0.2, 0.1), pos_hint={"center_x":0.2, "center_y":0.2})
    label6 = Label(text="Başarı(%):", size_hint=(0.2, 0.1), pos_hint={"center_x":0.2, "center_y":0.1})
    button15 = Button(text="geri", size_hint=(0.1, 0.1), pos_hint={"center_x":0.1, "center_y":0.9})
    layout.add_widget(label4)
    layout.add_widget(label5)
    layout.add_widget(label6)
    layout.add_widget(button15)


class Ders(Screen):
    def build(self):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.cols = 1
            layout = FloatLayout()
            matematik = Button(text="Matematik", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.8})
            turkce = Button(text="Türkçe", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.8})
            fen = Button(text="Fen", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.6})
            sosyal = Button(text="Sosyal", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.6})
            din = Button(text="Din", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.4})
            yabanci_dil = Button(text="Yabancı Dil", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.4})
            #button12 = Button(text="", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.2})
            #button13 = Button(text="", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.2})
            geri2 = Button(text="geri", size_hint=(0.1, 0.1), pos_hint={"center_x":0.1, "center_y":0.9})

            layout.add_widget(matematik)
            layout.add_widget(turkce)
            layout.add_widget(fen)
            layout.add_widget(sosyal)
            layout.add_widget(din)
            layout.add_widget(yabanci_dil)
            #layout.add_widget(button12)
            #layout.add_widget(button13)
            layout.add_widget(geri2)

class Dersimatik(App):
    def build(self):
        layout = FloatLayout()
        label1 = Label(text="Dersimatik", size_hint=(0.5, 0.3), pos_hint={"center_x":0.5, "center_y":0.9})
        plan = Button(text="Plan", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.7})
        ders = Button(text="Ders", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.7})
        notlar = Button(text="Notlar", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.3, "center_y": 0.5})
        bot = Button(text="Bot", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.7, "center_y": 0.5})
        tablo = Button(text="Tablo", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.3})
        
        layout.add_widget(label1)
        layout.add_widget(plan)
        layout.add_widget(ders)
        layout.add_widget(notlar)
        layout.add_widget(bot)
        layout.add_widget(tablo)

        self.screen_manager = ScreenManager()

        self.plan = Plan()
        screen = Screen(name="Plan")
        screen.add_widget(self.plan)
        self.screen_manager.add_widget(screen)
        

        self.ders = Ders()
        screen = Screen(name="Ders")
        screen.add_widget(self.ders)
        self.screen_manager.add_widget(screen)
        
        return layout


if __name__=="__main__":
    Dersimatik().run()