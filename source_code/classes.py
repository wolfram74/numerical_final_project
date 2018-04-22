import numpy
import random

class Particle():
    def __init__(self):
        self.state=numpy.zeros(4)
        self.system=None
    
    def sepVec(self, vec1, vec2):
        return vec1[:2] - vec2[:2]
 
    def set_positions(self, x_position, y_position):
        self.state[:2]=[x_position, y_position]

    def set_system(self, input_system):
        self.system=input_system



class System():
    def __init__(self,width=100,height=100):
        self.width=width
        self.height=height
        self.particles=[]
        
    def add_particle(self, particle):
        particle.set_system(self)
        self.particles.append(particle)
        
    def create_particle(self):
        place_x=random.random()*self.width
        place_y=random.random()*self.height
        particle_to_place=Particle()
        particle_to_place.set_position(place_x,place_y)
        particle_to_place.set_system(self)
        self.particles.append(particle_to_place)
