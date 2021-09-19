from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

# generate random integer values
from random import randint
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
        #create a table
        c.execute("""CREATE TABLE if not exists userCredentials(userID text,username text,password text )""")
        #commit our changes
        connect1.commit()
        #close conncetion
        connect1.close()
        return Builder.load_file('signup.kv')

    
        


    def verify(self):
        if len(self.root.ids.user.text) <=5:
            self.root.ids.register_label.text= 'Username too short'
            self.root.ids.user.text= ''
            self.root.ids.password.text=''
            self.root.ids.password2.text=''

        else:
            if len(self.root.ids.password.text) <= 5:
                self.root.ids.register_label.text= 'Weak Password'
                self.root.ids.user.text= ''
                self.root.ids.password.text=''
                self.root.ids.password2.text=''

            elif  self.root.ids.password.text != self.root.ids.password2.text:
                self.root.ids.register_label.text= 'Password doesnt match'
                self.root.ids.user.text= ''
                self.root.ids.password.text=''
                self.root.ids.password2.text=''
            else:
                value = randint(0, 1000)
                #create Database Or Connect TO Onw
                connect1 = sqlite3.connect('../db/users.db')
                #create a cursor
                c = connect1.cursor()
                #create a table
                c.execute("INSERT INTO userCredentials VALUES(:userID,:username,:password)",{
                    'userID':f'{self.root.ids.user.text}{value}',
                    'username':self.root.ids.user.text,
                    'password':self.root.ids.password.text
                })
                self.root.ids.register_label.text= f' {self.root.ids.user.text} Registered'
                self.root.ids.user.text= ''
                self.root.ids.password.text=''
                self.root.ids.password2.text=''
                #commit our changes
                connect1.commit()
                #close conncetion
                connect1.close()



        
        

    def clear(self):
        self.root.ids.register_label.text="REGISTRATION"
        self.root.ids.user.text= ''
        self.root.ids.password.text=''
        self.root.ids.password2.text=''

MainApp().run()
