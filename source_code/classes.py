import numpy
import random

class Particle():
    def __init__(self, state=numpy.zeros(4), index=None, system=None):
        self.state = state
        self.index = index
        self.system = system
        self.kernels = numpy.zeros([5,4])
        self.neighbor_ids = []

    def sepVec(self, vec1, vec2):
        return vec1[:2] - vec2[:2]

    def set_positions(self, x_position, y_position):
        self.state[:2]=[x_position, y_position]

    def set_system(self, input_system):
        self.system=input_system

    def cell_address(self):
        x_index = int(self.state[0]/self.system.cell_length)
        y_index = int(self.state[1]/self.system.cell_length)
        return [x_index, y_index]

class System():
    def __init__(self,
            width=100, height=100,
            drag_coeff=.01, buffer_width=10.0,
            amplitude=0.0, frequency=3.14, angle=0.0,
            time_step=0.01, cell_length=2.
            ):
    #angle off of y axis
        self.width = width
        self.height = height
        self.drag_coeff = drag_coeff
        self.buffer_width = buffer_width
        self.cell_length = cell_length
        self.time_step = time_step
        self.particles = []
        self.amplitude = amplitude
        self.frequency = frequency
        self.angle = angle

    def add_particle(self, particle):
        particle.set_system(self)
        particle.index = len(self.particles)
        self.particles.append(particle)

    def create_particle(self):
        place_x=random.random()*self.width
        place_y=random.random()*self.height
        particle_to_place=Particle()
        particle_to_place.set_position(place_x,place_y)
        particle_to_place.set_system(self)
        self.add_particle(particle_to_place)

    def populate_cell_list(self):
        pass
        x_cells = int(self.width/self.cell_length)+1
        y_cells = int(self.height/self.cell_length)+1
        self.cell_list = [[
            [] for x_ind in range(x_cells)
        ] for y_ind in range(y_cells)]
