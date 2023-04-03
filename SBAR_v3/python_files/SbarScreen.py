import classes
import CustomApp

from kivy.uix.screenmanager import ScreenManager, Screen
from LocalStorage import STORE_NOTES, delete_data
from Encryption import encrypt

class SbarScreen(Screen):
    '''Screen class to handle Sbar notes ,similiar to EmergScreen'''

    def on_enter(self):
        '''
        Code that gets executed everytime screen gets displayed
        Checks if there exists a note with exact same content
        '''
        self.repeat = False
        self.old_note = None
        self.old_toc = self.ids.toc_var.text
        self.old_id = self.ids.patientid.text
        self.old_sit = self.ids.situation.text
        self.old_bak = self.ids.bakgrund.text
        self.old_akt = self.ids.aktuellt.text
        self.old_rek = self.ids.rekomendation.text
        self.old_ext = self.ids.extra.text
        for note in CustomApp.CustomApp.notes:
            if (
                self.old_id == note.patientid and
                self.old_sit == note.situation and
                self.old_bak == note.background and
                self.old_akt == note.relevant and
                self.old_rek == note.recommendation and
                self.old_ext == note.extra
                ):
                print('found old note: ', note.patientid)
                self.old_note = note
                self.repeat = True

    def save_note(self):
        '''
        Code that gets executed when button is pressed to go to main menu
        Creates a note with current info and if it is not a previous note it gets put into list of notes
        changes to main menu
        '''
        patientid = self.ids.patientid.text
        situation = self.ids.situation.text
        bakgrund = self.ids.bakgrund.text
        aktuellt = self.ids.aktuellt.text
        rekomendation = self.ids.rekomendation.text
        extra = self.ids.extra.text

        if self.repeat:
            toc = self.old_note.time_of_creation
        else:
            toc = self.ids.toc_var.text

        note = classes.Note(patientid, situation, bakgrund, aktuellt, rekomendation, extra, '', '', '', '', '', False, False, toc)

        if self.repeat and self.old_note:
            note.checked = self.old_note.checked

        if self.repeat:
            if self.old_note:
                CustomApp.CustomApp.notes.remove(self.old_note)
                delete_data(STORE_NOTES, self.old_note.patientid, self.old_note.time_of_creation)
        if patientid or self.repeat:
            CustomApp.CustomApp.notes.append(note)
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)
        self.manager.current = 'main'

