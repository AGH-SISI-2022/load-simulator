import numpy as np

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def normal_distribution(loc, scale, size):
    return max(1, int(np.random.normal(loc=loc, scale=scale, size=size)))