import numpy as np
import random
from src.youtuber import YouTuber

def get_random_youtuber(youtubers) -> YouTuber:
    return random.choices(youtubers, [yt.upload_rate for yt in youtubers], k=1)[0]

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def normal_distribution(loc, scale, size):
    return max(1, int(np.random.normal(loc=loc, scale=scale, size=size)))