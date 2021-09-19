from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from datetime import date

todays_date = date.today()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style ="Dark"
        self.theme_cls.primary_palette ="BlueGray"
        return Builder.load_file('new.kv')

    #on ok
    def on_save(self,instance,value,date_range):
        self.root.ids.date_label.text = str(value)

    def on_cancel(self):
        pass


    def show_date_picker(self):
        date_dialog = MDDatePicker(year=todays_date.year, month=todays_date.month, day=todays_date.day)
        date_dialog.bind(on_save = self.on_save,on_cancel = self.on_cancel)
        date_dialog.open()


MainApp().run()