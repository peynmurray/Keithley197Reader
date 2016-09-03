import pyvisa
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.pyplot import *
from numpy import *
import time

from PyQt5 import QtGui, QtWidgets, QtCore
from PyVoltageReader import *

class PyVoltageReader(QtWidgets.QMainWindow, Ui_MainWindow, object):

	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)
		self.connectButtons()
		return
	
	def connectButtons(self):
		self.startButton.clicked.connect(self.startButtonClicked)
		self.stopButton.clicked.connect(self.stopButtonClicked)
		self.clearButton.clicked.connect(self.clearButtonClicked)
		self.refreshButton.clicked.connect(self.refreshButtonClicked)
		return


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = PyVoltageReader()
	win.setWindowTitle("PyVoltageReader")
	win.show()
	sys.exit(app.exec_())
