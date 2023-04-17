import CustomApp

from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *

from datetime import datetime

class SquareBlueButton(Button):
    '''Blue button'''

class SBARNoteCheckBox(CheckBox):
    '''Note CheckBsox'''

class BlueTextInput(TextInput):
    '''Blue TextInput'''


class Note:
    '''Class that holds information presented in notes'''

    def __init__(self, patientid, situation, background, relevant, recommendation, extra, airway, breath, circ, disability, exposure, emergency, checked, time_of_creation, timestamp = None):
        '''
        Parameters
        ----------
        patientid : str
            The name assigned to patient
        situation : str
            Info about patient situation
        background : str
            The name assigned to patient
        relevant : str
            Relevant info about patient
        recommendation : str
            Recommendations for patient
        extra : str
            Extra information about patient
        airway : str
            Any information about patient airway
        breath : str
            patient breathing
        circ : str
            patient circulation
        disability : str
            patient disability
        exposure : str
            patient exposure
        emergency : Bool
            Value to see if the note is an emergency note
        '''
        #For SBAR and Emerg
        self.patientid = patientid
        self.relevant = relevant
        self.recommendation = recommendation
        #Only for SBAR
        self.situation = situation
        self.background = background
        self.extra = extra
        #Only for Emerg
        self.airway = airway
        self.breath = breath
        self.circ = circ
        self.disability = disability
        self.exposure = exposure
        self.emergency = emergency
        self.checked = checked

        self.time_of_creation = time_of_creation

        # Timestamp used for auto-deletion.
        if timestamp == None:
            timestamp = datetime.now()
        self.timestamp = timestamp
        print(f'Created new note with timestamp: {timestamp}.')

    def is_empty(self):
        '''Returns whether the note is empty.'''
        return not (
        self.patientid or
        self.situation or
        self.background or
        self.relevant or
        self.recommendation or
        self.airway or
        self.breath or
        self.circ or
        self.disability or
        self.exposure or
        self.extra
        )

    def export_note(self, local_storage, encrypt_func):
        '''Exports SBAR Note to Local Storage'''
        local_storage.put(
            encrypt_func(self.patientid + self.time_of_creation),
            patientid = encrypt_func(self.patientid),
            situation = encrypt_func(self.situation),
            background = encrypt_func(self.background),
            relevant = encrypt_func(self.relevant),
            recommendation = encrypt_func(self.recommendation),
            extra = encrypt_func(self.extra),
            airway = encrypt_func(self.airway),
            breath = encrypt_func(self.breath),
            circ = encrypt_func(self.circ),
            disability = encrypt_func(self.disability),
            exposure = encrypt_func(self.exposure),
            emergency = self.emergency,
            checked = self.checked,
            time_of_creation = encrypt_func(self.time_of_creation),
            timestamp = encrypt_func(self.timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        )

    def timed_out(self, hours: int) -> bool:
        now = datetime.now()
        # temporarily set to 1 instead of 3600
        return (now - self.timestamp).total_seconds() > (hours * 60)


class SbarNote(BoxLayout):
    '''Mainscreen Sbar note handling'''

    def __init__(self, **kwargs):
        '''Builds note in mainmenu'''
        super().__init__(**kwargs)
        box = BoxLayout(orientation='horizontal', size_hint_y=None, height=80)
        main_btn = Button(size_hint_x=.8)
        box.add_widget(main_btn)
        checkbox = SBARNoteCheckBox(active=False, size_hint_x=.2)
        checkbox.bind(on_press=self.on_checkbox_active)
        box.add_widget(checkbox)

    def on_checkbox_active(self, checkbox):
        '''CheckBox Interaction'''
        if not checkbox.active:
            print('The checkbox', self, 'is active')
            self.ids.buttonone.background_color = 0,0,0,0.02
        else:
            print('The checkbox', self, 'is inactive')
            self.ids.buttonone.background_color = 0,0,0,0.15

class EmergNote(BoxLayout):
    '''Mainscreen Emerg note handling'''

    def on_checkbox_active(self, checkbox):
        '''CheckBox Interaction'''
        if not checkbox.active:
            print('The checkbox', self, 'is active')
            self.ids.buttonone.background_color = 0,0,0,0.02
        else:
            print('The checkbox', self, 'is inactive')
            self.ids.buttonone.background_color = 0,0,0,0.15
