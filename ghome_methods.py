playShell = None
IR_CONTROL = False

_devices = []

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

def processCommand( s) :
	sp = s.split(' ', 1)

	if sp[0].lower() == 'play' :
		play(sp[1])

	elif sp[0].lower() == 'turn' :
		x = sp[1].split(' ', 1)
		if x[0].lower() == 'on' or x[0].lower() == 'off' :
			b = False
			for device in _devices :
				if device.name == x[1] :
					device.turn(x[0].lower())
