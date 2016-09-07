#Written by Peyton Murray
# Kai Liu Group

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout
from matplotlib.pyplot import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class mplWidget(FigureCanvas):

	def __init__(self, parent=None, layout=None, coordinates="", plotType=None):

		self.cid = None							#Set the CID to None until event handling is taken care of later on.
		self.fig = figure()						#Create the figure
		self.axes = self.fig.add_subplot(111)	#Create the main axes, where data will be displayed.
		self.coordinates = coordinates			#Store the plot coordinates.
		self.plotType = plotType

		#Call the parent class initialization methods.
		FigureCanvas.__init__(self, self.fig)
		self.setParent(parent)

		#Set the figure size policy to always take up as much room as possible in the GUI.
		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

		#Add standard matplotlib toolbar.
		tb = NavigationToolbar(self, parent)
		layout.addWidget(self)
		layout.addWidget(tb)

		self.axes.ticklabel_format(useOffset=False)
		return

	#Gets the current coordinates of the plot.
	def getCoordinates(self):
		return self.coordinates

	#Stores the current coordines of the plot.
	def setCoordinates(self, coordinates):
		self.coordinates = coordinates
		return

	def setPlotType(self, plot_type):
		self.plotType = plot_type
		return

	def getPlotType(self):
		return self.plotType

	#Gets the CID of the current figure. Used when setting triggers for event handling
	def getCID(self):
		return self.cid

	#Sets the CID of the current figure. Used when setting triggers for event handling.
	def setCID(self, cid = None):
		self.cid = cid
		return

	#Returns the figure instance contained in the class instance.
	def getFig(self):
		return self.fig

	#Clears the data from the current figure, and removes any colorbars/extraneous axes.
	def clearFig(self):
		#Using fig.clf() here sets the x and y axes ranges to (0.0, 1.0)
		self.axes.cla()

		#Remove any colorbars. They will be replotted when another plot function is called.
		self.removeCbars()

		#Draw the figure again to display the changes.
		self.drawFig()
		return

	#Removes all extraneous axes, including colorbars.
	def removeCbars(self):
		#Get a list of axes that aren't the main plot axes.
		axesList = [axes for axes in self.getFig().get_axes() if axes != self.axes]

		#Only delete remaining axes if there are any left.
		if len(axesList) != 0:
			for axes in axesList:
				self.getFig().delaxes(axes)

		return

	#Returns the main set of axes that are used for displaying data.
	def getAxes(self):
		return self.axes

	#Gets limits of main axes used for displaying data
	def getXlim(self):
		return self.axes.get_xlim()

	#Gets limits of main axes used for displaying data
	def getYlim(self):
		return self.axes.get_ylim()

	#Gets limits of main axes used for displaying data
	def setXlim(self, xlimits):
		self.axes.set_xlim(xlimits)
		return

	#Gets limits of main axes used for displaying data
	def setYlim(self, ylimits):
		self.axes.set_ylim(ylimits)
		return

	#Redraw the figure. Need to do this when any changes are made to the data, figure, artist, axes, etc.
	def drawFig(self):
		self.draw()
		return

	#Sets the current figure to active.
	def setActive(self):
		figure(self.fig.number)
		return