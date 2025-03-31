import numpy as np

input = [1.5,3.5,2.0,4.2]
# weights1 = [3.1,2.5,4.5,3.2]
# weights2 = [3.9,2.2,4.1,3.7]
# weights3 = [3.6,2.1,4.9,3.6]
# bais1= 4
# bais2= 3
# bais3= 2

weights = [[3.1,2.5,4.5,3.2],
             [3.9,2.2,4.1,3.7],
                [3.6,2.1,4.9,3.6]]

baises=[4,3,2]

# output1= np.dot(input,weights1)+bais1
# output2= np.dot(input,weights2)+bais2
# output3= np.dot(input,weights3)+bais3

# output=[output1,output2,output3]

output=np.dot(weights,input)+baises
print(output)