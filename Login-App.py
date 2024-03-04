#import required modules
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

#create the login widget class - each window must habe a class

class Ui(QtWidgets.QMainWindow):
    '''This is a window class based on the xml code in the loguin ui'''
    def __init__(self):
        '''constructor method'''
        super(Ui, self).__init__()
        uic.loadUi()