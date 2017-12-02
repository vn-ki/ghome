#!/usr/bin/ python3

import ghome

led = ghome.Device('light', 1)

devices = [led]

assi = ghome.ghomeAssistant(devices, botUsername='iamafbbot@gmail.com', botPassword='iamabot123')

assi.start_listening()
