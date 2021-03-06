# import pyrosim
# import random
# import copy
# import math
# import pickle
# from robot import ROBOT
# from individual import INDIVIDUAL

# parent = INDIVIDUAL()
# parent.Evaluate(False)
# print(parent.fitness)

# for i in range(0,100):
#     child = copy.deepcopy( parent )
#     child.Mutate()
#     child.Evaluate(True)
#     if (child.fitness > parent.fitness):
#         parent = child
#         parent.Evaluate(False)
#         f = open('robot.p', 'wb')
#         pickle.dump(parent, f)
#         f.close()
#     print('[g:', i+1,']','[pw: ', parent.genome,']', '[p:' , parent.fitness , '] [c:',child.fitness,']')
    

# # import matplotlib.pyplot as plt
# # f = plt.figure()
# # panel = f.add_subplot(111)
# # panel.set_ylim(-1,+10)
# # plt.plot(sensorData)
# # plt.show()

# Step 57c should come after 62
# Step 100 should be removed
from population import POPULATION
import copy

parents = POPULATION(5)
for g in range(1,9):
    children = copy.deepcopy(parents)
    children.Mutate()

    parents.Evaluate()
    children.Evaluate()

    parents.ReplaceWith(children)

    print(g,end=' ')
    parents.Print()
    print()