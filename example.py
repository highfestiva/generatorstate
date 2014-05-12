#!/usr/bin/env python3

from generatorstate import State

def state_machine_tick():
	import os
	for path,directories,files in os.walk('/'):
		for filename in files:
			filename = os.path.join(path,filename)
			print(filename)
			yield	# yield resumes after next timeslice.
			if filename.endswith('txt'):
				print('Found a text file:')
				yield
				try:
					for line in open(filename, 'rt'):
						print(line)
						yield
				except:
					print('All the error handling you could ever want!')
					yield
	print('Nice one! Restarting from root again.')
	# Returning from the state machine (as opposed to yielding) restarts the state machine from scratch.

ticker = State(state_machine_tick, intermission=0.2)
while True:
	ticker.tick()
