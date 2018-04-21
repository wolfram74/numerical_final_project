import numpy
import random

class Particle():
    def __init__(self):
        self.state=numpy.zeros(4)
         
    def sepVec(self, vec1, vec2):
		seperation = []
		seperation = len(vec1)/2.
		seperation = numpy.subtract(vec1[:2], vec2[:2])
		return seperation
 
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
