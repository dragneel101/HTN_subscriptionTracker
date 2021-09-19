from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.primary_palette ="BlueGray"
        return Builder.load_file('signup.kv')

    
        


    def verify(self):
        if len(self.root.ids.user.text) <=5:
            self.root.ids.register_label.text= 'Username too short'
            self.root.ids.user.text= ''
            self.root.ids.password.text=''

        else:
            if len(self.root.ids.password.text) <= 5:
                self.root.ids.register_label.text= 'Weak Password'
                self.root.ids.user.text= ''
                self.root.ids.password.text=''

            elif  self.root.ids.password.text != self.root.ids.password2.text:
                self.root.ids.register_label.text= 'Password doesnt match'
                self.root.ids.user.text= ''
                self.root.ids.password.text=''
            else:
                self.root.ids.register_label.text= f' {self.root.ids.user.text} Registered'
                self.root.ids.user.text= ''
                self.root.ids.password.text=''

        
        

    def clear(self):
        self.root.ids.register_label.text="WELCOME"
        self.root.ids.user.text= ''
        self.root.ids.password.text=''

MainApp().run()
