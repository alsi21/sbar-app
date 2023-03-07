from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty, Clock, StringProperty
from kivy.app import App

class SetScreen(Screen):
    pin = ''
    text = StringProperty('Set code(4)')
    set_code = ''
    check = ''
    def on_button1_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '1'
        self.text += '1'
        
    def on_button2_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '2'
        self.text += '2'

    def on_button3_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '3'
        self.text += '3'
    
    def on_button4_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '4'
        self.text += '4'
    
    def on_button5_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '5'
        self.text += '5'
    
    def on_button6_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '6'
        self.text += '6'
    
    def on_button7_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '7'
        self.text += '7'
    
    def on_button8_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '8'
        self.text += '8'
    
    def on_button9_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '9'
        self.text += '9'
    
    def on_button0_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin += '0'
        self.text += '0'
    
    def on_buttondel_press(self):
        if len(self.text) > 5:
            self.text = ''
        self.pin = self.pin[:-1]
        self.text = self.text[:-1]

    def update_text(self):
        if len(self.pin) >3 and self.check == self.pin:
            # Switch to the next screen
            self.text = 'OK'
            app = App.get_running_app()
            second_screen = app.root.get_screen('pin')
            second_screen.set_set_code(self.pin)
            self.manager.current = 'main'

        elif len(self.pin) >3:
            self.check = self.pin
            self.pin = ''
            self.text = 'Again:'