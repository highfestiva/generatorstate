#!/usr/bin/env python

import time

class State:
	"Write your state machine using a generator function, and you're done before you can say 'yield'!"
	def __init__(self, func, intermission=0):
		self.func = func
		self.args = None
		self.intermission = intermission

	def tick(self, *args):
		if self.args != args:
			self.args = args
			self.func_generator = self.func(*self.args)

		time.sleep(self.intermission)
		try:
			return next(self.func_generator)
		except StopIteration:	# State machine made a return instead of a yield to make us start over state machine.
			self.func_generator = self.func(*self.args)
		except Exception as e:
			self.func_generator = self.func(*self.args)
			raise e
