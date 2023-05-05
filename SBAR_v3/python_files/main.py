from kivy.config import Config #must be at top
Config.set('graphics', 'width', '360')#
Config.set('graphics', 'height', '640')#

import CustomApp
from kivy.lang import Builder
# Loading Multiple .kv files 
Builder.load_file('SBAR_v3\kv_files\Classes.kv')
Builder.load_file('SBAR_v3\kv_files\EmergScreen.kv')
Builder.load_file('SBAR_v3\kv_files\MainScreen.kv')
Builder.load_file('SBAR_v3\kv_files\PinScreen.kv')
Builder.load_file('SBAR_v3\kv_files\SbarScreen.kv')
Builder.load_file('SBAR_v3\kv_files\SetScreen.kv')
Builder.load_file('SBAR_v3\kv_files\SettingsScreen.kv')
Builder.load_file('SBAR_v3\kv_files\HelpScreen.kv')
Builder.load_file('SBAR_v3\kv_files\ManualScreen.kv')

if __name__ == '__main__':
    CustomApp.CustomApp().run()
