import os

def vec_as_string(vec):
    return ("%f "*len(vec)+'\n') % tuple(vec)


def save_state_data(system):
    folder = str(system)
    folder_address = '../produced_data/%s' % folder
    folder_exists = os.path.exists(folder_address)
    if not folder_exists:
        os.makedirs(folder_address)
    file_name = "t_%.2f.txt" % system.time
    file_out = open(
        '%s/%s' % (folder_address, file_name),
        'w'
        )
    for particle in system.particles:
        file_out.write(vec_as_string(particle.state))
