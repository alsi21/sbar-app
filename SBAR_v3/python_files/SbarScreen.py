import classes
import CustomApp

from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
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



    def show_p_id(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Patient ID är ditt val av namn på patienten. Kom ihåg att inte använda riktiga namn, använd istället tex ett alias eller patientens rumsnummer."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="Patient ID", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()



    def show_situation(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Situation är kärnan i det som ska förmedlas och ska fungera som en kortfattad rubrik för att fånga mottagarens uppmärksamhet. Här presenterar sändaren sig själv och vem det gäller."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="Situation", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()
    


    def show_bakgrund(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Bakgrunden beskriver det relevanta för den aktuella situationen. Vid akuta tillfällen hinner man bara beskriva det allra viktigaste. Icke akuta situationer kan innehålla mer information."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="Bakgrund", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()    
        


    def show_aktuellt(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Aktuell bedömning beskriver den aktuella situationen som ska förmedlas. Använd gärna ABCDE för att strukturera patienternas vitalstatus. Berätta om eventuella åtgärder och resultat av dessa. Förmedla din bedömning av den aktuella situationen."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="Aktuellt", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()   
    


    def show_rekommendation(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Rekommendation eller varför du tagit kontakt och vad mottagaren ska göra. Klargör för dig själv vad mottagaren förväntas göra utifrån det som rapporterats under Situation, Bakgrund och Aktuellt, samt inom vilken tid du anser att det ska göras."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="Rekommendation", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()    
        
        
    
    def show_extra_notes(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Här skriver du själv dina egna anteckningar utöver SBAR om du vill."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="Extra notering", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()



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
        if not note.is_empty():
            CustomApp.CustomApp.notes.append(note)
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)
        self.manager.current = 'main'

