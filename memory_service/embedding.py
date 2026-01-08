import random

def generate_embedding(payload):
    random.seed(len(str(payload)))
    return [random.random() for _ in range(128)]
