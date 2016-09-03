

import visa
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.pyplot import *
from numpy import *
import mplWidget
import PyVoltageReader
import time

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QThread

class QueryVoltmeter(QThread):

	sendData = QtCore.pyqtSignal(float)

	def __init__(self, gpib_device, rate):
		QThread.__init__(self)
		self.gpib_device = gpib_device
		self.rm = visa.ResourceManager()
		self.instrument = self.rm.open_resource(gpib_device)

	def __del__(self):
		self.wait()

	def run(self):
		self.query()
		return

	def query(self):
		self.sendData.emit(self.instrument.read()[4:])
		return

class PyVoltageReader(QtWidgets.QMainWindow, PyVoltageReader.Ui_MainWindow, object):

	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)
		self.connectButtons()
		self.plot = mplWidget.mplWidget(self, layout=self.mplLayout)
		self.decoratePlot()
		return

	def connectButtons(self):
		self.startButton.clicked.connect(self.startButtonClicked)
		self.stopButton.clicked.connect(self.stopButtonClicked)
		self.clearButton.clicked.connect(self.clearButtonClicked)
		self.refreshButton.clicked.connect(self.refreshButtonClicked)
		return

	def startButtonClicked(self):

		self.queryThread = QueryVoltmeter(gpib_device, rate)

		return

	def stopButtonClicked(self):
		return

	def clearButtonClicked(self):
		return

	def refreshButtonClicked(self):
		return

	def decoratePlot(self):
		self.plot.getAxes().set_xlabel("Time")
		self.plot.getAxes().set_ylabel("Voltage")
		return


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = PyVoltageReader()
	win.setWindowTitle("PyVoltageReader")
	win.show()
	sys.exit(app.exec_())
