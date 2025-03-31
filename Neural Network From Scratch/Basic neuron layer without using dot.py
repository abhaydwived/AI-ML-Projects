import numpy as np, math

input = [1.5,3.5,2.0,4.2]
# weights = [[3.1,2.5,4.5,3.2],
#              [3.9,2.2,4.1,3.7],
#                 [3.6,2.1,4.9,3.6]]

np.random.seed(78975)       

weights = np.random.randn(3,4)
print("Weights: \n",weights)

baises=[4,3,2]

outputs=[]
for neuron_weights, neuron_bais in zip(weights,baises):
    neuron_ouput=0
    for n_input,weight in zip(input, neuron_weights):
        neuron_ouput += n_input * weight
    neuron_ouput += neuron_bais
    outputs.append(neuron_ouput)

print("Output Layer: \n",outputs)

total_2 = sum(outputs)
probability_2 = [i / total_2 for i in outputs]
print("Probability without using exp: \n",probability_2)
print(probability_2.index(max(probability_2)))

total = sum(list(map(lambda x: math.exp(x), outputs)))
probability = [math.exp(i) / total for i in outputs]
print("Probability with using exp: \n",probability)
print(probability.index(max(probability)))












