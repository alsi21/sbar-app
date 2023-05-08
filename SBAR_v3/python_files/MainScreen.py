import time
import CustomApp
import classes

from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.app import App
from kivy.metrics import dp

from LocalStorage import STORE_NOTES, delete_data
from Encryption import encrypt

NOTE_HEIGTH = (dp(80) + 10) # +10 because of spacing and bottom padding.

class MainScreen(Screen):
    '''Screen class for main menu'''

    def on_enter(self):
        '''
        Code that gets executed whenever screen is showed,
        Adds graphical main menu note representation for each note
        '''
        #Change transition to slide to left
        self.manager.transition = SlideTransition(direction='left')
        # clear any existing buttons
        self.ids.label_layout.clear_widgets()
        # add a button for each note
        # Resets scroll-view height. Set to 10 to take top padding into account.
        self.ids.label_layout.height = 10

        # Removes notes flagged as timed out.
        del_index = [] # List for storing index of notes to delete.
        for index, note in enumerate(CustomApp.CustomApp.notes):
            if note.timed_out(3):
                del_index.append(index)
                delete_data(STORE_NOTES, note.time_of_creation)

        # Loop backwards to prevent out-of-bound pops.
        for index in del_index[::-1]:
            CustomApp.CustomApp.notes.pop(index)

        for note in CustomApp.CustomApp.notes[::-1]:
            # Calculates new scroll-view height from note count.
            self.ids.label_layout.height += NOTE_HEIGTH
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
                    
            full_widget.ids.buttonone.text = note.patientid + '      ' + note.time_of_creation
            button_note = note  # create a new variable with the value of note
            full_widget.ids.buttonone.bind(on_press=lambda instance, button_note=button_note: self.edit_note(instance, button_note))
            full_widget.ids.checkbox.bind(on_press=lambda instance, button_note=button_note: self.check_note(instance, button_note))
            self.ids.label_layout.add_widget(full_widget)
            full_widget.ids.buttonone.note = note
    
    def get_font_size(self):
        self.font_size = CustomApp.CustomApp.font_size
        return self.font_size

    def check_note(self, instance, note):
        ''' 
        Toggles the checked state for a SBAR Note
        '''
        state = note.checked
        note.checked = not state
        self.manager.current = 'main'
        if note.checked:
            CustomApp.CustomApp.notes.remove(note)
            self.delete_note(note)
            CustomApp.CustomApp.notes.insert(0, note)
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)
        else:
            CustomApp.CustomApp.notes.remove(note)
            self.delete_note(note)
            CustomApp.CustomApp.notes.append(note)
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)
            
        self.on_enter()


    def delete_note(self, note):
        '''Deletes Note from Local Storage'''
        delete_data(STORE_NOTES, note.time_of_creation)            

    def edit_note(self, instance, note):
        '''
        Executed when entering already saved note,
        Checks if it is sbar note or emergency note, 
        depending on type save different note values
        '''
        if not note.emergency:
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
            emerg_screen.ids.situation.text = note.situation
            emerg_screen.ids.bakgrund.text = note.background
            # emerg_screen.ids.aktuellt.text = note.relevant
            emerg_screen.ids.safety.text = note.safety
            emerg_screen.ids.air.text = note.airway
            emerg_screen.ids.breath.text = note.breath
            emerg_screen.ids.circ.text = note.circ
            emerg_screen.ids.deg.text = note.disability
            emerg_screen.ids.exposure.text = note.exposure
            emerg_screen.ids.reko.text = note.recommendation
            emerg_screen.ids.extra.text = note.extra
            emerg_screen.ids.time_of_creation = note.time_of_creation

    def add_sbar(self):
        '''
        Enters SbarScreen and clears any existing text, 
        not saved til save button is pressed on SbarScreen
        '''
        self.ids.label_layout.height += NOTE_HEIGTH* self.get_font_size()
        self.manager.current = 'sbar'
        sbar_screen = self.manager.get_screen('sbar')
        sbar_screen.ids.patientid.text = ''
        sbar_screen.ids.situation.text = ''
        sbar_screen.ids.bakgrund.text = ''
        sbar_screen.ids.aktuellt.text = ''
        sbar_screen.ids.rekomendation.text = ''
        sbar_screen.ids.extra.text = ''
        sbar_screen.ids.toc_var.text = time.strftime('%d/%m    %H:%M:%S')
        

    def add_emerg(self):
        '''
        Enters EmergScreen and clears any existing text, 
        not saved til save button is pressed on EmergScreen
        '''
        self.ids.label_layout.height += NOTE_HEIGTH* self.get_font_size()
        self.manager.current = 'emerg'
        emerg_screen = self.manager.get_screen('emerg')
        emerg_screen.ids.patientid.text = ''
        emerg_screen.ids.situation.text = ''
        emerg_screen.ids.bakgrund.text = ''
        # emerg_screen.ids.aktuellt.text = ''
        emerg_screen.ids.safety.text = ''
        emerg_screen.ids.air.text = ''
        emerg_screen.ids.breath.text = ''
        emerg_screen.ids.circ.text = ''
        emerg_screen.ids.deg.text = ''
        emerg_screen.ids.exposure.text = ''
        emerg_screen.ids.reko.text = ''
        emerg_screen.ids.extra.text = ''
        emerg_screen.ids.toc_var.text = time.strftime('%d/%m    %H:%M:%S')

    def go_to_settings(self):
        '''Simple function to go to SettingsScreen'''
        self.manager.current = 'settings' 

    def go_to_sbar(self):
        '''Simple function to go to SBAR'''
        self.manager.current = 'sbar'
    
    def change_transition(self):
        self.manager.transition = NoTransition()
    