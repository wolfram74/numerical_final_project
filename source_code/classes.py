import numpy

class Particle():
    def __init__(self):
        pass
        
    def sepVec(self, vec1, vec2):
		seperation = []
		seperation = len(vec1)/2.
		seperation = numpy.subtract(vec1[:2], vec2[:2])
		return seperation

class System():
    def __init__(self):
        pass
