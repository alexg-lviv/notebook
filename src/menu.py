import sys

from notebook import Notebook, Note

class Menu:
    '''
    display a menu and respond to choises whn run
    '''
    def __init__(self):
        self.notebook = Notebook
        self.choices = {
        '1': self.show_notes,
        '2': self.search_notes,
        '3': self.add_note,
        '4': self.modify_note,
        '5': self.quit
        }
    def display_menu(self):
        print("""
Notebook Menu

1. show all notes
2. search notes
3. add note
4. modify note
5. quit
""")
    def run(self):
        '''
        display the menu and respond to choices
        '''
        while True:
            self.display_menu()
            choice = input("enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
