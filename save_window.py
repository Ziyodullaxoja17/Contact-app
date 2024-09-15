from PyQt5.QtWidgets import QWidget 
from components import Button , Label , Input

class Window_Save(QWidget):
     def __init__(self):
          super().__init__()
          self.resize(400 , 400)
          self.setWindowTitle("#New Contact")
          self.new_contact_label=Label(self , "New Contact" , 30)
          self.name_input=Input(self , "Name" , 300 , 50 , 120)
          self.number_input=Input(self , "Number" ,300 , 50 , 180)

          self.save_new_contact_btn=Button(self , "Save" ,150 , 300 )


          




