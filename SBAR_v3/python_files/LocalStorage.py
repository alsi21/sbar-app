from classes import Note
from Encryption import encrypt, decrypt
from kivy.storage.jsonstore import JsonStore

from datetime import datetime

# Storage constants used when interacting with local storage managed by Kivy.
STORE_NOTES = JsonStore('notes.json')
STORE_PIN = JsonStore('pin.json')
STORE_SETTINGS = JsonStore('settings.json')

def serialize_notes(notes_storage):
    '''Takes in JsonStore link, returns a list of Notes.'''
    notes = []
    keys = notes_storage.keys()
    for key in keys:
        data = notes_storage.get(key)
        note = Note(
            decrypt(data['patientid']),
            decrypt(data['situation']),
            decrypt(data['background']),
            decrypt(data['relevant']),
            decrypt(data['recommendation']),
            decrypt(data['extra']),
            decrypt(data['safety']),
            decrypt(data['airway']),
            decrypt(data['breath']),
            decrypt(data['circ']),
            decrypt(data['disability']),
            decrypt(data['exposure']),
            data['emergency'],
            data['checked'],
            decrypt(data['communication']),
            decrypt(data['breathing']),
            decrypt(data['circulation']),
            decrypt(data['elimination']),
            decrypt(data['pain']),
            decrypt(data['activity']),
            decrypt(data['sleep']),
            decrypt(data['psycho']),
            decrypt(data['time_of_creation']),
            datetime.strptime(decrypt(data['timestamp']), '%Y-%m-%d %H:%M:%S')

        )
        if note.checked:
            notes.insert(0, note)
        else:
            notes.append(note)
    return notes

def serialize_pin(pin_storage) -> str:
    '''Takes in JsonStore link, returns pin.'''
    pin = ''
    if pin_storage.exists('pin'):
        pin = decrypt(pin_storage.get('pin')['code'])
    return pin

def get_font(font_storage) -> str:
    '''Takes in JsonStore link, returns pin.'''
    if font_storage.exists('font_size'):
        font = font_storage.get('font_size')['font']
    else:
        font = 1
    return font

def get_data(notes_storage, time_of_creation: str):
    '''Takes in JsonStore link, patient ID and time of creation.
    Returns data matching ID and ToC.'''
    id = time_of_creation
    encoded_pid = encrypt(id)
    if notes_storage.exists(encoded_pid):
        return notes_storage.get(encoded_pid)

def delete_data(notes_storage, time_of_creation: str) -> None:
    '''Takes in JsonStore link, patient ID and time of creation.
    Removes data matching ID and ToC.'''
    id = time_of_creation
    keys = notes_storage.keys()
    for key in keys:
        if decrypt(key) == id:
            notes_storage.delete(key)
