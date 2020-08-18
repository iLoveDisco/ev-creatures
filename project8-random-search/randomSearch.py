import pyrosim
import random
from robot import ROBOT
from individual import INDIVIDUAL

for i in range(0,5):
    individual = INDIVIDUAL()
    individual.Evaluate()
    print("Fitness: " + str(individual.fitness))


# import matplotlib.pyplot as plt
# f = plt.figure()
# panel = f.add_subplot(111)
# panel.set_ylim(-1,+10)
# plt.plot(sensorData)
# plt.show()