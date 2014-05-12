#!/usr/bin/env python3

from generatorstate import State

def print_files_state_machine_main():
	'This is the state machine. yield waits for the next tick, return restarts.'
	import os
	for path,directories,files in os.walk('/'):
		for filename in files:
			filename = os.path.join(path,filename)
			print(filename)
			yield	# yield resumes in the next timeslice.
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
	# Returning from the state machine (as opposed to yielding) restarts the state machine function from scratch.

# Tick through each file, each line, each error using the state machine.
tick_another_file = State(print_files_state_machine_main, intermission=0.2)
while True:
	tick_another_file()
