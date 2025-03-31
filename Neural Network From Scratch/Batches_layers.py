import numpy as np

inputs = [[1.5,3.5,2.0,4.2],
         [2.0,1.2,0.5,3.3],
         [2.3,2.6,0.5,0.7]]

weights1 = [[3.1,2.5,4.5,3.2],
           [3.9,2.2,4.1,3.7],
           [3.6,2.1,4.9,3.6]]

weights2=[[0.1, -0.14, 0.5],
          [-0.5, 0.12, -0.33],
          [-0.44, 0.73, -0.13]]

baises1=[4,3,2]

baises2=[-1, 2, -0.5]

output_layer1 = np.dot( inputs , np.array(weights1).T ) + baises1
output_layer2 = np.dot( output_layer1 , np.array(weights2).T ) + baises2

print(output_layer1)
print(output_layer2)