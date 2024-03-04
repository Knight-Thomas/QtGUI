#import required modules
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

#create the login widget class - each window must habe a class

class Ui(QtWidgets.QMainWindow):
    '''This is a window class based on the xml code in the loguin ui'''
    def __init__(self):
        '''constructor method'''
        super(Ui, self).__init__()
        uic.loadUi('/Users/tomknight/GUI-programming/PyQtGUI/QtGUI/login.ui', self)

        #add event listeners
        self.btnLogin.clicked.connect(self.loginMethod)
        self.btnClear.clicked.connect(self.clearMethod)
        #show the window
        self.show()

    def loginMethod(self):
        '''Handle click events on the login button'''
        #access form line edits
        enteredUsername = self.userNameInput.text()
        enteredPassword = self.passwordInput.text()
        print(f'username: {enteredUsername} | Password: {enteredPassword}')
    def clearMethod(self):
        '''Resets the form fields'''
        self.userNameInput.setText('')
        self.passwordInput.setText('')

def messageBoxHandler(title, message, iconType='info'):
    '''this will display a dialogue message'''
    msgBox = QtWidgets.QMessageBox() #this line creates a message box object
    # set icon type based on the flag
    if iconType ==  'Info':
        msgBox.setIcon(QtWidgets.QMessageBox.information)
    elif iconType == 'question':
        msgBox.setIcon(QtWidgets.QMessageBox.question)
    elif iconType == 'warning':
        msgBox.setIcon(QtWidgets.QMessageBox.warning)  
    else:
        msgBox.setIcon(QtWidgets.QMessageBox.critical)
    #set the title
    msgBox.setWindowTitle(title)
    #set the content
    msgBox.setText(message)  
    msgBox.exec_() #show the msg box

def mainAppication():
    '''Main application load the window instance'''
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

mainAppication()