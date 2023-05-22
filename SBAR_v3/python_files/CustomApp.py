import PinScreen
import SetScreen
import MainScreen
import SettingsScreen
import SbarScreen
import EmergScreen
import ManualScreen
import HelpScreen
import SokScreen
import EmergSearchScreen

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from LocalStorage import STORE_NOTES, serialize_notes
from LocalStorage import STORE_SETTINGS, get_font
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
    font_size = get_font(STORE_SETTINGS)
    sm = ScreenManager(transition = SlideTransition())
    def build(self):
        '''
        Build function that calls Screenmanager, 
        adds screens to it 
        and binds a popup window to when you attempt to close window'''
        self.sm.add_widget(PinScreen.PinScreen(name='pin'))
        self.sm.add_widget(SetScreen.SetScreen(name='set'))
        self.sm.add_widget(MainScreen.MainScreen(name='main'))  
        self.sm.add_widget(SettingsScreen.SettingsScreen(name='settings'))
        self.sm.add_widget(SbarScreen.SbarScreen(name='sbar'))
        self.sm.add_widget(EmergScreen.EmergScreen(name='emerg'))
        self.sm.add_widget(HelpScreen.HelpScreen(name='help'))
        self.sm.add_widget(ManualScreen.ManualScreen(name='manual'))
        self.sm.add_widget(SokScreen.SokScreen(name='search'))
        self.sm.add_widget(EmergSearchScreen.EmergSearchScreen(name='emergsearch'))
        Window.bind(on_request_close=self.on_request_close)
        return self.sm

    def on_request_close(self, *args, **kwargs):
        '''Function to call TextPopup'''
        #Save here
        # self.TextPopup(title='Avsluta', text='Vill du avsluta?')
        print('Called on_request_close.')
        self.stop()
        return True
    
    def android_back(self, window, key, *largs):
        if key == 27:
            # self.TextPopup(title='Avsluta', text='Vill du avsluta?')
            print(key)
            print('Pressed android back.')
            self.stop()
            return True
    
    def on_stop(self):
        print('Closing window.')
        Window.close()

    def reload_screens(self, screen_name,*args):
        '''
        removes all screens, then adds them back to refresh font size
        '''
        print('reloading screen')
        #sm = ScreenManager()
        self.sm.clear_widgets()
        self.sm.add_widget(MainScreen.MainScreen(name='main'))  
        self.sm.add_widget(PinScreen.PinScreen(name='pin'))
        self.sm.add_widget(SetScreen.SetScreen(name='set'))
        self.sm.add_widget(SettingsScreen.SettingsScreen(name='settings'))
        self.sm.add_widget(SbarScreen.SbarScreen(name='sbar'))
        self.sm.add_widget(EmergScreen.EmergScreen(name='emerg'))
        self.sm.add_widget(HelpScreen.HelpScreen(name='help'))
        self.sm.add_widget(ManualScreen.ManualScreen(name='manual'))
        self.sm.add_widget(SokScreen.SokScreen(name='search'))
        self.sm.add_widget(EmergSearchScreen.EmergSearchScreen(name='emergsearch'))
        self.sm.transition = SlideTransition()
        self.sm.current = screen_name

        # self.sm.clear_widgets()
        # self.sm.add_widget(MainScreen.MainScreen(name='main'))  
        # self.sm.add_widget(PinScreen.PinScreen(name='pin'))
        # self.sm.add_widget(SetScreen.SetScreen(name='set'))
        # self.sm.add_widget(SettingsScreen.SettingsScreen(name='settings'))
        # self.sm.add_widget(SbarScreen.SbarScreen(name='sbar'))
        # self.sm.add_widget(EmergScreen.EmergScreen(name='emerg'))
        # self.sm.add_widget(HelpScreen.HelpScreen(name='help'))
        # self.sm.add_widget(ManualScreen.ManualScreen(name='manual'))
        # self.sm.transition = NoTransition()
        # self.sm.current = screen_name

    def TextPopup(self, title='', text=''):
        '''
        Function to create a popup boxlayout with a button in it
        '''
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        btn_wrapper = BoxLayout(orientation='horizontal', size_hint=(1, 0.25))
        btn_exit = Button(text='Ja', size_hint=(0.5, 1), halign='center')
        btn_stay = Button(text='Nej', size_hint=(0.5, 1), halign='center')
        btn_wrapper.add_widget(btn_exit)
        btn_wrapper.add_widget(btn_stay)
        box.add_widget(btn_wrapper)
        self.popup = Popup(title=title, content=box, size_hint=(None, None), size=(600, 300))
        self.popup.open()
        btn_exit.bind(on_release=self.stop)
        btn_stay.bind(on_release=self.popup.dismiss)
