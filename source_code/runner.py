import classes
import data_utils
import class_helpers
import time

def relaxer():
    system = classes.System(
        width=500, height=200,
        drag_coeff=.1, buffer_width=10.0,
        frequency=138
        )
    class_helpers.system_with_density(system, .25)
    loops = 10
    t0 = time.time()
    for i in xrange(loops):
        system.time_step()
    tf = time.time()
    delta_t = tf-t0
    print('%f to take %d steps' % (delta_t, loops))


if __name__ == '__main__':
    relaxer()
