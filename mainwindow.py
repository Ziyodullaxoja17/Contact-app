from PyQt5.QtWidgets import  QWidget 
from components import Button , Label

class Window(QWidget):
     def __init__(self):
          super().__init__()
          self.resize(480 , 640)
          self.setWindowTitle("#Contact")
          self.add_new_contact_btn=Button(self , "Add" , 90 , 540)
          self.delete_contact_btn=Button(self , "Delete" , 290 , 540)

          self.contact_label=Label(self , "Contact" , 30)


          




