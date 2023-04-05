import PinScreen
import SetScreen
import MainScreen
import SettingsScreen
import SbarScreen
import EmergScreen

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from LocalStorage import STORE_NOTES, serialize_notes

class MyScreenManager(ScreenManager):
    '''ScreenManager class'''
    # def transition(self, screen, direction):
    #     if screen.name == 'sbar' or screen.name == 'emerg':
    #         self.transition = SlideTransition(direction = 'right')
    #     elif screen.name == 'pin' or screen.name == 'set' or screen.name == 'main' or screen.name == 'settings':
    #         self.transition = SlideTransition(direction = 'left')
    #     else:
    #         self.transition = SlideTransition(direction = 'up')
    pass

class CustomApp(App):
    '''App class, keeps track of notes'''
    notes = serialize_notes(STORE_NOTES)

    def build(self):
        '''Build function that calls Screenmanager, 
        adds screens to it 
        and binds a popup window to when you attempt to close window'''
        sm = ScreenManager(transition = SlideTransition())
        sm.add_widget(PinScreen.PinScreen(name='pin'))
        sm.add_widget(SetScreen.SetScreen(name='set'))
        sm.add_widget(MainScreen.MainScreen(name='main'))  
        sm.add_widget(SettingsScreen.SettingsScreen(name='settings'))
        sm.add_widget(SbarScreen.SbarScreen(name='sbar'))
        sm.add_widget(EmergScreen.EmergScreen(name='emerg'))
        Window.bind(on_request_close=self.on_request_close)
        return sm

    def on_request_close(self, *args):
        '''Function to call TextPopup'''
        #Save here
        self.TextPopup(title='Avsltuta', text='Är du säker på att du vill avsluta?')
        return True

    def TextPopup(self, title='', text=''):
        '''Function to create a popup boxlayout with a button in it'''
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        mybutton = Button(text='OK', size_hint=(1, 0.25))
        box.add_widget(mybutton)
        popup = Popup(title=title, content=box, size_hint=(None, None), size=(600, 300))
        mybutton.bind(on_release=self.stop)
        popup.open()
