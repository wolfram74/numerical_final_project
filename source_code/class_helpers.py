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
