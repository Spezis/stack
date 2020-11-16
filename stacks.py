def Menu(): 
	print('Hinweis: ohne den jeweils vorherigen Punkt können die folgenden nicht korrekt ausgeführt werden!\n')
	menu = int(input('Was soll aufgerufen werden? \nneuerStack [1]\nablegen    [2]\nausgeben   [3]\nlöschen    [4]\n-> '))
	if menu == 1:
		neuerStack()
	elif menu == 2:
		ablegen()
	elif menu == 3:
		ausgeben()
	elif menu == 4:
		löschen()
	else:
		print('\nDiese Funktion existiert nicht\n')

def neuerStack():
	global Liste
	Liste = [] # neuer Stack
	print('neuer Stack:', Liste)
	g = str(input('\nfortfahren? (j/n): '))
	if g == 'j':
		ablegen()
	elif g == 'n':
		return 'break'

def ablegen():
	Abbruch = 0
	global counter
	counter = 0
	global Liste
	while Abbruch == 0:
		a = (input('neues Element: '))
		if a == 'f':
			print('Stack: ', Liste)
			h = str(input('\nfortfahren? (j/n) '))
			if h == 'j':
				ausgeben()
				Abbruch = 1
			elif h == 'n':
				Abbruch = 1
				return 'break'
			else:
				print('break')
		else:
			Liste += a
			counter += 1

def ausgeben():
	global counter
	global Liste
	Abbruch = 0
	while Abbruch == 0:
		Ausgabe = str(input('letztes Element ausgeben lassen? (j/n): '))
		if Ausgabe == 'n':
			print('break')
		elif Ausgabe == 'j':
			if counter >= 1:
				print(Liste[counter -1:counter])
				counter -= 1
			else:
				print('\nStack leer oder nicht vorhanden')
				i = str(input('mit löschen fortfahren? (j/n): '))
				if i == 'j':
					löschen()
					Abbruch = 1
				elif i == 'n':
					print('break')
					Abbruch = 1

def löschen():
	global Liste
	del Liste
	return 'break'

print(Menu())
