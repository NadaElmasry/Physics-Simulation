import numpy as np
# good results at k = 0.08, 0.2, not soo good at k - 1.5. 
# good results at c = 0.02, 0.05, too slow at 0.1
class Spring:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.rest_length = np.linalg.norm(p1.pos - p2.pos)
		self.k = 0.9
		self.c = 0.02

	def apply_force(self):
		direction = self.p2.pos - self.p1.pos
		current_length = np.linalg.norm(direction)
		displacement = current_length - self.rest_length
		force = (self.k *displacement * direction) / current_length
		damping_p1 = -self.c * self.p1.velocity
		damping_p2 = -self.c * self.p2.velocity
		self.p1.add_force(force + damping_p1)
		self.p2.add_force(-force +damping_p2)

