import random
import classes
import numpy

def system_with_density(system, density):
    area = system.area()
    particle_quantity = int(area*density)
    for part_id in range(particle_quantity):
        state = numpy.zeros(4)
        x_val = random.random()*system.width
        y_val = random.random()*(
            system.height-2*system.buffer_width
            )+system.buffer_width
        state[:2] = [x_val, y_val]
        system.add_particle(classes.Particle(state=state))

def load_data(file_address):
    file_data = open(file_address, 'r')
    states = []
    for line in file_data:
        values = [float(ele) for ele in line.split()]
        states.append(values[:])
    return states

def load_state_from_file(system, file_address):
    states = load_data(file_address)
    for state_in in states:
        state = numpy.zeros(4)
        state[:] = state_in
        system.add_particle(classes.Particle(state=state))
