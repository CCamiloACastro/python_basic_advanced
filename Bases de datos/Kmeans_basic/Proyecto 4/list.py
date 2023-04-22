import base64
import mysql.connector
import os
import pandas as pd
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto4.ui", self)
        self.pushButton.clicked.connect(self.load_file)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel (*.xlsx)")
        if file_path:
            file_name = os.path.basename(file_path)
            df = pd.read_excel(file_path)
            data = df.to_csv(index=False).encode("utf-8")
            encoded_data = base64.b64encode(data)
            self.send_to_database(file_name, encoded_data)

    def send_to_database(self, file_name, encoded_data):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="Proyecto4"
        )
        cursor = connection.cursor()
        query = "INSERT INTO Datos (`Nombre`, `Archivo`) VALUES (%s, %s)"
        cursor.execute(query, (file_name, encoded_data))
        connection.commit()
        cursor.close()
        connection.close()


    def read_data(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="Proyecto4"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Nombre FROM Datos")
        result = mycursor.fetchall()

        self.comboBox.addItems([i[0] for i in result])
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    window.read_data()
    app.exec()
