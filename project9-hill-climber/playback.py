from individual import INDIVIDUAL
import pickle
f = open('robot.p', 'rb')
best = pickle.load(f)
best.Evaluate(False)
print(best.fitness)
f.close()