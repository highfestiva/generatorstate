#!/usr/bin/env python3

from generatorstate import State

def alarm_active():
	return eval(input('  Alarm active (1/0)? ') or '1')

def alarm_sensor_detecting_something():
	return eval(input('  Burglar in da haus (1/0)? ') or '1')

def alarm_main():
	print('Alarm not turned on.')
	while not alarm_active():
		yield	# yield resumes in the next timeslice.
	print('Alarm turned on, waiting for burglar.')
	while alarm_active():
		if alarm_sensor_detecting_something():
			print('FAT BEEP! (Waiting 10 seconds to wake the neighbours up.)')
			for _ in range(10): yield
			print('Siren turned off. Resetting alarm.')
			return # Returning restarts this function.
		yield

print('Acme Alarm Software v9.3')
tick = State(alarm_main, intermission=1)
while True:
	tick()
