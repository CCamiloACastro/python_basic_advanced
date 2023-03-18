import sys
from PyQt6 import uic, QtWidgets

Form, Ventana = uic.loadUiType("ej1.ui")

class Aplicacion(QtWidgets.QMainWindow, Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Form.__init__(self)
        self.setupUi(self)
        self.Boton.clicked.connect(self.aviso)
    def aviso(self):
        self.Campo_entrada.setText("Hola mundo")

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Vent = Aplicacion()
    Vent.show()
    app.exec()
