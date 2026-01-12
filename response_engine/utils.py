import random


def choose_random(items: list):
    if not items:
        return None
    return random.choice(items)
