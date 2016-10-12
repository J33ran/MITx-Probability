import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from scipy.misc import comb

def binomial (n, k, p):
    #return ncr(n, k) * p**k * (1-p)**(n-k)
    return comb(n,k) * p**k * (1-p)**(n-k)


S = np.arange(1,5)
C = np.arange(0, 2*S.size+1)


prob_s = [1/4] *4
print('--- prob_s ---')
print(prob_s)

prob_c_s = np.array([[1/(2*i + 1) for j in C] for i in S])
print('--- prob_c_s ---')
print(prob_c_s)

d = 2
q = .5

prob_d_s = np.array([binomial(i, d, q) for i in S] )
print('--- prob_d_s ---')
print(prob_d_s)

prob_c_and_d_and_s = np.zeros(prob_c_s.shape)

for i, value in enumerate(prob_c_s):
    prob_c_and_d_and_s[i] = value * prob_d_s[i] * prob_s[i]

print('--- prob_c_and_d_and_s ---')
print(prob_c_and_d_and_s)

prob_c_and_d = np.sum(prob_c_and_d_and_s, axis = 0) 
print('--- prob_c_and_d ---')
print(prob_c_and_d)

prob_d = np.sum(prob_c_and_d, axis= 0)
print('--- prob_d ---')
print(prob_d)

prob_c_d = prob_c_and_d/prob_d 
print('--- prob_c_d ---')
print(prob_c_d)

expectation_c_d = np.sum([c * prob_c_d for c in C])

print('--- expectation_c_d ---')
print(expectation_c_d)

# print(prob_c_s)
# print(prob_c_s.shape)





exit(0)
#########################################
joint_prob_XY = np.array([[0.10, 0.09, 0.11], [0.08, 0.07, 0.07], [0.18, 0.13, 0.17]])

prob_X = joint_prob_XY.sum(axis=1)
prob_Y = joint_prob_XY.sum(axis=0)

joint_prob_XY_indep = np.outer(prob_X, prob_Y)

div_XY = [[joint_prob_XY[i,j] * np.log2(joint_prob_XY[i,j]/joint_prob_XY_indep[i,j])
    for i in np.arange(3)]  for j in np.arange(3)]


print(np.sum(np.sum(div_XY), axis = 0))