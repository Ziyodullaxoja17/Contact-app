from database import Database

from PyQt5.QtWidgets import QApplication , QMessageBox

from os import system

from mainwindow import Window 
from save_window import Window_Save
from delete_window import Window_Delete

system("cls")

class App:
     def __init__(self) -> None:
          self.asosiysahifa=Window()
          self.saqlashsahifa=Window_Save()
          self.deletesahifa=Window_Delete()
          self.dbase=Database()


          self.asosiysahifa.show()

          self.asosiysahifa.add_new_contact_btn.clicked.connect(self.add_func)
          self.asosiysahifa.delete_contact_btn.clicked.connect(self.delete_func)

     
     def add_func(self):
          self.saqlashsahifa.show()
          self.asosiysahifa.close()

          self.saqlashsahifa.save_new_contact_btn.clicked.connect(self.saqlash_func)
     
     def saqlash_func(self):
          name=self.saqlashsahifa.name_input.text()
          number=self.saqlashsahifa.number_input.text()
          try :
               self.dbase.INSERT_NEW_CONTACT(name , number)
               self.msbox=QMessageBox(self.saqlashsahifa)
               self.msbox.setText("Contact saqlandi")
               
               self.asosiysahifa.show()
               self.saqlashsahifa.close()

          except :
               self.msbox=QMessageBox(self.saqlashsahifa)
               self.msbox.setText("Contact topilmadi")

          
     

     def delete_func(self):
          self.deletesahifa.show()
          self.asosiysahifa.close()

          self.deletesahifa.delete_contact_btn.clicked.connect(self.delete_contact_func)
     
     def delete_contact_func(self):
          
          name=self.deletesahifa.name_input.text()
          try :

               self.dbase.DELETE_CONTACT(name)
               self.msbox=QMessageBox(self.deletesahifa)
               self.msbox.setText("Contact o'chirildi")
               self.asosiysahifa.show()
               self.deletesahifa.close()

          except :
               self.msbox=QMessageBox(self.deletesahifa)
               self.msbox.setText("Contact topilmadi")





app=QApplication([])
main=App()

app.exec()