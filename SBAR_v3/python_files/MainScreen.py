from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
import time
import CustomApp
import classes

class MainScreen(Screen):
    def on_enter(self):
        print('entering')
        # clear any existing buttons
        self.ids.label_layout.clear_widgets()
        # add a button for each note
        print(len(CustomApp.CustomApp.notes))
        for note in CustomApp.CustomApp.notes[::-1]:
            if note.exposure:
                full_widget = classes.EmergNote()
            else:
                full_widget = classes.SbarNote()
            full_widget.ids.buttonone.text = note.patientid + '        ' + note.time_of_creation
            button_note = note  # create a new variable with the value of note
            full_widget.ids.buttonone.bind(on_press=lambda instance, button_note=button_note: self.edit_note(instance, button_note))
            self.ids.label_layout.add_widget(full_widget)
            full_widget.ids.buttonone.note = note
            

    def edit_note(self, instance, note):
        if not note.emerg:
            self.manager.current = 'sbar'
            print('note patientid: ',note.patientid)
            sbar_screen = self.manager.get_screen('sbar')
            sbar_screen.ids.patientid.text = note.patientid
            sbar_screen.ids.situation.text = note.situation
            sbar_screen.ids.bakgrund.text = note.bakgrund
            sbar_screen.ids.aktuellt.text = note.aktuellt
            sbar_screen.ids.rekomendation.text = note.rekomendation
            sbar_screen.ids.extra.text = note.extra
            sbar_screen.ids.time_of_creation = note.time_of_creation
            print(sbar_screen.ids.patientid.text)            
        else:
            self.manager.current = 'emerg'
            emerg_screen = self.manager.get_screen('emerg')
            emerg_screen.ids.patientid.text = note.patientid
            emerg_screen.ids.aktuellt.text = note.aktuellt
            emerg_screen.ids.air.text = note.airway
            emerg_screen.ids.breath.text = note.breath
            emerg_screen.ids.circ.text = note.circ
            emerg_screen.ids.deg.text = note.deg
            emerg_screen.ids.reko.text = note.rekomendation
            emerg_screen.ids.time_of_creation = note.time_of_creation

    def add_sbar(self):
        self.ids.label_layout.height += 90
        self.manager.current = 'sbar'
        sbar_screen = self.manager.get_screen('sbar')
        sbar_screen.ids.patientid.text = ''
        sbar_screen.ids.situation.text = ''
        sbar_screen.ids.bakgrund.text = ''
        sbar_screen.ids.aktuellt.text = ''
        sbar_screen.ids.rekomendation.text = ''
        sbar_screen.ids.extra.text = ''
        sbar_screen.ids.toc_var.text = time.strftime('[%d/%m]    [%H:%M:%S]')
        

    def add_emerg(self):
        self.ids.label_layout.height += 90
        self.manager.current = 'emerg'
        emerg_screen = self.manager.get_screen('emerg')
        emerg_screen.ids.patientid.text = ''
        emerg_screen.ids.aktuellt.text = ''
        emerg_screen.ids.air.text = ''
        emerg_screen.ids.breath.text = ''
        emerg_screen.ids.circ.text = ''
        emerg_screen.ids.deg.text = ''
        emerg_screen.ids.reko.text = ''
        emerg_screen.ids.toc_var.text = time.strftime('[%d/%m]    [%H:%M:%S]')

    def go_to_settings(self):
        self.manager.current = 'settings' 

    def go_to_sbar(self):
        self.manager.current = 'sbar'