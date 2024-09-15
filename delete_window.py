from PyQt5.QtWidgets import QWidget
from components import Button , Input , Label 

class Window_Delete(QWidget):
     def __init__(self):
          super().__init__()
          self.resize(400 , 400)
          self.setWindowTitle("#Delete Contact")
          self.delete_contact_label=Label(self , "Delete Contact" , 30)
          self.name_input=Input(self , "Name" , 300 , 50 , 120)

          self.delete_contact_btn=Button(self , "Delete" ,150 , 300 )