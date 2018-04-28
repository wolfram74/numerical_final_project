import classes
import data_utils
import class_helpers
import time

def relaxer():
    system = classes.System(
        width=500./3., height=200./3.0,
        drag_coeff=.1, buffer_width=10.0,
        frequency=138
        )
    class_helpers.system_with_density(system, .25)
    loops = 2
    print(len(system.particles))
    t0 = time.time()
    data_utils.save_state_data(system)
    for i in xrange(loops):
        system.time_step()
        print(i)
        print(system.particles[0].neighbor_ids)
        print(system.particles[2].neighbor_ids)
        print(system.particles[305].neighbor_ids)
        # data_utils.save_state_data(system)
    tf = time.time()
    delta_t = tf-t0
    print('%f to take %d steps' % (delta_t, loops))


if __name__ == '__main__':
    relaxer()
