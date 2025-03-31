import numpy as np

x = [[1.5,3.5,2.0,4.2],
         [2.0,1.2,0.5,3.3],
         [2.3,2.6,0.5,0.7]]

class layer_dense:
    def __init__ (self,n_input , n_neurons):
        self.weights = np.random.randn(n_input, n_neurons)
        self.baises =  np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.baises

layer1= layer_dense(4,5)
layer2= layer_dense(5,2)

layer1.forward(x)
print(layer1.output)

layer2.forward(layer1.output)
print(layer2.output)
