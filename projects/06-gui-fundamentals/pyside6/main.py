from PySide6.QtWidgets import QApplication
from learning import MainWindow 

app = QApplication([])
window = MainWindow()
window.show()
app.exec()