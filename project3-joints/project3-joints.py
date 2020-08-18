import pyrosim
print(1)
sim = pyrosim.Simulator(play_paused=True)

whiteObject = sim.send_cylinder(x=0, y=0, z=0.6, length=1.0,radius=0.1)
redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, r1=0,r2=1,r3=0, r=1,g=0,b=0)
joint = sim.send_hinge_joint(first_body_id = whiteObject, second_body_id = redObject, x = 0, y= 0, z = 1.05, n1 = -1, n2 = 0, n3 = 0)
sim.start()
sim.wait_to_finish()