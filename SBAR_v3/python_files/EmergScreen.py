import classes
import CustomApp

from kivy.uix.screenmanager import ScreenManager, Screen
from LocalStorage import STORE_NOTES
from Encryption import encrypt

class EmergScreen(Screen):
    '''Screen class to handle emergency notes ,similiar to SbarScreen'''

    def on_enter(self):
        '''
        Code that gets executed everytime screen gets displayed
        Checks if there exists a note with exact same content
        '''
        self.repeat = False
        if self.ids.patientid.text:
            self.old_toc = self.ids.toc_var.text
            self.old_id = self.ids.patientid.text
            self.old_akt = self.ids.aktuellt.text
            self.old_air = self.ids.air.text
            self.old_bre = self.ids.breath.text
            self.old_circ = self.ids.circ.text
            self.old_deg = self.ids.deg.text
            self.old_rek = self.ids.reko.text
            for note in CustomApp.CustomApp.notes:
                if self.old_id == note.patientid and self.old_akt == note.relevant and self.old_air == note.airway and self.old_bre == note.breath and self.old_circ == note.circ and self.old_deg == note.disability and self.old_rek == note.recommendation:
                    self.repeat = True
                    self.old_note = note

    def save_note(self):
        '''
        Code that gets executed when button is pressed to go to main menu
        Creates a note with current info and if it is not a previous note it gets put into list of notes
        changes to main menu
        '''
        patientid = self.ids.patientid.text
        aktuellt = self.ids.aktuellt.text
        d = self.ids.deg.text
        c = self.ids.circ.text
        b = self.ids.breath.text
        a = self.ids.air.text
        rek = self.ids.reko.text
        toc = self.ids.toc_var.text
        note = classes.Note(patientid, '', '', aktuellt, rek, '',a,b,c,d, True, False, toc)
        if self.repeat and self.old_note:
            note.checked = self.old_note.checked
        note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)
        # add the new note to the shared notes list
        if self.repeat:
            if self.old_note:
                CustomApp.CustomApp.notes.remove(self.old_note)
        if patientid or aktuellt or a or b or c or d or rek:
            CustomApp.CustomApp.notes.append(note)
        self.manager.current = 'main'
