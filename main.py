import numpy as np
#while True:
#    point = input('Insert the x,y coordinates to find the potencial in the point separating with ",": "x,y", or leave' +
#                  'it blank to end the program.')
#    if not point:
#        break#
#
#    point = list(map(float, point.split(",")))
#   print(point)

A = np.array([[1,0,0,0],[-0.7786,1.25,-0.4571,-0.0143], [0,0,1,0], [-0.4571,-0.0143,-0.3667,0.8381]])
b = np.array([0,0,10,0])
x = np.linalg.solve(A,b)
print(x)