import datetime

last_id = 0

class Note:
    '''
    Represents a note in notebook
    '''
    def init(self, memo, tags=''):
        '''
        initialize a note with memo and optional tags
        Automatically set the note's creation date ad a unique id
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.day.today()
        global last_id
        last_id += 1
        self.id = last_id
    def match(self, filter):
        '''
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        '''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''
    'Represent a collection of notes that can be tagged,
    modified, and searched
    '''
    def __init__(self):
        '''
        initialize a notebook with an empty list
        '''
        self.notes = []
    def new_note(self, memo, tags=''):
        '''
        create a new note and add it ti the list
        '''
        self.notes.append(Note(memo, tags))
    
    def modify_memo(self, note_id, memo):
        '''
        change the value of note with given id to given value
        '''
        self._find_note(note_id).memo = memo
    
    def modify_tags(self, note_id, tags):
        '''
        change the tags of note with given id to given tags
        '''
        self._find_note(note_id).tags = tags    
    def search(self, filter):
        '''
        find all notes that match the given filter string
        '''
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

