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

from ghome_methods import *
import threading
#

class ghomeAssistant :


	def __init__(self, devices, IREnabled = False, botUsername, botPassword) :

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

		_devices = devices

		for device in _devices :
			GPIO.setup(device.pin, GPIO.OUT)

		IR_CONTROL = IREnabled

		self.bot = ghomeBot(botUsername, botPassword);

		self.botThread = threading.Thread(bot.listen)


	def start_listening(self) :
		self.botThread.start()
		for event in assistant.start() :
			if event.type == EventType.ON_RECONGNIZING_SPEECH_FINISHED :
				assistant.stop_conversation()
				processCommand(event.args['text'])

	def addDevice(device) :
		_devices += [device]
