import pyrosim
import random
from robot import ROBOT
class INDIVIDUAL:
    def __init__(self):
        self.genome = random.random() * 2 - 1
        self.fitness = 0
        print(self.genome)

    def Evaluate(self):
        sim = pyrosim.Simulator()
        robot = ROBOT(sim, self.genome)
        sim.start()
        sim.wait_to_finish()

        x = sim.get_sensor_data(sensor_id=robot.P4, svi=0)
        y = sim.get_sensor_data(sensor_id=robot.P4, svi=1)
        z = sim.get_sensor_data(sensor_id=robot.P4, svi=2)

        self.fitness = y[-1]

