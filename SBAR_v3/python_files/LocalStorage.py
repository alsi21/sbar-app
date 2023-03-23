from classes import Note
from Encryption import encrypt, decrypt
from kivy.storage.jsonstore import JsonStore

# Storage constants used when interacting with local storage managed by Kivy.
STORE_NOTES = JsonStore('notes.json')
STORE_PIN = JsonStore('pin.json')

def serialize_notes(notes_storage):
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
            decrypt(data['airway']),
            decrypt(data['breath']),
            decrypt(data['circ']),
            decrypt(data['disability']),
            decrypt(data['exposure']),
            data['emergency'],
            decrypt(data['time_of_creation'])
        )
        notes.append(note)
    return notes
    
def serialize_pin(pin_storage):
    pin = ''
    if pin_storage.exists('pin'):
        pin = decrypt(pin_storage.get('pin')['code'])
    return pin

def get_data(notes_storage, patientid):
    encoded_pid = encrypt(patientid)
    if notes_storage.exists(encoded_pid):
        notes_storage.get(encoded_pid)

def delete_data(notes_storage, patientid, time_of_creation):
    id = patientid + time_of_creation
    keys = notes_storage.keys()
    for key in keys:
        if decrypt(key) == id:
            notes_storage.delete(key)