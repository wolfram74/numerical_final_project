
def vec_as_string(vec):
    return ("%f "*len(vec)+'\n') % tuple(vec)


def save_state_data(system):
    folder = str(system)
    file_name = "t_%.2f.txt"
    file_out = open(
        '../produced_data/%s/%s' % (folder, file_name),
        'w'
        )
    for particle in system.particles:
        file_out.write(vec_as_string(particle.state))
