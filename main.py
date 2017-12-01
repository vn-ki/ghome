#!/bin/python3

import ghome

led = Device('light', 1)

devices = [led]

assi = ghomeAssistant(devices, botUsername='', botPassword='')

assi.start_listening()
