'''
	Autor : Richard Pedraza
	Fecha : 24 - 02 - 2021
	Nombre : login
	Descripcion : login con pyqt y pyrebase
    modulos:
        -pyrebase: conexion y autentificacion de usuarios
        -pyside2: genera todo el entorno grafico 
        -login-ui:trae la vista del login
'''
import hashlib
import re
import pyrebase
import sys
import platform
from PySide2 import QtWidgets, QtGui, QtCore, QtMultimedia, QtMultimediaWidgets
from login_pyrebase.imagenes import rcc_version
from login_pyrebase.login_ui import *


class mylogin(QtWidgets.QMainWindow):
    def __init__(self, parent=None, *args):
        super(mylogin, self).__init__(parent=parent)
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)
        self.setWindowTitle("Login Firebase")
        """icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/neuron_music/img/neuron.ico"),
        QtGui.QIcon.Normal, QtGui.QIcon.On)
        try:
            widget.setWindowTitle('Neuron Music')
            widget.setFixedSize(460, 470)
            widget.setWindowIcon(icon)
        except:
            pass"""
        # ******************#q
        # conexion firebase
        #******************#
        self.config = {"apiKey": "AIzaSyBVBUR6oftmJrFUue4wFf75i2OWLRHXlyI",
                       "authDomain": "login-6f6f1.firebaseapp.com",
                       "databaseURL": "https://databaseName.firebaseio.com",
                       "storageBucket": "login-6f6f1.appspot.com", }
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        #******************#
        # conecion de los botones del login
        #******************#
        self.ui.boton_aceptar.clicked.connect(self.boton_aceptar)

    # boton aceptar conexion con firebase autenticar correo y hash #contraseña

    def boton_aceptar(self):
        regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        email = self.ui.user.text()
        password_raw = hashlib.sha3_512(self.ui.password.text().encode())
        password = password_raw.hexdigest()
        try:
            if email != '' and re.match(regex, email) and password != '':
                self.auth.sign_in_with_email_and_password(email, password)
                self.popup = QtWidgets.QMessageBox.information(
                    self, 'autentificado correctamente ', 'bienvenido')
            elif email == '':
                self.alert = QtWidgets.QMessageBox.critical(
                    self, 'error', 'campo vacio')
            else:
                self.alert = QtWidgets.QMessageBox.critical(
                    self, 'error', 'email  o contraseña incorrecta')
        except:
            self.alert = QtWidgets.QMessageBox.critical(
                self, 'error', 'email o contraseña incorrecta')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login = mylogin()
    login.show()
    app.exec_()
