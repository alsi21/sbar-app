import CustomApp
import classes

from kivy.uix.screenmanager import Screen
from kivy.animation import Animation

class SettingsScreen(Screen):
    '''
    Screen class for settings,
    exist to set settings buttons to functions and make import into App easier
    '''
    def on_enter(self):
        self.ids.label_layout.clear_widgets()
        for note in CustomApp.CustomApp.notes[::-1]:
                if note.exposure:
                    full_widget = classes.EmergNote()
                else:
                    full_widget = classes.SbarNote()
                full_widget.ids.buttonone.text = note.patientid + '        ' + note.time_of_creation
                button_note = note  # create a new variable with the value of note
                full_widget.ids.buttonone.bind(on_press=lambda instance, button_note=button_note: self.edit_note(instance, button_note))
                full_widget.ids.deletebutton.bind(on_press=lambda instance, button_note=button_note: self.delete_note(instance, button_note))
                self.ids.label_layout.add_widget(full_widget)
                full_widget.ids.buttonone.note = note