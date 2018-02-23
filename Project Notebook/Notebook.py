import datetime
# Store the next available id for all new notes
last_id = 0

class Note:
     '''Represent a note in the notebook. Match against a
        Objects in Python
        [ 52 ]
        string in searches and store tags for each note.
        '''

     def __init__(self, memo, tags=''):
         '''initialize a note with memo and optional
         space-separated tags. Automatically set the note's
         creation date and a unique id.'''
         self.memo = memo
         self.tags = tags
         self.creation_date = datetime.date.today()
         global last_id
         last_id += 1
         self.id = last_id

     def match(self, filter):
         '''Determine if this note matches the filter
         text. Return True if it matches, False otherwise.

         Search is case sensitive and matches both text and
         tags.'''
         return filter in self.memo or filter in self.tags

class Notebook:
     '''Represent a collection of notes that can be tagged,
     modified, and searched.'''

     def __init__(self):
         '''Initialize a notebook with an empty list.'''
         self.notes = []

     def new_note(self, memo, tags=''):
         '''Create a new note and add it to the list.'''
         self.notes.append(Note(memo, tags))

     def modify_memo(self, note_id, memo):
         '''Find the note with the given id and change its
         memo to the given value.'''
         for note in self.notes:
             if note.id == note_id:
                 note.memo = memo
                 break

     def modify_tags(self, note_id, tags):
         '''Find the note with the given id and change its
         tags to the given value.'''
         for note in self.notes:
             if note.id == note_id:
                 note.tags = tags
                 break

     def search(self, filter):
         '''Find all notes that match the given filter
         string.'''
         return [note for note in self.notes if
         note.match(filter)]

if __name__ == "__main__":
    #'Task1: Test the efficiency'
    print('Task1. Test the efficiency:')
    n = Notebook()
    n.new_note("hello world")
    n.new_note("hello again")
    print(n.notes[0].id)
    print(n.notes[1].id)
    print(n.notes[0].memo)
    print( n.search("hello"))
    print(n.search("world"))
    n.modify_memo(1, "hi world")
    print( n.notes[0].memo)
    #Task2: use isinstance, dir to explain: object, atribute, method, self, __init__, __str__
    print('\nTask2. Use isinstance, dir to explain: object, atribute, method, self, __init__, __str__:')
    #here by using isinstance() we found that it shows if object is born from class
    print(isinstance(n, Notebook))
    print(isinstance(n, object))
    print(isinstance(Notebook, object))
    #here we can find all methods(created by ourselves and builded in) in needed class
    print("\nDir method:")
    print(dir(Notebook))
    #__str__ methot is called everytime we use command print(smth)
    #__init__ method is called automatically everytime we create new object from a class 