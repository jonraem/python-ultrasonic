import sys
import math
import time
import RPi.GPIO as GPIO


__author__ = 'Teemu, Minna, Joni'
__version__ = '0.9'

#	Luokka UI on osa suorituksen k‰yttˆliittym‰‰. Se valmistelee mittauksen ja m‰‰ritt‰‰, 
#	ett‰ mitataanko jaloissa vai metreiss‰. Se myˆs mahdollistaa heti alussa ohjelman hallitun 
#	lopettamisen.
class UI:
	def userinterface(self):
		putin = Input()
		dialog1 = raw_input("Would you like to measure distance? (Y/N) ")
		time.sleep(0.5)
		if dialog1.lower() == "y":
			while True:
				UI.unit = raw_input("Do you want to measure in meters or feet? (M/F) ")
				if UI.unit.lower() == "m" or UI.unit.lower() == "f":
					time.sleep(0.5)
					while True:
						if_dialog = raw_input("Prepare the device. Are you ready? (Y/N) ")			
						if if_dialog.lower() == "y":
							time.sleep(0.5)
							print("Measuring...")
							time.sleep(0.2)
							putin.input()
						if if_dialog.lower() == "n":
							time.sleep(0.5)
							self.userinterface()
						time.sleep(0.5)
						print("Invalid argument.")
						time.sleep(0.5)
				time.sleep(0.5)
				print("Invalid argument.")
				time.sleep(0.5)					
		elif dialog1.lower() == "n":
			while True:
				print("Shutting down...")
				time.sleep(0.5)
				sys.exit(0)
		else:
			time.sleep(0.5)
			print("Invalid argument.")
			time.sleep(0.5)
			self.userinterface()

#	Luokka Input sis‰lt‰‰ varsinaisen sensorin kanssa kommunikoimisen. Se m‰‰ritt‰‰, mitk‰ 
#	pinnit 	ovat k‰ytˆss‰ laudalta, varsinaisen pulssin aktivoimisen ja laskee ultra‰‰nest‰ ‰‰nen 
#	nopeuden avulla sensorin ja kohteen v‰lisen et‰isyyden.
class Input:
	def input(self):
		measure = Measurement()
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18,GPIO.OUT)
		GPIO.setup(23,GPIO.IN)
		GPIO.output(18, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(18, True)
		time.sleep(0.00001)
		GPIO.output(18, False)
		while GPIO.input(23) == 0:
			signaloff = time.time()
		while GPIO.input(23) == 1:
			signalon = time.time()
		timepassed = signalon - signaloff
		distance = timepassed * 170
		GPIO.cleanup()
		measure.measurement(distance)

class Measurement:
	def measurement(self, sensor):
		face = UI()
		time.sleep(0.5)
		if face.unit.lower() == "m":
			print("Distance measured: " + str("%.2f" % sensor) + " m")
		if face.unit.lower() == "f":
			feet = math.floor((sensor*3.2808))
			inches = (((sensor*3.2808) - feet) * 12)
			print("Distance measured: " + str("%.0f" % feet) + " ft " + str("%.0f" % inches) + " in")
		time.sleep(0.5)
		self.remeasure()

#	Luokka Measurement k‰‰nt‰‰ ja tulostaa sensorista saadun metrim‰‰r‰n kahden desimaalin 
#	tarkkuudelle, jos mitataan metreiss‰. Jos mitataan jaloissa, se tulostaa annetun 
#	metrim‰‰r‰n jaloiksi ja tuumiksi k‰‰nnettyn‰. T‰m‰ luokka hallitsee myˆs uudelleenmittauksen 
#	k‰yttˆliittym‰‰ ja suorituksen hallitun lopettamisen mittauksen p‰‰tteeksi.
	def remeasure(self):
		putin2 = Input()
		while True:
			dialog2 = raw_input("Would you like to measure again? (Y/N) ")
			if dialog2.lower() == "y":
				time.sleep(0.5)
				print("Measuring...")
				time.sleep(0.2)
				putin2.input()
			if dialog2.lower() == "n":
				time.sleep(0.5)
				print("Shutting down...")
				time.sleep(0.5)
				sys.exit(0)
			time.sleep(0.5)
			print("Invalid argument.")
			time.sleep(0.5)

#	Main-metodi suoritetaan ohjelmassa ensin. Pythonissa sit‰ ei tarvitse, mutta se on nyt
#	olemassa selkeyden vuoksi. Se luo UI-olion ja k‰ynnist‰‰ sen userinterface-metodin.
def main():
	ui = UI()
	ui.userinterface()
	
main()