import mysql.connector
from os import system 
from colorama import init , Fore

system("cls")


class Database:
     def __init__(self):
          self.data_base=mysql.connector.connect(
               host = "localhost",
               user = 'root',
               password = '111317'
          )

          self.kursor=self.data_base.cursor()


          self.__Set_Up_Database()


     def __Set_Up_Database(self):
          self.kursor.execute("CREATE DATABASE IF NOT EXISTS DATABASE_CONTACTS;")
          self.kursor.execute("USE DATABASE_CONTACTS;")
          self.kursor.execute("""CREATE TABLE IF NOT EXISTS CONTACTS (NAME VARCHAR(32) UNIQUE , 
           NUMBER_CONTACT VARCHAR(32) UNIQUE);""")


          print(Fore.GREEN + "$ DATABASE YARATILDI ")
     

     def INSERT_NEW_CONTACT(self , name , number):
          try:
               self.kursor.execute("SELECT * FROM CONTACTS WHERE NAME = %s OR NUMBER_CONTACT = %s;",(name, number))
               if self.kursor.fetchone() :
                    
                    print(Fore.RED + "ERROR : Bunday kontakt mavjud")
                    return 1
               
               else :
                    self.kursor.execute("INSERT INTO CONTACTS VALUES (%s , %s);",(name , number))
                    self.data_base.commit()
                    print(Fore.GREEN + "$ CONTACT YARATILDI ")

          except :
               print(Fore.RED + "ERROR")
               return 1
     
     
          
     
     def DELETE_CONTACT (self , name):
          try:
               self.kursor.execute("DELETE FROM CONTACTS WHERE NAME = %s;",(name,))
               self.data_base.commit()
               print(Fore.GREEN + "$ CONTACT O'CHIRILDI ")
          except:
               print(Fore.RED + "ERROR")
               return 1

     def GET_ALL_CONTACTS(self):
          try:
               self.kursor.execute("SELECT * FROM CONTACTS;")
               data_contact=self.kursor.fetchall()
               data_contact=list(data_contact)
               
               return data_contact 
          except:
               print(Fore.RED + "ERROR")
               return 1  
          





database=Database()