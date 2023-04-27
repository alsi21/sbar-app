import CustomApp
import classes

from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.slider import Slider
from LocalStorage import STORE_SETTINGS
class SettingsScreen(Screen):
    '''
    Screen class for settings,
    exist to set settings buttons to functions and make import into App easier
    '''
    def on_enter(self):
        # clear any existing buttons
        self.ids.label_layout.clear_widgets()
        # add a button for each note
        for note in CustomApp.CustomApp.notes[::-1]:
            if note.emergency:
                full_widget = classes.EmergNote()
                if note.checked:
                    full_widget.ids.buttonone.background_color = 0,0,0,0.15
                    full_widget.ids.checkbox.active = True
            else:
                full_widget = classes.SbarNote()
                if note.checked:
                    full_widget.ids.buttonone.background_color = 0,0,0,0.15
                    full_widget.ids.checkbox.active = True
                    
            full_widget.ids.buttonone.text = note.patientid + '        ' + note.time_of_creation
            button_note = note  # create a new variable with the value of note
            # full_widget.ids.buttonone.bind(on_press=lambda instance, button_note=button_note: self.edit_note(instance, button_note))
            # full_widget.ids.checkbox.bind(on_press=lambda instance, button_note=button_note: self.check_note(instance, button_note))
            self.ids.label_layout.add_widget(full_widget)
            full_widget.ids.buttonone.note = note

    def go_main(self, *args):
        app = CustomApp.CustomApp.get_running_app()
        app.reload_screens()

    def get_font_size(self):
        self.font_size = CustomApp.CustomApp.font_size
        return self.font_size

    def go_to_help(self):
        self.manager.current = "help"

    def go_to_manual(self):
        self.manager.current = "manual"

    def change_font(self, font_size):
        CustomApp.CustomApp.font_size = round(font_size,1)
        print(CustomApp.CustomApp.font_size)
        STORE_SETTINGS.put('font_size', font = CustomApp.CustomApp.font_size)

        
