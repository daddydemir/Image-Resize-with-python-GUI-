import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import cv2 

class Example(QWidget):
	filename = " "; w=0; h =0
	def __init__(self , parent=None):
		global filename 
		filename = ""
		super(Example , self).__init__(parent)

		grid = QGridLayout()

		grid.addWidget(self.createLayout1() , 0 , 0)
		grid.addWidget(self.createLayout2() , 0 , 2)
		grid.addWidget(self.createLayout3() , 0 , 1)
		grid.addWidget(self.createLayout4() , 1 , 1)
		grid.addWidget(self.createLayout5() , 1 , 0)
		grid.addWidget(self.createLayout6() , 1 , 2)

		self.setLayout(grid)

		self.setWindowTitle("Image Resize")
		self.setFixedSize(800,500)

	def createLayout1(self):
		self.gurup = QGroupBox("Manual")

		lblWidth = QLabel("Width")
		self.lineWidth = QLineEdit()

		lblHeight = QLabel("Height")
		self.lineHeight = QLineEdit()

		
		izgara = QGridLayout()
		izgara.addWidget(lblWidth , 0 , 0)
		izgara.addWidget(self.lineWidth, 0 , 1)
		izgara.addWidget(lblHeight , 1 , 0)
		izgara.addWidget(self.lineHeight, 1 , 1)

		self.gurup.setLayout(izgara)

		return self.gurup

	def createLayout2(self):
		self.gurupAuto = QGroupBox("Auto")
		self.gurupAuto.setDisabled(True)
		
		self.radioArti = QRadioButton("Size Increase ")
		self.radioArti.setChecked(True)
		self.radioArti.toggled.connect(self.radioA)
		self.slideArti = QSlider(Qt.Horizontal)
		self.slideArti.setMinimum(1)
		self.slideArti.setMaximum(5)
		self.slideArti.valueChanged.connect(self.slideA)
		self.lblArti = QLabel("sayi")

		self.radioEksi = QRadioButton("Size Reduction")
		self.slideEksi = QSlider(Qt.Horizontal)
		self.slideEksi.setMinimum(1)
		self.slideEksi.setMaximum(5)
		self.slideEksi.valueChanged.connect(self.slideE)
		self.slideEksi.setDisabled(True)
		self.lblEksi = QLabel("sayi")


		izgaraAuto = QGridLayout()

		izgaraAuto.addWidget(self.radioArti , 0,0)
		izgaraAuto.addWidget(self.slideArti ,0,1)
		izgaraAuto.addWidget(self.lblArti , 0,2)

		izgaraAuto.addWidget(self.radioEksi , 1,0)
		izgaraAuto.addWidget(self.slideEksi ,1,1)
		izgaraAuto.addWidget(self.lblEksi , 1,2)

		self.gurupAuto.setLayout(izgaraAuto)
		return self.gurupAuto

	def createLayout3(self):
		gurupSec = QGroupBox("Select Mode")
		
		self.radioManual = QRadioButton("Manual Mode")
		self.radioManual.setChecked(True)
		self.radioManual.toggled.connect(self.radioSec)
		self.radioAuto = QRadioButton("Auto Mode")

		izgaraSec = QGridLayout()

		izgaraSec.addWidget(self.radioManual, 0 , 0)
		izgaraSec.addWidget(self.radioAuto , 0 , 1)

		gurupSec.setLayout(izgaraSec)
		return gurupSec

	def createLayout4(self):
		gurupButon = QGroupBox("")

		self.resimSec = QPushButton("Select Image")
		self.resimSec.clicked.connect(self.selectImageClick)
		self.resimKirp = QPushButton("Resize Preview")
		self.resimKirp.clicked.connect(self.resizeImage)
		self.resimSave = QPushButton("Resize Save")
		self.resimSave.clicked.connect(self.saveFile)

		izgaraButon = QGridLayout()
		
		izgaraButon.addWidget(self.resimSec , 0 , 0)
		izgaraButon.addWidget(self.resimKirp , 0 , 1)
		izgaraButon.addWidget(self.resimSave , 0 , 2)

		gurupButon.setLayout(izgaraButon)
		return gurupButon

	def createLayout5(self):
		gurupProp = QGroupBox("Image Properties")

		self.widthOriginal = QLabel("")
		self.heightOriginal = QLabel("")

		izgaraProp = QGridLayout()

		izgaraProp.addWidget(self.widthOriginal , 0,0)
		izgaraProp.addWidget(self.heightOriginal , 1,0)

		gurupProp.setLayout(izgaraProp)
		return gurupProp

	def createLayout6(self):
		gurupProp = QGroupBox("Image Properties (RESIZE)")

		self.widthResize = QLabel("")
		self.heightResize = QLabel("")

		izgaraProp = QGridLayout()

		izgaraProp.addWidget(self.widthResize , 0,0)
		izgaraProp.addWidget(self.heightResize , 1,0)

		gurupProp.setLayout(izgaraProp)
		return gurupProp
		


	def radioA(self):
		if self.radioArti.isChecked() == True:
			self.slideEksi.setDisabled(True)
			self.slideArti.setDisabled(False)
		else:
			self.slideArti.setDisabled(True)
			self.slideEksi.setDisabled(False)
	
	def slideA(self):
		sayi = self.slideArti.value()
		self.lblArti.setText(str(sayi))

	def slideE(self):
		sayi = self.slideEksi.value()
		self.lblEksi.setText(str(sayi))

	def radioSec(self):
		if self.radioManual.isChecked() == True:
			self.gurup.setDisabled(False)
			self.gurupAuto.setDisabled(True)
		else:
			self.gurup.setDisabled(True)
			self.gurupAuto.setDisabled(False)

	def selectImageClick(self): 
		global filename , w, h
		file = QFileDialog.getOpenFileName(self , 'Select Image','c:\\','Images (*.jpg , *.png , *.jpeg)')
		filename = file[0]
		anaResim = cv2.imread(filename)
		h , w , d = anaResim.shape
		width = "Original Width  : "+str(w)
		height = "Original Height : "+str(h)
		self.widthOriginal.setText(width)
		self.heightOriginal.setText(height)

	def resizeImage(self):
		global filename , w , h
		anaresim = cv2.imread(filename)
		h , w , d = anaresim.shape
		width = "Resize Width  :"
		height = "Resize Height :"
		if self.radioManual.isChecked() == True:
			if self.lineWidth.text() != "" and self.lineHeight.text() != "":
				w1 = int(self.lineWidth.text())
				h1 = int(self.lineHeight.text())
				w=w1 ; h=h1
				if w1 > 100 and h1 > 100:	
					cv2.imshow("Resize Image",cv2.resize(anaresim , (w1 , h1)))
					width += str(w1); height += str(h1)
					self.widthResize.setText(width)
					self.heightResize.setText(height)
		if self.radioAuto.isChecked() == True:
			# Slider kullanılıyorsa 
			if self.radioArti.isChecked() == True:
				sayi = self.slideArti.value()
				w = w*sayi; h = h*sayi
				cv2.imshow("Resize Image",cv2.resize(anaresim,(w,h)))
				width += str(w); height += str(h)
				self.widthResize.setText(width)
				self.heightResize.setText(height)
			if self.radioEksi.isChecked() == True:
				sayi = self.slideEksi.value()
				w = int(w/sayi); h = int(h/sayi)
				cv2.imshow("Resize Image",cv2.resize(anaresim,(w,h)))
				width += str(w); height += str(h)
				self.widthResize.setText(width)
				self.heightResize.setText(height)

	def saveFile(self):
		global w ,h , filename 
		if filename != "":
			try:
				isim = "filename"
				save = QFileDialog.getSaveFileName(self , 'Save Image' ,isim ,'Image (*.png)')
				cv2.imwrite(save[0], cv2.resize(cv2.imread(filename) , (w,h)))
			except:
				isim = "filename"
				# nobody


def main():
	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()