from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
value = randint(0, 1000)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.primary_palette ="BlueGray"
        #create Database Or Connect TO Onw
        connect1 = sqlite3.connect('../db/users.db')
        #create a cursor
        c = connect1.cursor()
        c.execute("""CREATE TABLE if not exists subscriptions(userID text,subscription text,date text )""")
        #commit our changes
        connect1.commit()
        #close conncetion
        connect1.close()
        return Builder.load_file('subscribe.kv')


    def verify(self):
        #create Database Or Connect TO Onw
        connect1 = sqlite3.connect('../db/users.db')
        #create a cursor
        c = connect1.cursor()
        #create a table
        c.execute("INSERT INTO subscriptions VALUES(:userID,:subscription,:date)",{
            'userID':f'{self.root.ids.user.text}{value}',
            'subscription':self.root.ids.subscription.text,
            'date':self.root.ids.duedate.text
        })
        self.root.ids.subscribe_label.text= f' {self.root.ids.subscription.text} Subscribed'
        self.root.ids.user.text= ''
        self.root.ids.subscription.text=''
        self.root.ids.duedate.text=''
        #commit our changes
        connect1.commit()
        #close conncetion
        connect1.close()

    def clear(self):
        self.root.ids.register_label.text="SUBSCRIPTION"
        self.root.ids.user.text= ''
        self.root.ids.password.text=''
        self.root.ids.password2.text=''

MainApp().run()
