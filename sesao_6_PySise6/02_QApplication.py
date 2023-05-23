from PySide6.QtWidgets import QApplication, QPushButton

# QApplication é a classe base que gerencia o loop da nossa aplicação, ela é
# responsável por capitar iterações do usuário
app = QApplication()

# QPushButton representa um widget de botão, podemos mudas o estilo com o
# método setStyleSheet()
button = QPushButton("My Button")
button.setStyleSheet("color: blue; width: 100px; height: 50;background-color: red")
button.show()

app.exec()
