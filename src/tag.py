from enum import Enum

class Tag(Enum):
    # TAG = (X,Y,Z)
    # X times views
    # Y times video_length time peak
    # Z times vide_length standard deviation

    SPORTS = (0.8, 1.2, 2.5)
    NEWS = (1.1, 1, 0.75)
    GAMING = (1, 1.2, 1.1)
    FUNNY = (1.1, 1.5, 1)
    DOCUMENTARY = (0.6, 1.5, 2)
    COOKING = (1.2, 1.5, 1.5)
    SCIENCE = (0.9, 1, 1.75)

    HIT = (5, 1, 2)
    MISS = (0.3, 1, 2)
