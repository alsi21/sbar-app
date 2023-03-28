import time
import CustomApp
import classes

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

from LocalStorage import STORE_NOTES, delete_data
from Encryption import encrypt

class MainScreen(Screen):
    '''Screen class for main menu'''

    def on_enter(self):
        '''
        Code that gets executed whenever screen is showed,
        Adds graphical main menu note representation for each note'''
        blue = 217/255,225/255,1,1
        checked_blue = 108/255,112/255,0.5,1
        red = 227/255,210/255,210/255,1
        checked_red = 113/255,105/255,105/255,1

        # clear any existing buttons
        self.ids.label_layout.clear_widgets()
        # add a button for each note
        for note in CustomApp.CustomApp.notes[::-1]:
            if note.exposure:
                full_widget = classes.EmergNote()
                if note.checked:
                    full_widget.ids.rgba = checked_red
                    full_widget.ids.checkbox.active = note.checked
                    print('ecr')
                else:
                    full_widget.ids.rgba = red
                    full_widget.ids.checkbox.active = note.checked
                    print('er')

            else:
                full_widget = classes.SbarNote()
                if note.checked:
                    print('cb')
                    full_widget.ids.rgba = checked_blue
                    full_widget.ids.checkbox.active = note.checked
                else:
                    print('b')
                    full_widget.ids.rgba = blue
                    full_widget.ids.checkbox.active = note.checked
                    
            full_widget.ids.buttonone.text = note.patientid + '        ' + note.time_of_creation
            button_note = note  # create a new variable with the value of note
            full_widget.ids.buttonone.bind(on_press=lambda instance, button_note=button_note: self.edit_note(instance, button_note))
            full_widget.ids.checkbox.bind(on_press=lambda instance, button_note=button_note: self.check_note(instance, button_note))
            self.ids.label_layout.add_widget(full_widget)
            full_widget.ids.buttonone.note = note

    def check_note(self, instance, note):
        state = note.checked
        note.checked = not state
        note.export_note(STORE_NOTES, encrypt)
        self.manager.current = 'main'

    def delete_note(self, instance, note):
        delete_data(STORE_NOTES, note.patientid + note.time_of_creation)            

    def edit_note(self, instance, note):
        '''
        Executed when entering already saved note,
        Checks if it is sbar note or emergency note, 
        depending on type save different note values
        '''
        if not note.exposure:
            self.manager.current = 'sbar'
            print('note patientid: ',note.patientid)
            sbar_screen = self.manager.get_screen('sbar')
            sbar_screen.ids.patientid.text = note.patientid
            sbar_screen.ids.situation.text = note.situation
            sbar_screen.ids.bakgrund.text = note.background
            sbar_screen.ids.aktuellt.text = note.relevant
            sbar_screen.ids.rekomendation.text = note.recommendation
            sbar_screen.ids.extra.text = note.extra
            sbar_screen.ids.time_of_creation = note.time_of_creation
            print(sbar_screen.ids.patientid.text)            
        else:
            self.manager.current = 'emerg'
            emerg_screen = self.manager.get_screen('emerg')
            emerg_screen.ids.patientid.text = note.patientid
            emerg_screen.ids.aktuellt.text = note.relevant
            emerg_screen.ids.air.text = note.airway
            emerg_screen.ids.breath.text = note.breath
            emerg_screen.ids.circ.text = note.circ
            emerg_screen.ids.deg.text = note.disability
            emerg_screen.ids.reko.text = note.recommendation
            emerg_screen.ids.time_of_creation = note.time_of_creation

    def add_sbar(self):
        '''
        Enters SbarScreen and clears any existing text, 
        not saved til save button is pressed on SbarScreen
        '''
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
        '''
        Enters EmergScreen and clears any existing text, 
        not saved til save button is pressed on EmergScreen
        '''
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
        '''Simple function to go to SettingsScreen'''
        self.manager.current = 'settings' 

    def go_to_sbar(self):
        '''Simple function to go to SBAR'''
        self.manager.current = 'sbar'