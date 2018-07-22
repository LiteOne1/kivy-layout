import kivy
#kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from engine.grab import get_synopsis, soup, soup1, get_rating, get_cast # import from external py file



Builder.load_file('kv/layout.kv')# load external kv file


class Film(BoxLayout):

    def get_syn(self):
        self.ids.synopsis.text = get_synopsis(soup)
        self.ids.cast.text = get_cast(soup1)




class FilmApp(App):
    def build(self):
        return Film()

if __name__ == '__main__':
    FilmApp().run()
