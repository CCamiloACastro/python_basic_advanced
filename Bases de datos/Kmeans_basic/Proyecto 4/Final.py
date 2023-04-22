import base64
import io
import mysql.connector
import os
import pandas as pd
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


def connect_db():
    """
    function to connect with mysql
    Returns:
        An object mysql connector

    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="Proyecto4"
    )
    return connection


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto4.ui", self)
        self.pushButton.clicked.connect(self.load_file)
        self.comboBox.currentIndexChanged.connect(self.decode_file)
        self.pushButton_2.clicked.connect(self.delete_file)

    def delete_file(self):
        print('Delete all the files in the database')
        try:
            # Quita la imagen
            pixmap = QPixmap("")
            self.label.setPixmap(pixmap)
            # Conexión para eliminar
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Datos WHERE ID > 1")
            connection.commit()
            self.read_from_database()
        except Exception as exception:
            print(f"Something went wrong in Delete File")
            print(f'{exception}')

    def load_file(self):
        print('load file')
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel (*.xlsx)")

        if file_path:
            print('File path different to None')
            file_name_ = os.path.basename(file_path)
            file_name = file_name_.split(".")[0]

            try:
                df = pd.read_excel(file_path)
                data = df.to_csv(index=False).encode("utf-8")
                encoded_data = base64.b64encode(data)
                # print(f'\n\tEncoded_data\t{encoded_data}')
                self.send_to_database(file_name, encoded_data)
                self.read_from_database()
            except Exception as exception:
                print(f"Something went wrong in Load File")
                print(f'{exception}')

    def send_to_database(self, file_name, encoded_data):
        print('send to database')
        self.comboBox.clear()

        try:
            connection = connect_db()
            cursor = connection.cursor()
            query = "INSERT INTO Datos (`Nombre`, `Archivo`) VALUES (%s, %s)"
            cursor.execute(query, (file_name, encoded_data))
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as exception:
            print(f"Something went wrong in Send Data")
            print(f'{exception}')

    def read_from_database(self):
        print('read data')
        self.comboBox.clear()

        try:
            connection = connect_db()
            cursor = connection.cursor()
            cursor.execute("SELECT Nombre FROM Datos")
            result = cursor.fetchall()
            self.comboBox.addItems([i[0] for i in result])
            cursor.close()
            connection.close()
        except Exception as exception:
            print(f"Something went wrong in Read data")
            print(f'{exception}')

    def decode_file(self):
        print('decode_file')
        file_name = self.comboBox.currentText()
        if file_name != "Seleccionar":

            try:
                connection = connect_db()
                cursor = connection.cursor()
                cursor.execute("SELECT Archivo FROM Datos WHERE Nombre=%s", (file_name,))
                result = cursor.fetchone()

                if result is not None and result[0] is not None:
                    encoded_data = result[0]
                    decoded_data = base64.b64decode(encoded_data)

                    try:
                        df = pd.read_csv(io.StringIO(decoded_data.decode('utf-8')))
                        # Transformar la variable job_title en una variable numérica
                        le = LabelEncoder()
                        # Ajustar codificador de etiquetas y devolver etiquetas codificadas
                        df['job_title_num'] = le.fit_transform(df['job_title'])
                        print(df['job_title_num'])
                        # Seleccionar las características a utilizar en el clustering
                        df_values = df[['job_title_num', 'salary_in_usd']].values
                        # Entrenar el modelo de clustering con KMeans
                        kmeans = KMeans(n_clusters=10, random_state=42)
                        kmeans.fit(df_values)

                        # Obtener los centroides y las etiquetas de cada punto
                        centroides = kmeans.cluster_centers_
                        labels = kmeans.labels_

                        # Visualizar los resultados
                        plt.scatter(df_values[:, 0], df_values[:, 1], c=labels)
                        plt.scatter(centroides[:, 0], centroides[:, 1], marker='*', s=300, c='r')
                        plt.title('KMeans Clustering')
                        plt.xlabel('job_title')
                        plt.ylabel('salary_in_usd')
                        # plt.show()
                        plt.savefig("abc.png")

                        pixmap = QPixmap("./abc.png")
                        self.label.setPixmap(pixmap)

                    except Exception as e:
                        QMessageBox.critical(self, "Error",
                                             "An error occurred while decoding or saving the file:\n" + str(e))
                        pixmap = QPixmap("")
                        self.label.setPixmap(pixmap)
            except Exception as exception:
                print(f'Error in decode file {exception}')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setWindowTitle('Proyecto 4')
    window.setWindowIcon(QIcon("ud.png"))
    window.show()
    window.read_from_database()
    app.exec()
