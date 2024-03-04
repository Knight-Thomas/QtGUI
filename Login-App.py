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
        print('Login button was clicked')
    def clearMethod(self):
        '''Resets the form fields'''
        print('Clear button was clicked')
def mainAppication():
    '''Main application load the window instance'''
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

mainAppication()