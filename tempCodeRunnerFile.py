from database import Database
from PyQt5.QtWidgets import QApplication, QMessageBox
from os import system
from mainwindow import Window
from save_window import Window_Save
from delete_window import Window_Delete

system("cls")

class App:
    def __init__(self) -> None:
        self.asosiysahifa = Window()
        self.saqlashsahifa = Window_Save()
        self.deletesahifa = Window_Delete()
        self.dbase = Database()

        self.asosiysahifa.show()

        # Connect buttons to corresponding functions
        self.asosiysahifa.add_new_contact_btn.clicked.connect(self.add_func)
        self.asosiysahifa.delete_contact_btn.clicked.connect(self.delete_func)

    def add_func(self):
        self.saqlashsahifa.show()
        self.asosiysahifa.close()

        # Disconnect existing connections before connecting to avoid multiple triggers
        try:
            self.saqlashsahifa.save_new_contact_btn.clicked.disconnect()
        except:
            pass
        self.saqlashsahifa.save_new_contact_btn.clicked.connect(self.saqlash_func)

    def saqlash_func(self):
        name = self.saqlashsahifa.name_input.text().strip()
        number = self.saqlashsahifa.number_input.text().strip()

        if not name or not number:
            self.show_message(self.saqlashsahifa, "Iltimos, barcha ma'lumotlarni to'ldiring")
            return

        if not number.isdigit():
            self.show_message(self.saqlashsahifa, "Iltimos, telefon raqamga xatolik yuz berdi")
            return

        try:
            result = self.dbase.INSERT_NEW_CONTACT(name, number)
            if result == 1:
                self.show_message(self.saqlashsahifa, "Contact mavjud")
            else:
                self.show_message(self.saqlashsahifa, "Contact saqlandi")
                self.saqlashsahifa.name_input.clear()
                self.saqlashsahifa.number_input.clear()
                
                self.asosiysahifa.show()
                self.saqlashsahifa.close()

            
           

            

        except Exception as e:
            self.show_message(self.saqlashsahifa, f"Xatolik yuz berdi: {str(e)}")

    def delete_func(self):
        self.deletesahifa.show()
        self.asosiysahifa.close()

        
        try:
            self.deletesahifa.delete_contact_btn.clicked.disconnect()
        except:
            pass
        self.deletesahifa.delete_contact_btn.clicked.connect(self.delete_contact_func)

    def delete_contact_func(self):
        name = self.deletesahifa.name_input.text().strip()

        try:
            result = self.dbase.DELETE_CONTACT(name)
            if result == 1:
                self.show_message(self.deletesahifa, "Contact o'chirildi")
            else:
                self.show_message(self.deletesahifa, "Contact topilmadi")

            # Show the main window and close the delete window
            self.asosiysahifa.show()
            self.deletesahifa.close()

        except Exception as e:
            self.show_message(self.deletesahifa, f"Xatolik yuz berdi: {str(e)}")

    def show_message(self, parent, text):
        
        msbox = QMessageBox(parent)
        msbox.setText(text)
        msbox.exec()

app = QApplication([])
main = App()
app.exec()
