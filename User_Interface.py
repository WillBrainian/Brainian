import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.lang import Builder
import speech_To_Text as st


class Wills_Website_Blocker(App):
    def build(self):
        self.icon = "me.png"
        #self.theme_cls.theme_style
        #self.theme_cls.primary_palette ="BlueGray"
        #self.uix
        #return Builder.load_file("Login.kv")
        return Label(text="hello proggggg")
    st.read_My_file()


    
if __name__=="__main__":
        Wills_Website_Blocker().run()
