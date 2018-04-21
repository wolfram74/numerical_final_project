import numpy
import random

class Particle():
    def __init__(self):
        self.state=numpy.zeros(4)
         
    def sepVec(self, vec1, vec2):
		return vec1[:2] - vec2[:2]
 
    def set_positions(self, x_position, y_position):
        self.state[:2]=[x_position, y_position]



class System():
    def __init__(self,width=100,height=100):
        self.width=width
        self.height=height
        self.particle=[]
    def add_particle(self):
        place_x=random.random()*self.width
        place_y=random.random()*self.height
        particle_to_place=Particle()
        particle_to_place.set_position(place_x,place_y)

	def drag_force(self, vec1):
		system = classes.System(drag_coeff = .1)
		drag_force = drag_coeff * state[3]
		force = - system.drag_force(state)
		return force
		
		'''
		system = classes.System(drag_coeff = .1)
        state = numpy.array([0.0, 0.0, 0.0, random.random()*50-25])
        
        self.assertEqual(0.0, force[2])
        self.assertTrue(0.0 > force[3]*state[3])
        '''
