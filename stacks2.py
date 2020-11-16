#von Manuel Paul

class stack:
	def Menu(self): 
		print('Hinweis: ohne den jeweils vorherigen Punkt können die folgenden nicht korrekt ausgeführt werden!\n')
		menu = int(input('Was soll aufgerufen werden? \nneuerStack [1]\nablegen    [2]\nausgeben   [3]\nlöschen    [4]\n-> '))
		if menu == 1:
			self.neuerStack()
		elif menu == 2:
			self.ablegen()
		elif menu == 3:
			self.ausgeben()
		elif menu == 4:
			self.löschen()
		else:
			print('\nDiese Funktion existiert nicht\n')
	
	def neuerStack(self):
		self.Liste = [] # neuer Stack
		print('neuer Stack:', self.Liste)
		g = (input('\nfortfahren? (j/n): '))
		if g == 'j':
			self.ablegen()
		elif g == 'n':
			return 'break'
		else:
			print('Fehler-neuerStack-fortfahren')
	
	def ablegen(self):
		Abbruch = 0
		self.counter = 0
		while Abbruch == 0:
			a = (input('neues Element: '))
			if a == 'f':
				print('Stack: ', self.Liste)
				h = (input('\nfortfahren? (j/n) '))
				if h == 'j':
					self.ausgeben()
					Abbruch = 1
				elif h == 'n':
					Abbruch = 1
					return 'break'
				else:
					print('Fehler-ablegen-fortfahren')
					break
			elif len(a) > 1:
				print('Fehler-ablegen-neues Element -> zu viele-Stellen-max.1!!!')
			else:
				self.Liste += a
				self.counter += 1
	
	def ausgeben(self):
		Abbruch = 0
		while Abbruch == 0:
			Ausgabe = str(input('letztes Element ausgeben lassen? (j/n): '))
			if Ausgabe == 'n':
				print('break')
			elif Ausgabe == 'j':
				if self.counter >= 1:
					print(self.Liste[self.counter -1:self.counter])
					self.counter -= 1
				else:
					print('\nStack leer oder nicht vorhanden')
					i = str(input('mit löschen fortfahren? (j/n): '))
					if i == 'j':
						self.löschen()
						Abbruch = 1
					elif i == 'n':
						print('break')
						Abbruch = 1
	
	def löschen(self):
		del self.Liste
		return 'fertig'

Menu = stack()
Menu.Menu()

