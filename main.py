import sys
import visa
import pyqtgraph as pg
from numpy import *
# import mplWidget
import PyVoltageReader
import time

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QThread

class QueryVoltmeter(QThread):

	dataReady = QtCore.pyqtSignal(float)

	def __init__(self, gpib_device, rate, kind):
		QThread.__init__(self)
		if kind == "voltmeter":
			self.calibration = 120
		elif kind == "ammeter":
			self.calibration = 0.1
		elif kind == "wattmeter":
			self.calibration = 50
		else:
			raise ValueError("Wrong kind parameter.")

		self.gpib_device = gpib_device
		self.rm = visa.ResourceManager()
		self.instrument = self.rm.open_resource(gpib_device)
		self.rate = rate
		self.stopFlag = False

	def __del__(self):
		self.wait()

	def run(self):
		while not self.stopFlag:
			self.dataReady.emit(self.calibration*float(self.instrument.read()[4:]))
			self.sleep(1/self.rate)
		return

	def stop(self):
		self.stopFlag = True
		return

class PyVoltageReader(QtWidgets.QMainWindow, PyVoltageReader.Ui_MainWindow, object):

	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)
		self.connectButtons()
		self.xdata = []
		self.ydata = []
		self.decoratePlot()
		return

	def connectButtons(self):
		self.startButton.clicked.connect(self.startButtonClicked)
		self.stopButton.clicked.connect(self.stopButtonClicked)
		self.clearButton.clicked.connect(self.clearButtonClicked)
		self.refreshButton.clicked.connect(self.refreshButtonClicked)

		self.refreshButtonClicked()
		return

	def startButtonClicked(self):
		self.t0 = time.time()
		self.queryThread = QueryVoltmeter(self.gpibBox.currentText(), rate=self.rateBox.value(), kind="voltmeter")
		self.queryThread.dataReady.connect(self.updatePlot)
		self.queryThread.start()
		return

	def stopButtonClicked(self):
		self.queryThread.stop()
		return

	def clearButtonClicked(self):
		self.xdata = []
		self.ydata = []
		self.plot.clear()
		return

	def refreshButtonClicked(self):
		self.gpibBox.clear()
		instruments = visa.ResourceManager().list_resources()
		self.gpibBox.addItems(instruments)
		return

	def decoratePlot(self):
		self.plot.setRange(xRange=[0, 1], yRange=[0, 1])
		self.plot.repaint()
		return

	def updatePlot(self, data):
		self.plot.clear()
		self.xdata.append(time.time()-self.t0)
		self.ydata.append(data)
		self.plot.setRange(xRange=[0, self.xdata[-1]], yRange=[min(self.ydata), max(self.ydata)])
		self.plot.addItem(pg.PlotDataItem(x=self.xdata, y=self.ydata, labels={'left':'Voltage', 'bottom':'Time'}, pen='w', symbol='o', pxMode=False))
		self.plot.setTitle("Voltage")
		self.plot.repaint()
		return

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = PyVoltageReader()
	win.setWindowTitle("PyVoltageReader")
	win.show()
	sys.exit(app.exec_())
