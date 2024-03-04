#import required modules
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import sqlite3

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
        #perform validation on the username and password
        if enteredPassword == '' or enteredUsername =='':
            messageBoxHandler('Blank fields detected','Password and Username must be entered','warning')
        else:
            messageBoxHandler('Success', 'You have logged in successfully')
    
    def clearMethod(self):
        '''Resets the form fields'''
        self.userNameInput.setText('')
        self.passwordInput.setText('')

def messageBoxHandler(title, message, iconType='info'):
    '''this will display a dialogue message'''
    msgBox = QtWidgets.QMessageBox() #this line creates a message box object
    # set icon type based on the flag
    if iconType ==  'Info':
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
    elif iconType == 'question':
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
    elif iconType == 'warning':
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)  
    else:
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
    #set the title
    msgBox.setWindowTitle(title)
    #set the content
    msgBox.setText(message)  
    msgBox.exec_() #show the msg box

def dbConnector():
    '''connects to the database and returns a cursor and connection object'''
    conn = sqlite3.connect('usersAndFilms.db')
    cur = conn.cursor()
    return conn,cur

def mainAppication():
    '''Main application load the window instance'''
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

#mainAppication()
#print(dbConnector())