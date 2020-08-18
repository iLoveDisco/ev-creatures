import pyrosim
import random
import math
import numpy
from robot import ROBOT
class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = numpy.random.random(4) * 2 - 1
        self.fitness = 0
        
    def Evaluate(self, pb):
        self.Start_Evaluation(pb)
        self.Compute_Fitness()

    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator(play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
        self.fitness = y[-1]
        del self.sim

    def Mutate(self):
        geneToMutate = random.randint(0, 3)
        self.genome[geneToMutate] = random.gauss( self.genome[geneToMutate] , math.fabs(self.genome[geneToMutate]) )

    def Print(self):
        print('[',end='')
        print(self.ID,end=' ')
        print(self.fitness,end='')
        print('] ',end='')