from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import BooleanProperty, Clock, StringProperty

from LocalStorage import STORE_PIN, serialize_pin

class PinScreen(Screen):
    '''
    Screen class for when there is a pincode set
    pin : str
        Attempted code
    text : str
        Text in label
    set_code : str
        Already set code to compare against'''
    pin = ''
    text = StringProperty('Pin:')
    set_code = serialize_pin(STORE_PIN)

    def on_button1_press(self):
        self.pin += '1'
        self.text += '*'
        
    def on_button2_press(self):
        self.pin += '2'
        self.text += '*'

    def on_button3_press(self):
        self.pin += '3'
        self.text += '*'
    
    def on_button4_press(self):
        self.pin += '4'
        self.text += '*'
    
    def on_button5_press(self):
        self.pin += '5'
        self.text += '*'
    
    def on_button6_press(self):
        self.pin += '6'
        self.text += '*'
    
    def on_button7_press(self):
        self.pin += '7'
        self.text += '*'
    
    def on_button8_press(self):
        self.pin += '8'
        self.text += '*'
    
    def on_button9_press(self):
        self.pin += '9'
        self.text += '*'
    
    def on_button0_press(self):
        self.pin += '0'
        self.text += '*'
    
    def on_buttondel_press(self):
        self.pin = self.pin[:-1]
        self.text = self.text[:-1]

    def update_text(self):
        '''
        # Checks if there is a set code, if not switch to SetScreen 
        If 4 numbers have been entered, check to see if code is correct
        Else clear attempted code and label'''
        # if not self.set_code:
        #     self.manager.current = 'set'

        if len(self.pin) >3 and self.pin == self.set_code:
            # Switch to the next screen
            self.manager.current = 'main'
        elif len(self.pin) >3:
            self.text = ''
            self.pin = ''

    def set_set_code(self,code):
        '''Sets the code to attempt against'''
        self.set_code = code
        self.pin = ''
        self.text = ''

    def on_enter(self):
        '''
        Executed when entering screen,
        Gives a delay of .1 seconds to check if there is a code set, 
        '''
        Clock.schedule_once(self.check_password, .1)
        
    def check_password(self, *args):
        '''If no password is set, switch to SetScreen'''
        if not self.set_code:
            self.manager.current = 'set'
