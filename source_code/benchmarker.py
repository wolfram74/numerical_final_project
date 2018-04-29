import classes
import time
import class_helpers

def cell_maker(system):
    loops = 10
    task = 'cell list making'
    t0 = time.time()
    for trial in range(loops):
        system.populate_cell_list()
    tf = time.time()
    print('%f seconds per call on %s' % ((tf-t0)/loops, task))
def time_step(system):
    loops = 10
    task = 'cell list making'
    t0 = time.time()
    for trial in range(loops):
        system.time_step()
    tf = time.time()
    print('%f seconds per call on %s' % ((tf-t0)/loops, task))



def main():
    system = classes.System(
        width=500./3., height=200./3.0,
        drag_coeff=.01, buffer_width=10.0,
        frequency=139, time =1.0,
        step_size=.05
        )
    last_state= './w_167_h_77.txt'
    class_helpers.load_state_from_file(system, last_state)
    # cell_maker(system)
    time_step(system)

    return

if __name__ =='__main__':
    main()
