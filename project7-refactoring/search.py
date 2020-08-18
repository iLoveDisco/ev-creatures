import pyrosim
import random
from robot import ROBOT

for i in range(0,3):
    sim = pyrosim.Simulator()
    robot = ROBOT(sim, random.random() *2 - 1)
    sim.start()
    sim.wait_to_finish()

# sensorData = sim.get_sensor_data(sensor_id = P2)
# print(sensorData)

# import matplotlib.pyplot as plt
# f = plt.figure()
# panel = f.add_subplot(111)
# panel.set_ylim(-1,+10)
# plt.plot(sensorData)
# plt.show()