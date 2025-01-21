import numpy as np

# good results at dt = 0.15 , 0.2 , 0.3, after 0.5 the simulation results in an error
class Particle:
	def __init__(self, x, y):
		self.pos = np.array([x, y])
		self.mass = 1
		self.force = np.array([0, 0])
		self.velocity = 0
		self.acc = 0
		self.dt = 0.2 

	def update(self):
		self.acc = self.force / self.mass
		self.velocity += (self.acc * self.dt)
		self.pos += (self.velocity * self.dt)
		if self.pos[1] > 2:
			self.pos[1] = 2


	def add_force(self, f):
		self.force = self.force + f