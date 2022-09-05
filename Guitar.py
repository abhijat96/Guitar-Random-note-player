import time
import random
from playsound import playsound


scaleMappings = {
					'F': 0,
					'F#': 1, 
					'G': 2, 
					'A flat': 3, 
					'A': 4, 
					'B flat' : 4,
					'B' : 5, 
					'C': 6, 
					'C#': 7, 
					'D': 8, 
					'E flat': 9,
					'E': 10, 
					'F': 11
				 }
def PredictSoundPractice():
	score = 1
	strings = [6,5,4]
	frets = [2,3,4,5,6,7,8,9,10,11,12]
	relativeFrets = [2,3]
	while(True):
		string = random.randint(0,len(strings)-1)
		fret = random.randint(0,len(frets)-1)
		relativeFret = random.randint(0, len(relativeFrets) - 1)
		print( str(score))
		print("Fret: " + str(frets[fret]))
		print("String: " + str(strings[string]))
		print("Relative Fret: " + str(relativeFrets[relativeFret]))
		print("")
		score = score + 1
		time.sleep(10)

def PredictPositionPractice(scale):
	score = 1
	scaleTabs = [[1,3],[0,1,3],[0,2,3],[0,2,3],[1,3],[0,1,3]]
	lastString = -1
	lastFret = -1
	while(True):
		string = random.randint(0,5)
		actualString = 6-string

		fret = scaleTabs[string][random.randint(0,len(scaleTabs[string]) - 1)]
		fret = fret + scaleMappings[scale]

		if((string == lastString) and (fret == lastFret)):
			print("Skipping same note")
			continue
		print("String: " + str(actualString))
		print("Fret: " + str(fret))
		print()

		PlayNote(actualString, fret)
		lastFret = fret
		lastString = string
		time.sleep(1.0)

def PlayNote(string, note):
	playsound('SOUNDS/NOTES/' + str(string) + "_" + str(note) + ".mp3")

# PredictSoundPractice()
PredictPositionPractice('A')
