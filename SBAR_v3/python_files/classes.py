import CustomApp

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class SquareBlueButton(Button):
    '''Blue button'''


class BlueTextInput(TextInput):
    '''Blue TextInput'''


class Note:
    '''Class that holds information presented in notes'''

    def __init__(self, patientid, situation, background, relevant, recommendation, extra, airway, breath, circ, disability, exposure, time_of_creation):
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
        checked : Bool
            Value to see if nurse has marked note as finished
        '''
        #For SBAR and Emerg
        self.patientid = patientid
        self.relevant = relevant
        self.time_of_creation = time_of_creation
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
        self.checked = False

    def export_note(self, local_storage, encrypt_func):
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
            exposure = self.exposure,
            time_of_creation = encrypt_func(self.time_of_creation)
        )


class SbarNote(BoxLayout):
    '''Mainscreen Sbar note handling'''

    def __init__(self, **kwargs):
        '''Builds note in mainmenu'''
        super().__init__(**kwargs)
        box = BoxLayout(orientation='horizontal', size_hint_y=None, height=80)
        main_btn = Button(size_hint_x=.8)
        box.add_widget(main_btn)
        del_btn = SquareBlueButton(text='del', size_hint_x=.2)
        del_btn.bind(on_press=self.delete_boxlayout)
        box.add_widget(del_btn)

    def delete_boxlayout(self, instance):
        '''Deletes itself (note)'''
        self.parent.height -= 90
        CustomApp.CustomApp.notes.remove(self.ids.buttonone.note)
        self.parent.remove_widget(self)

class EmergNote(BoxLayout):
    '''Mainscreen Emerg note handling'''

    def delete_boxlayout(self, instance):
        '''Deletes itself (note)'''
        self.parent.height -= 90
        CustomApp.CustomApp.notes.remove(self.ids.buttonone.note)
        self.parent.remove_widget(self)
