from PyQt5.QtWidgets import QPushButton , QLabel , QLineEdit , QWidget


class Button(QPushButton):
     def __init__(self , oyna  , text , x , y ):
          super().__init__(oyna)

          self.setText(text)
          self.setStyleSheet("""
     font-size : 25px;
     font-weight : bold;
     Pushbutton{
     background-color : blue ;                   
                             }
     QPushbutton:hover{
     background-color : white;
                             }
""")
          self.move(x , y)

          self.resize(100 , 50)


class Input(QLineEdit):
     def __init__(self , oyna , text , w , h , y ):
          super().__init__(oyna)
          self.setPlaceholderText(text)
          self.resize(w , h)
          self.move((400-w) // 2 , y)
          self.setStyleSheet("""
               font-size : 25px;
               font-weight : bold;
          """)



class Label(QLabel):
     def __init__(self , oyna : QWidget, text , y):
          super().__init__(oyna)

          self.setText(text)
          self.setStyleSheet("""
          font-size : 25px;
          font-weight : bold;
          """)
          self.move((oyna.width() - self.width()) // 2 , y)



