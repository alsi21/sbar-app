import classes
import CustomApp

from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from LocalStorage import STORE_NOTES, delete_data
from Encryption import encrypt
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class EmergSearchScreen(Screen):
    '''Screen class to handle emergency notes ,similiar to SbarScreen'''
    def max_length_text(self,text):
        """
        Every time text is written it checks the length to see if it's too long,
        if it is slice the last part of and override text of patientid
        """
        print(len(text))
        if len(text) > 24:
            text =text[:-1]
            self.ids.patientid.text = text
    def on_enter(self):
        '''
        Code that gets executed everytime screen gets displayed
        Checks if there exists a note with exact same content
        '''
        
        self.repeat = False
        #self.old_note = None
        self.old_toc = self.ids.toc_var.text
        self.old_id = self.ids.patientid.text
        self.old_situation = self.ids.situation.text
        self.old_background = self.ids.bakgrund.text
        # self.old_akt = self.ids.aktuellt.text
        self.old_safety = self.ids.safety.text
        self.old_air = self.ids.air.text
        self.old_bre = self.ids.breath.text
        self.old_circ = self.ids.circ.text
        self.old_deg = self.ids.deg.text
        self.old_exposure = self.ids.exposure.text
        self.old_rek = self.ids.reko.text
        self.old_extra = self.ids.extra.text
        for note in CustomApp.CustomApp.notes:
            if (
                self.old_id == note.patientid and
                self.old_situation == note.situation and
                self.old_background == note.background and
                # self.old_akt == note.relevant and
                self.old_safety == note.safety and
                self.old_air == note.airway and
                self.old_bre == note.breath and
                self.old_circ == note.circ and
                self.old_deg == note.disability and
                self.old_exposure == note.exposure and
                self.old_rek == note.recommendation and
                self.old_extra == note.extra
                ):
                print('found old note: ', note.patientid)
                self.old_note = note
                self.repeat = True
        note = self.old_note
        delete_data(STORE_NOTES, self.old_note.time_of_creation)
        self.auto_save = Clock.schedule_interval(self.quick_save, 2.5)

    def get_font_size(self):
        self.font_size = CustomApp.CustomApp.font_size
        return self.font_size

    def show_p_id(self):
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

    def show_situation(self):
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
    


    def show_bakgrund(self):
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
        


    def show_aktuellt(self):
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


    def show_airway(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Stabilisering av nacke?"
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="A - Fri luftväg", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()   


    def show_breathing(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Lyssna på lungor.\nAndningsrörelse."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="B - Syresättning, andningsfrekvens", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open()   

    def show_circulation(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Blodtryck, puls, kapillär återfyllnad, hudstatus."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="C - cirkulation", 
        content=text,
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open() 

    def show_disability(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Medvetande och neurologstatus, P-glukos."
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="D - Medvetande och neurologstatus", 
        content=text,   
        size_hint=(0.8, 0.5),
        title_size="30sp"
        )
        popup.open() 

    def show_exposure(self):
        """
        Code that excutes when you press on the text buttonsthat will show
        the user information about what should be written in each field.
        """
        msg = "Kroppsinspektion. \nVärm patienten om den är kall. \nEKG?"
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size=18)
        popup = Popup(title="E - Exponering", 
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
        text = TextInput(text=msg, multiline=True, readonly=True, height = 300, font_size='18dp')
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
        # aktuellt = self.ids.aktuellt.text
        s = self.ids.safety.text
        a = self.ids.air.text
        b = self.ids.breath.text
        c = self.ids.circ.text
        d = self.ids.deg.text
        e = self.ids.exposure.text
        communication = self.ids.communication.text
        breathing = self.ids.breathing.text
        circulation = self.ids.circulation.text
        elimination = self.ids.elimination.text
        pain = self.ids.pain.text
        activity = self.ids.activity.text
        sleep = self.ids.sleep.text
        psycho = self.ids.psycho.text
        rek = self.ids.reko.text
        extra = self.ids.extra.text

        if self.repeat:
            toc = self.old_note.time_of_creation
        else:
            toc = self.ids.toc_var.text

        note = classes.Note(
            patientid, situation, bakgrund,
            '', rek, extra, s, a, b, c, d,
            e, True, False, communication ,breathing, circulation, elimination,
              pain, activity, sleep, psycho, toc)
        
        if self.repeat and self.old_note:
            note.checked = self.old_note.checked
            note.timestamp = self.old_note.timestamp

        if self.repeat:
            if self.old_note:
                delete_data(STORE_NOTES, self.old_note.time_of_creation)
        if not note.is_empty():
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)

    def save_note(self):
        '''
        Code that gets executed when button is pressed to go to main menu
        Creates a note with current info and if it is not a previous note it gets put into list of notes
        changes to main menu
        '''

        patientid = self.ids.patientid.text
        situation = self.ids.situation.text
        bakgrund = self.ids.bakgrund.text
        # aktuellt = self.ids.aktuellt.text
        s = self.ids.safety.text
        a = self.ids.air.text
        b = self.ids.breath.text
        c = self.ids.circ.text
        d = self.ids.deg.text
        e = self.ids.exposure.text
        communication = self.ids.communication.text
        breathing = self.ids.breathing.text
        circulation = self.ids.circulation.text
        elimination = self.ids.elimination.text
        pain = self.ids.pain.text
        activity = self.ids.activity.text
        sleep = self.ids.sleep.text
        psycho = self.ids.psycho.text
        rek = self.ids.reko.text
        extra = self.ids.extra.text

        if self.repeat:
            toc = self.old_note.time_of_creation
        else:
            toc = self.ids.toc_var.text

        note = classes.Note(
            patientid, situation, bakgrund,
            '', rek, extra, s, a, b, c, d,
            e, True, False, communication ,breathing, circulation, elimination,
              pain, activity, sleep, psycho, toc)

        if self.repeat and self.old_note:
            note.checked = self.old_note.checked
            note.timestamp = self.old_note.timestamp

        # add the new note to the shared notes list
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
        # aktuellt = self.ids.aktuellt.text
        s = self.ids.safety.text
        a = self.ids.air.text
        b = self.ids.breath.text
        c = self.ids.circ.text
        d = self.ids.deg.text
        e = self.ids.exposure.text
        communication = self.ids.communication.text
        breathing = self.ids.breathing.text
        circulation = self.ids.circulation.text
        elimination = self.ids.elimination.text
        pain = self.ids.pain.text
        activity = self.ids.activity.text
        sleep = self.ids.sleep.text
        psycho = self.ids.psycho.text
        rek = self.ids.reko.text
        extra = self.ids.extra.text

        if self.repeat:
            toc = self.old_note.time_of_creation
        else:
            toc = self.ids.toc_var.text

        note = classes.Note(
            patientid, situation, bakgrund,
            '', rek, extra, s, a, b, c, d,
            e, True, False, communication ,breathing, circulation, elimination,
              pain, activity, sleep, psycho, toc)

        if self.repeat and self.old_note:
            note.checked = self.old_note.checked
            note.timestamp = self.old_note.timestamp

        if self.repeat:
            if self.old_note:
                delete_data(STORE_NOTES, self.old_note.time_of_creation)
        if not note.is_empty():
            note.export_note(local_storage=STORE_NOTES, encrypt_func=encrypt)

        Clock.unschedule(self.auto_save)
        self.manager.current = 'emerg'
        emerg_screen = self.manager.get_screen('emerg')
        emerg_screen.ids.patientid.text = note.patientid
        emerg_screen.ids.situation.text = note.situation
        emerg_screen.ids.bakgrund.text = note.background
        #emerg_screen.ids.aktuellt.text = note.relevant
        emerg_screen.ids.reko.text = note.recommendation
        emerg_screen.ids.extra.text = note.extra
        emerg_screen.ids.time_of_creation = note.time_of_creation
        emerg_screen.ids.communication.text = note.communication
        emerg_screen.ids.breathing.text = note.breathing
        emerg_screen.ids.circulation.text = note.circulation
        emerg_screen.ids.elimination.text = note.elimination
        emerg_screen.ids.pain.text = note.pain
        emerg_screen.ids.activity.text = note.activity
        emerg_screen.ids.sleep.text = note.sleep
        emerg_screen.ids.psycho.text = note.psycho
        emerg_screen.ids.safety.text = note.safety
        emerg_screen.ids.air.text = note.airway
        emerg_screen.ids.breath.text = note.breath
        emerg_screen.ids.circ.text = note.circ
        emerg_screen.ids.deg.text = note.disability
        emerg_screen.ids.exposure.text = note.exposure
