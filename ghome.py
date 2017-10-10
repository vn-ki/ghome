import argparse
import os.path
import json

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file


#
import RPi.GPIO as GPIO
import time
from gtts import gTTS
import subprocess
#

playShell = None
IR_CONTROL = False

class Device :
	def __init__(self, name, pin) :
		self.name = name
		self.pin = pin

	def turnOn(self, s) :
		if s == 'on' :
			GPIO.output(self.pin, 1)
			str = " turned on"
			str =  self.name + str
			tts = gTTS(text = str, lang='en', slow=False)
			tts.save(".temp.mp3")
        	        #Play the mp3
					subprocess.run('vlc .temp.mp3'.split())
					#
		elif s == 'off' :
			GPIO.output(device.pin, 0)
			str = " turned off"
			str =  self.name + str
			tts = gTTS(text = str, lang='en', slow=False)
			tts.save(".temp.mp3")
        	        #Play the mp3
					subprocess.run('vlc .temp.mp3'.split())
    	            #

class ghomeAssistant :
	Devices = []

	def __init__(self, devices, IREnabled = False) :

		#Code from google's hotword.py
		parser = argparse.ArgumentParser(
		formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('--credentials', type=existing_file,
					metavar='OAUTH2_CREDENTIALS_FILE',
					default=os.path.join(
						os.path.expanduser('~/.config'),
						'google-oauthlib-tool',
						'credentials.json'
					),
					help='Path to store and read OAuth2 credentials')
		args = parser.parse_args()
		with open(args.credentials, 'r') as f:
			credentials = google.oauth2.credentials.Credentials(token=None, **json.load(f))
		#

		self.assistant = Assistant(credentials)

		GPIO.setmode(GPIO.BCM)  #Sets numbering to BCM
		GPIO.setwarnings(False)  #Done so that Pi doesnt raise a runtime warning since GPIO.cleanup() isn't called

		self.Devices = devices

		for device in self.Devices :
			GPIO.setup(device.pin, GPIO.OUT)

		IR_CONTROL = IREnabled

	def _processCommand(self, s) :
		sp = s.split(' ', 1)

		if sp[0].lower() == 'play' :
			play(sp[1])

		elif sp[0].lower() == 'turn' :
			x = sp[1].split(' ', 1)
			if x[0].lower() == 'on' or x[0].lower() == 'off' :
				b = False
				for device in self.Devices :
					if device.name == x[1] :
						device.turn(x[0].lower())

	def start_listening(self) :
		for event in assistant.start() :
			if event.type == EventType.ON_RECONGNIZING_SPEECH_FINISHED :
				assistant.stop_conversation()
				_processCommand(event.args['text'])

	def addDevice(device) :
		self.Devices += [device]




def play(s) :

	# Idea for not closing mpsyt so that startup time is considerably reduced is borrowed from
	# project by mikerr on raspberrypi.org
	# Visit https://www.raspberrypi.org/forums/viewtopic.php?f=114&t=182665 for more details
	
	if(playShell == None)
		playShell = subprocess.Popen("mpsyt", stdin = subprocess.PIPE, stdout=subprocess.PIPE)


	sp = s.rsplit(' ', 1)
	cmd = ""

	if sp[-1].lower() == 'playlist' :
		cmd += '//'
		cmd += sp[0]
		cmd += "\n1\nall\n"

	else :
		cmd += '/'
		cmd += sp[0]
		cmd += "\n1\n"
	
	playShell.stdin.write(bytes(cmd, 'utf-8'))
	playShell.stdin.flush()

	if IR_CONTROL is True :
		#IR remote control
		
	else :
		#Wait for input for now
		input()

	subprocess.run('pkill vlc'.split())
