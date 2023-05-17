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

    def __init__(
            self, patientid, situation, background,
            relevant, recommendation, extra, safety, airway,
            breath, circ, disability, exposure, emergency,
            checked, communication, breathing, circulation, elimination, pain, activity, sleep, psycho, time_of_creation, timestamp = None):
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
        self.safety = safety
        self.airway = airway
        self.breath = breath
        self.circ = circ
        self.disability = disability
        self.exposure = exposure
        self.emergency = emergency
        self.checked = checked
        #Search
        self.communication = communication
        self.breathing = breathing
        self.circulation = circulation
        self.elimination = elimination
        self.pain = pain
        self.activity = activity
        self.sleep = sleep
        self.psycho = psycho
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
        self.safety or
        self.airway or
        self.breath or
        self.circ or
        self.disability or
        self.exposure or
        self.extra)

    def export_note(self, local_storage, encrypt_func):
        '''Exports SBAR Note to Local Storage'''
        local_storage.put(
            encrypt_func(self.time_of_creation),
            patientid = encrypt_func(self.patientid),
            situation = encrypt_func(self.situation),
            background = encrypt_func(self.background),
            relevant = encrypt_func(self.relevant),
            recommendation = encrypt_func(self.recommendation),
            extra = encrypt_func(self.extra),
            safety = encrypt_func(self.safety),
            airway = encrypt_func(self.airway),
            breath = encrypt_func(self.breath),
            circ = encrypt_func(self.circ),
            disability = encrypt_func(self.disability),
            exposure = encrypt_func(self.exposure),
            emergency = self.emergency,
            checked = self.checked,
            communication = encrypt_func(self.communication),
            breathing = encrypt_func(self.breathing),
            circulation = encrypt_func(self.circulation),
            elimination = encrypt_func(self.elimination),
            pain = encrypt_func(self.pain),
            activity = encrypt_func(self.activity),
            sleep = encrypt_func(self.sleep),
            psycho = encrypt_func(self.psycho),
            time_of_creation = encrypt_func(self.time_of_creation),
            timestamp = encrypt_func(self.timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        )

    def timed_out(self, hours: int) -> bool:
        now = datetime.now()
        # Temporarily set to 60 instead of 3600 to get minutes instead of hours.
        timeframe = (hours * 60)
        if self.checked:
            timeframe = (hours * 20)
        return (now - self.timestamp).total_seconds() > timeframe

class SbarNote(BoxLayout):
    '''Mainscreen Sbar note handling'''

    def on_checkbox_active(self, checkbox):
        '''CheckBox Interaction'''
        pass

    def get_font_size(self):
        self.font_size = CustomApp.CustomApp.font_size
        return self.font_size

class EmergNote(BoxLayout):
    '''Mainscreen Emerg note handling'''

    def on_checkbox_active(self, checkbox):
        '''CheckBox Interaction'''
        pass

    def get_font_size(self):
        self.font_size = CustomApp.CustomApp.font_size
        return self.font_size
