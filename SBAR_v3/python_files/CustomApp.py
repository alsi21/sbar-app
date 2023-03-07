import PinScreen
import SetScreen
import MainScreen
import SettingsScreen
import SbarScreen
import EmergScreen

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup



class MyScreenManager(ScreenManager):
    '''ScreenManager class'''
    pass

class CustomApp(App):
    '''App class, keeps track of notes'''
    notes = []

    def build(self):
        '''Build function that calls Screenmanager, 
        adds screens to it 
        and binds a popup window to when you attempt to close window'''
        sm = ScreenManager()
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
        self.TextPopup(title='Exit', text='Are you sure?')
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
