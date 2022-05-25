import numpy as np
import random
from src.youtuber import YouTuber
from src.tag import Tag

youtubers = [
    YouTuber('PewDiePie', 100, 0.2, 20, 15, [(Tag.GAMING, 0.6), (Tag.FUNNY, 0.3), (Tag.NEWS, 0.1)]),
    YouTuber('Mark Rober', 40, 1.0, 20, 1, [(Tag.SCIENCE, 0.8), (Tag.FUNNY, 0.2)]),
    YouTuber('RATIRL', 10, 0.9, 15, 16, [(Tag.GAMING, 0.9), (Tag.FUNNY, 0.1)]),
    YouTuber('DIY Perks', 25, 0.95, 20, 1, [(Tag.DOCUMENTARY, 0.6), (Tag.SCIENCE, 0.4)]),
    YouTuber('Linus Tech Tips', 60, 0.3, 10, 30, [(Tag.NEWS, 0.5), (Tag.GAMING, 0.4), (Tag.DOCUMENTARY, 0.1)]),
    YouTuber('Uwaga! Naukowy Bełkot', 15, 0.5, 18, 5, [(Tag.SCIENCE, 0.8), (Tag.FUNNY, 0.2)]),
    YouTuber('Thebausffs', 10, 1.0, 11, 12, [(Tag.GAMING, 1.0)]),
    YouTuber('LEC', 10, 0.5, 5, 10, [(Tag.SPORTS, 0.7), (Tag.GAMING, 0.1), (Tag.DOCUMENTARY, 0.1), (Tag.FUNNY, 0.1)]),
    YouTuber('TikTok ABC', 30, 0.8, 1, 50, [(Tag.FUNNY, 0.7), (Tag.COOKING, 0.3)]),
    YouTuber('ilmango', 20, 0.3, 10, 15, [(Tag.GAMING, 0.5), (Tag.NEWS, 0.4), (Tag.DOCUMENTARY, 0.1)]),
]

def get_random_youtuber(youtubers) -> YouTuber:
    return random.choices(youtubers, [yt.upload_rate for yt in youtubers], k=1)[0]

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def normal_distribution(loc, scale, size):
    return max(1, int(np.random.normal(loc=loc, scale=scale, size=size)))

def get_random_tag(video) -> Tag:
    tags = [t for (t, _) in video.youtuber.video_tags]
    tags_chance = [p for (_, p) in video.youtuber.video_tags]
    return random.choices(tags, tags_chance, k=1)[0]

def get_tag_mltprs(tags: list):
    assert len(tags) > 0
    (mult_x, mult_y, mult_z) = (1,1,1)
    for t in tags:
        (x,y,z) = t.value
        mult_x *= x
        mult_y *= y
        mult_z *= z
    return (mult_x/len(tags), mult_y/len(tags), mult_z/len(tags))