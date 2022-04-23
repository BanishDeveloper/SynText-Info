import numpy
import json
from colorama import *
from replit import *
from time import sleep as wait
from time import time as watch
from getkey import *

#holy thats alot of modules right there
def keyDown(key):
	realKey = key
	if type(key) is str:
		realKey = key.lower()
	if getkey().lower() == realKey:
		return True
	else: 
		return False

def playFrames(array):
	for i in array:
		print(i[0])
		wait(i[1])
		clear()

def shakeText(text,length = 5,delay = 0.1, amount = 1):
	for i in range(0,int(length/delay)):
		space = ""
		for z in range(0,int(amount-i%(amount+1))):
			space += " "
		print(space + text)
		wait(delay)
		clear()

def strike(text):
	result = ''
	for c in text:
		result = result + c + '\u0336'
	return result

def colorText(text,r=0,g=0,b=0):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def jumpText(text,length=2,delay=0.1,jumpAmount=2):
	for i in range(0,int(length/delay)*jumpAmount):
		jumps = ""
		for z in range(0,int(jumpAmount-i%(jumpAmount+1))):
			jumps += "\n"
		print(jumps + text)
		wait(delay/jumpAmount)
		clear()

def fileData(file):
	f = open(file)
	try:
		return json.load(f)
	except:
		f = open(file, "r")
		return f.read()
def strToJson(string):
	if type(string) == str:
		return json.loads(string) 

def overwriteFile(file, data = ""):
	try:
		f = open(file, "w")
		f.write(data)
	except: return
# useful json wow!
