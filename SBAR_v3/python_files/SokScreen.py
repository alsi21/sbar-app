import classes
import CustomApp

from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from LocalStorage import STORE_NOTES, delete_data
from Encryption import encrypt
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.utils import platform

class SokScreen(Screen):
    '''Screen class to handle Sbar notes ,similiar to EmergScreen'''
    def on_enter(self):
        '''
        Code that gets executed everytime screen gets displayed
        Checks if there exists communication note with exact same content
        '''
        if platform ==  "android":
            Window.bind(on_keyboard_height=self.on_keyboard_height)
        self.repeat = False
        #self.old_note = None
        self.old_toc = self.ids.toc_var.text
        self.old_id = self.ids.patientid.text
        self.old_sit = self.ids.situation.text
        self.old_bak = self.ids.bakgrund.text
        self.old_akt = self.ids.aktuellt.text
        self.old_rek = self.ids.rekomendation.text
        self.old_ext = self.ids.extra.text
        self.old_a = self.ids.communication.text
        self.old_b = self.ids.breathing.text
        self.old_c = self.ids.circulation.text
        self.old_d = self.ids.elimination.text
        self.old_e = self.ids.pain.text
        self.old_f = self.ids.activity.text
        self.old_g = self.ids.sleep.text
        self.old_h = self.ids.psycho.text
        for note in CustomApp.CustomApp.notes:
            if (
                self.old_id == note.patientid and
                self.old_sit == note.situation and
                self.old_bak == note.background and
                self.old_akt == note.relevant and
                self.old_rek == note.recommendation and
                self.old_ext == note.extra and
                self.old_a == note.communication and
                self.old_b == note.breathing and
                self.old_c == note.circulation and
                self.old_d == note.elimination and
                self.old_e == note.pain and
                self.old_f == note.activity and
                self.old_g == note.sleep and
                self.old_h == note.psycho
                ):
                print('found old note: ', note.patientid)
                self.old_note = note
                self.repeat = True
        note = self.old_note
        delete_data(STORE_NOTES, self.old_note.time_of_creation)
        # for i in CustomApp.CustomApp.notes:
        #     if note == i:
        #         CustomApp.CustomApp.notes.remove(i)
        # self.old_note = classes.Note(self.ids.patientid.text, self.ids.situation.text, self.ids.bakgrund.text,
        #                         self.ids.aktuellt.text, self.ids.rekomendation.text, self.ids.extra.text, '', '', '','', 
        #                         '','', False, False, self.ids.communication.text,
        #                         self.ids.breathing.text, self.ids.circulation.text, self.ids.elimination.text, self.ids.pain.text, self.ids.activity.text, self.ids.toc_var.text)

        self.auto_save = Clock.schedule_interval(self.quick_save, 2.5)
    
    def get_font_size(self):
        self.font_size = CustomApp.CustomApp.font_size
        return self.font_size

    def on_keyboard_height(self,window,keyboard_height):
        if keyboard_height > 0:
            self.ids.whitespace.height = keyboard_height
            self.ids.ScrollBox.height = self.ids.ScrollBox.minimum_height
        else:
            self.ids.whitespace.height = 0
            self.ids.ScrollBox.height = self.ids.ScrollBox.minimum_height

    def max_length_text(self,text):
        """
        Every time text is written it checks the length to see if it's too long,
        if it is slice the last part of and override text of patientid
        """
        print(len(text))
        if len(text) > 24:
            text =text[:-1]
            self.ids.patientid.text = text

    def show_com(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Patient ID är ditt val av namn på patienten. Kom ihåg att inte använda riktiga namn, använd istället tex ett alias eller patientens rumsnummer."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
        popup = Popup(title="Patient ID", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()

    def show_breath(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Situation är kärnan i det som ska förmedlas och ska fungera som en kortfattad rubrik för att fånga mottagarens uppmärksamhet. Här presenterar sändaren sig själv och vem det gäller."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
        popup = Popup(title="Situation", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()

    def show_circ(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Bakgrunden beskriver det relevanta för den aktuella situationen. Vid akuta tillfällen hinner man bara beskriva det allra viktigaste. Icke akuta situationer kan innehålla mer information."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
        popup = Popup(title="Bakgrund", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()    

    def show_elim(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Aktuell bedömning beskriver den aktuella situationen som ska förmedlas. Använd gärna ABCDE för att strukturera patienternas vitalstatus. Berätta om eventuella åtgärder och resultat av dessa. Förmedla din bedömning av den aktuella situationen."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
        popup = Popup(title="Aktuellt", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()   

    def show_pain(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Rekommendation eller varför du tagit kontakt och vad mottagaren ska göra. Klargör för dig själv vad mottagaren förväntas göra utifrån det som rapporterats under Situation, Bakgrund och Aktuellt, samt inom vilken tid du anser att det ska göras."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
        popup = Popup(title="Rekommendation", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()    

    def show_activity(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Här skriver du själv dina egna anteckningar utöver SBAR om du vill."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
        popup = Popup(title="Extra notering", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()

    def show_sleep(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Här skriver du själv dina egna anteckningar utöver SBAR om du vill."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
        popup = Popup(title="Extra notering", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()

    def show_psycho(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Här skriver du själv dina egna anteckningar utöver SBAR om du vill."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
        popup = Popup(title="Extra notering", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()

    def quick_save(self, dt):
        patientid = self.ids.patientid.text
        situation = self.ids.situation.text
        bakgrund = self.ids.bakgrund.text
        aktuellt = self.ids.aktuellt.text
        rekomendation = self.ids.rekomendation.text
        extra = self.ids.extra.text
        communication = self.ids.communication.text
        breathing = self.ids.breathing.text
        circulation = self.ids.circulation.text
        elimination = self.ids.elimination.text
        pain = self.ids.pain.text
        activity = self.ids.activity.text
        sleep = self.ids.sleep.text
        psycho = self.ids.psycho.text

        if self.repeat:
            toc = self.old_note.time_of_creation
        else:
            toc = self.ids.toc_var.text
        

        note = classes.Note(
            patientid, situation, bakgrund,
            aktuellt, rekomendation, extra,
            '', '', '', '', '', '', 
            False, False, communication, breathing, circulation, elimination , pain, activity, sleep, psycho, toc)
        
        if self.repeat and self.old_note:
            note.checked = self.old_note.checked
            note.timestamp = self.old_note.timestamp

        # if( self.old_id == note.patientid and
        #     self.old_sit == note.situation and
        #     self.old_bak == note.background and
        #     self.old_akt == note.relevant and
        #     self.old_rek == note.recommendation and
        #     self.old_ext == note.extra
        #    ):
        #     if self.old_note:
        #         delete_data(STORE_NOTES, self.old_note.time_of_creation)
        
        if self.repeat:
            if self.old_note:
                delete_data(STORE_NOTES, self.old_note.time_of_creation)
        if not note.is_empty():
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)

    def save_note(self):
        '''
        Code that gets executed when button is pressed to go to main menu
        Creates communication note with current info and if it is not communication previous note it gets put into list of notes
        changes to main menu
        '''
        patientid = self.ids.patientid.text
        situation = self.ids.situation.text
        bakgrund = self.ids.bakgrund.text
        aktuellt = self.ids.aktuellt.text
        rekomendation = self.ids.rekomendation.text
        extra = self.ids.extra.text
        communication = self.ids.communication.text
        breathing = self.ids.breathing.text
        circulation = self.ids.circulation.text
        elimination = self.ids.elimination.text
        pain = self.ids.pain.text
        activity = self.ids.activity.text
        sleep = self.ids.sleep.text
        psycho = self.ids.psycho.text

        if self.repeat:
            toc = self.old_note.time_of_creation
        else:
            toc = self.ids.toc_var.text

        note = classes.Note(
            patientid, situation, bakgrund,
            aktuellt, rekomendation, extra,
            '', '', '', '', '', '', 
            False, False, communication, breathing, circulation, 
            elimination, pain, activity, sleep, psycho, toc)

        if self.repeat and self.old_note:
            note.checked = self.old_note.checked
            note.timestamp = self.old_note.timestamp

        if self.repeat:
            if self.old_note:
                CustomApp.CustomApp.notes.remove(self.old_note)
                delete_data(STORE_NOTES, self.old_note.time_of_creation)


        if not note.is_empty():
            CustomApp.CustomApp.notes.append(note)
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)

        for note in CustomApp.CustomApp.notes:
            for note2 in CustomApp.CustomApp.notes:
                if note != note2:
                    if note.time_of_creation == note2.time_of_creation:
                        CustomApp.CustomApp.notes.remove(note)
                        break

        Clock.unschedule(self.auto_save)
        self.manager.current = 'main'


    def to_sbar(self):
        patientid = self.ids.patientid.text
        situation = self.ids.situation.text
        bakgrund = self.ids.bakgrund.text
        aktuellt = self.ids.aktuellt.text
        rekomendation = self.ids.rekomendation.text
        extra = self.ids.extra.text
        communication = self.ids.communication.text
        breathing = self.ids.breathing.text
        circulation = self.ids.circulation.text
        elimination = self.ids.elimination.text
        pain = self.ids.pain.text
        activity = self.ids.activity.text
        sleep = self.ids.sleep.text
        psycho = self.ids.psycho.text

        if self.repeat:
            toc = self.old_note.time_of_creation
        else:
            toc = self.ids.toc_var.text

        note = classes.Note(
            patientid, situation, bakgrund,
            aktuellt, rekomendation, extra,
            '', '', '', '', '', '', 
            False, False, communication, breathing, circulation, elimination, pain, activity, sleep, psycho, toc)
        
        if self.repeat and self.old_note:
            note.checked = self.old_note.checked
            note.timestamp = self.old_note.timestamp

        if self.repeat:
            if self.old_note:
                delete_data(STORE_NOTES, self.old_note.time_of_creation)
        if not note.is_empty():
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)
            
        Clock.unschedule(self.auto_save)
        self.manager.current = 'sbar'
        #print('note patientid: ',note.patientid)
        sbar_screen = self.manager.get_screen('sbar')
        sbar_screen.ids.patientid.text = note.patientid
        sbar_screen.ids.situation.text = note.situation
        sbar_screen.ids.bakgrund.text = note.background
        sbar_screen.ids.aktuellt.text = note.relevant
        sbar_screen.ids.rekomendation.text = note.recommendation
        sbar_screen.ids.extra.text = note.extra
        sbar_screen.ids.time_of_creation = note.time_of_creation
        sbar_screen.ids.communication.text = note.communication
        sbar_screen.ids.breathing.text = note.breathing
        sbar_screen.ids.circulation.text = note.circulation
        sbar_screen.ids.elimination.text = note.elimination
        sbar_screen.ids.pain.text = note.pain
        sbar_screen.ids.activity.text = note.activity
        sbar_screen.ids.sleep.text = note.sleep
        sbar_screen.ids.psycho.text = note.psycho