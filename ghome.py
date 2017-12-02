
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
from fb_listener import *
#

print(EventType.ON_RECOGNIZING_SPEECH_FINISHED)

class ghomeAssistant :


	def __init__(self, devices, botUsername, botPassword, IREnabled = False) :

		GPIO.setmode(GPIO.BCM)  #Sets numbering to BCM
		GPIO.setwarnings(False)  #Done so that Pi doesnt raise a runtime warning since GPIO.cleanup() isn't called

		_devices = devices

		for device in _devices :
			GPIO.setup(device.pin, GPIO.OUT)

		IR_CONTROL = IREnabled

		self.bot = ghomeBot(botUsername, botPassword);

		self.botThread = threading.Thread(target=self.bot.listen)


	def start_listening(self) :
		self.botThread.start()
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
		with Assistant(credentials) as assistant :
			for event in assistant.start() :
				if event.type == EventType.ON_START_FINISHED:
					print(event)

				if event.type == EventType.ON_CONVERSATION_TURN_STARTED :
					print("say")

				if event.type == EventType.ON_END_OF_UTTERANCE :
					print("okay")

				if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED :
					if isACustomCommand(event.args['text'])
						assistant.stop_conversation()
					processCommand(event.args['text'])

	def addDevice(self, device) :
		_devices += [device]
