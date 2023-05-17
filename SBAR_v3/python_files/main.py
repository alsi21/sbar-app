from kivy.config import Config #must be at top
Config.set('graphics', 'width', '360')#
Config.set('graphics', 'height', '640')#

from kivy.core.text import LabelBase

LabelBase.register(name="icon_font", fn_regular="seguisym.ttf")

import CustomApp
from kivy.lang import Builder
from kivy.utils import platform
# Loading Multiple .kv files 
if platform == "android":
    Builder.load_file('Classes.kv')
    Builder.load_file('EmergScreen.kv')
    Builder.load_file('MainScreen.kv')
    Builder.load_file('PinScreen.kv')
    Builder.load_file('SbarScreen.kv')
    Builder.load_file('SetScreen.kv')
    Builder.load_file('SettingsScreen.kv')
    Builder.load_file('HelpScreen.kv')
    Builder.load_file('ManualScreen.kv')
    Builder.load_file('SokScreen.kv')
    Builder.load_file('EmergSearchScreen.kv')
else:
    Builder.load_file('SBAR_v3\kv_files\Classes.kv')
    Builder.load_file('SBAR_v3\kv_files\EmergScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\MainScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\PinScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\SbarScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\SetScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\SettingsScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\HelpScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\ManualScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\SokScreen.kv')
    Builder.load_file('SBAR_v3\kv_files\EmergSearchScreen.kv')

if __name__ == '__main__':
    CustomApp.CustomApp().run()
    