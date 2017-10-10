import ghome

led = Device('light', 1)

devices = [led]

assi = ghomeAssistant(devices)

assi.start_listening()
