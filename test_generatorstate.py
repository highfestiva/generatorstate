#!/usr/bin/env python

from generatorstate import State
import unittest

class GeneratorStateTest(unittest.TestCase):

	def test_yield_3(self):
		def machine(n):
			for _ in range(n):
				yield
			raise IOError
		state = State(machine)
		state.tick(3)
		state.tick(3)
		state.tick(3)
		try: state.tick(3)
		except IOError: return
		assert False, 'Expecting IOError exception, but none was raised!'

	def test_restart(self):
		class Machine:
			def hop(self):
				self.n = 0
				yield
				self.n += 1
		m = Machine()
		state = State(m.hop)
		state.tick()
		assert m.n == 0
		state.tick()
		assert m.n == 1
		state.tick()	# State machine method restarted.
		assert m.n == 0

if __name__ == '__main__':
	unittest.main()
