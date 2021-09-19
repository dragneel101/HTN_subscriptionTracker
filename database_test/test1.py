from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.primary_palette ="BlueGray"

        #create Database Or Connect TO Onw
        connect1 = sqlite3.connect('test_db.db')

        #create a cursor
        c = connect1.cursor()

        #create a table
        c.execute("""CREATE TABLE if not exists customers(name text)""")

        #commit our changes
        connect1.commit()

        #close conncetion
        connect1.close()

        return Builder.load_file('test1.kv')


    def submit(self):
        #create Database Or Connect TO Onw
        connect1 = sqlite3.connect('test_db.db')

        #create a cursor
        c = connect1.cursor()

        #create a table
        c.execute("INSERT INTO customers VALUES(:first)",{
            'first':self.root.ids.word_input.text
        })
        self.root.ids.word_label.text = f"{self.root.ids.word_label.text} Added"
        self.root.ids.word_input.text =""

        #commit our changes
        connect1.commit()

        #close conncetion
        connect1.close()

    def show_records(self):
        #create Database Or Connect TO Onw
        connect1 = sqlite3.connect('test_db.db')
        #create a cursor
        c = connect1.cursor()
        #create a table
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        word=''

        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'

        self.root.ids.word_label.text = f"{self.root.ids.word_label.text}"
        self.root.ids.word_input.text =""

        #commit our changes
        connect1.commit()

        #close conncetion
        connect1.close()


MainApp().run()