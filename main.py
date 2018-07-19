import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.stacklayout import StackLayout
from engine.grab import get_synopsis, soup # import from external py file


Builder.load_file('kv/layout.kv')# load external kv file


class Film(BoxLayout):
    def get_syn(self): 
        x = get_synopsis(soup)
        self.ids.movie_description.text = x


class FilmApp(App):
    def build(self):
        return Film()

if __name__ == '__main__':
    FilmApp().run()
