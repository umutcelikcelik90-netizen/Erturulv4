from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import urllib.request

class ArcomaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text="Kablosuz ağa bağlanılıyor...", size_hint_y=None, height=50)
        self.layout.add_widget(self.label)
        self.text_input = TextInput(hint_text="Buraya istediğin yazıyı yazabilirsin...", multiline=True)
        self.layout.add_widget(self.text_input)
        self.check_network()
        return self.layout

    def check_network(self, *args):
        try:
            urllib.request.urlopen('http://www.google.com', timeout=4)
            self.label.text = "Successfully"
        except:
            self.label.text = "Bağlantı başarısız, tekrar deneniyor..."
            from kivy.clock import Clock
            Clock.schedule_once(self.check_network, 3)

if __name__ == '__main__':
    ArcomaApp().run()
