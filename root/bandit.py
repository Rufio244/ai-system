import random
from collections import defaultdict

# เก็บ performance
stats = defaultdict(lambda: {"count": 0, "reward": 0})

def select(formulas):
    # epsilon-greedy
    epsilon = 0.2

    if random.random() < epsilon:
        return random.choice(list(formulas.keys()))

    # เลือก reward สูงสุด
    best = max(stats.items(), key=lambda x: x[1]["reward"]/max(x[1]["count"],1), default=("balanced", {}))
    return best[0]

def update(name, reward):
    stats[name]["count"] += 1
    stats[name]["reward"] += reward
