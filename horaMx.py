import datetime
import time
import calendar

class mexTime:
	
	def __init__(self):
		self.array = []
		self.parseTime()

	def parseTime(self):
		utcTime = datetime.datetime.now()
		mexTime = str( utcTime + datetime.timedelta(hours=-5) )
		cadena = ""
		j = 0
		for i in range(0, len(mexTime)):

			if (i >= 0 and i <= 3) or (i >= 5  and i<= 6) or (i >= 8 and i<= 9) or (i >= 11 and i<= 12) or (i >= 14 and i<= 15):
				cadena = cadena + mexTime[i]

			if mexTime[i] == "-" or mexTime[i] == " " or mexTime[i] == ":":
				self.array.insert(j, cadena)
				cadena = ""
				j = j + 1

	def getAno(self):
		return self.array[0]
		
	def getMes(self):
		return self.array[1]

	def getDia(self):
		return self.array[2]

	def getHora(self):
		return self.array[3]

	def getMinuto(self):
		return self.array[4]