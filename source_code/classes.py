import numpy
import random

class Particle():
    def __init__(self, state=None, index=None, system=None):
        if state:
            self.state = state
        else:
            self.state = numpy.zeros(4)
        self.index = index
        self.system = system
        self.kernels = numpy.zeros([5,4])
        self.neighbor_ids = []

    def sepVec(self, vec1, vec2):
        seperation = vec1[:2] - vec2[:2]
        if self.system:
            seperation[0] %= self.system.width #imposing periodic boundary along x
        return seperation

    def set_positions(self, x_position, y_position):
        self.state[:2]=[x_position, y_position]

    def set_system(self, input_system):
        self.system=input_system

    def cell_address(self):
        x_index = int(self.state[0]/self.system.cell_length)
        y_index = int(self.state[1]/self.system.cell_length)
        return [x_index, y_index]

    def populate_neighbor_ids(self):
        col, row = self.cell_address()
        system = self.system
        self.neighbor_ids = []
        margin = 2
        col_max = len(system.cell_list[0])-1
        row_max = len(system.cell_list)-1
        for col_index in range(col-margin, col+margin+1):
            for row_index in range(row-margin, row+margin+1):
                if row_index > row_max or row_index < 0:
                    continue
                inspect_row = row_index
                inspect_col = col_index%(col_max+1)
                self.neighbor_ids += system.cell_list[inspect_row][inspect_col]
        self.neighbor_ids.remove(self.index)

    def interaction_force(self, state1, state2):
        force = numpy.zeros(4)
        seperation = self.sepVec(state1, state2)
        radius = numpy.linalg.norm(seperation)
        decay = numpy.exp(-radius)
        force[2:] = -seperation/(radius**3)
        return force*decay

    def set_working_state(self, kernel_num):
        modifier = [0, 1.0, .5, .5, 1.0]
        # print('working state set')
        # print(self.kernels[kernel_num-1]*modifier[kernel_num])
        self.working_state = self.state + (
            self.kernels[kernel_num-1]*modifier[kernel_num]
            )

    def total_force(self):
        output = numpy.zeros(4)
        output += self.system.confinement_force(self.working_state)
        output += self.system.drag_force(self.working_state)
        for neighbor_id in self.neighbor_ids:
            output += self.interaction_force(
                self.working_state,
                self.system.particles[neighbor_id].working_state
                )
        return output

class System():
    def __init__(self,
            width=100, height=100,
            drag_coeff=.01, buffer_width=10.0,
            amplitude=0.0, frequency=3.14, angle=0.0,
            step_size=0.01, cell_length=2.,
            time=0.0
            ):
    #angle off of y axis
        self.width = width
        self.height = height
        self.drag_coeff = drag_coeff
        self.buffer_width = buffer_width
        self.cell_length = cell_length
        self.step_size = step_size
        self.particles = []
        self.amplitude = amplitude
        self.frequency = frequency
        self.angle = angle
        self.time = time
        self.working_time = None

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
        x_cells = int(numpy.ceil(self.width/self.cell_length))
        y_cells = int(numpy.ceil(self.height/self.cell_length))
        self.cell_list = [[
            [] for x_ind in range(x_cells)
        ] for y_ind in range(y_cells)]
        for particle in self.particles:
            col, row = particle.cell_address()
            self.cell_list[row][col].append(particle.index)
        for particle in self.particles:
            particle.populate_neighbor_ids()

    def confinement_force(self, state):
        force = numpy.zeros(4)
        y = state[1]
        force[3] = -(
            numpy.exp(self.buffer_width - self.height + y)
            -numpy.exp(self.buffer_width - y)
            )
        return force

    def drag_force(self, state):
        force = numpy.zeros(4)
        force[2:] = -self.drag_coeff*state[2:]
        return force

    def set_working_time(self, kernel_num):
        modifier = [0, 0.0, .5, .5, 1.0]
        self.working_time = self.time+self.step_size*modifier[kernel_num]

    def time_step(self):
        self.populate_cell_list()
        for particle in self.particles:
            particle.kernels = numpy.zeros([5,4])
        for kernel_num in range(1, 5):
            self.set_working_time(kernel_num)
            for particle in self.particles:
                particle.set_working_state(kernel_num)
            for particle in self.particles:
                net_force = particle.total_force()
                particle.kernels[kernel_num][:2] = particle.working_state[2:]
                particle.kernels[kernel_num] += net_force
                particle.kernels[kernel_num]*= self.step_size
        for particle in self.particles:
            particle.state += 6**(-1)*(
                particle.kernels[1]+
                2.*particle.kernels[2]+
                2.*particle.kernels[3]+
                particle.kernels[4]
                )
        self.time+=self.step_size
