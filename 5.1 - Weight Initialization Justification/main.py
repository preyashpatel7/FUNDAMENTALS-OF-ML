import neural_network as nn

weighted_sum = 1000 * 10
print("Sigmoid value at value 10 : " + str(nn.sigmoid(weighted_sum)))
print("Sigmoid gradient value at value 10 : " + str(nn.sigmoid_gradient(nn.sigmoid(weighted_sum))))