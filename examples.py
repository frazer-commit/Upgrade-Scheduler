from upgrade import Upgrade
import numpy as np

rng = np.random.default_rng()

def gen_random(amount=10, noise=0.1):
    upgrades = []

    for i in range(amount):
        cost = np.pow(2, i) * 10
        cost *= 1 + rng.uniform(low=-noise, high=noise)
        
        rate = np.pow(2, i) * 0.1 
        rate *= 1 + rng.uniform(low=-noise, high=noise)

        u = Upgrade(f"Upgrade {i+1}", cost, rate)
        upgrades.append(u)

    return upgrades


if __name__ == "__main__":
    upgrades = gen_random()
    print(*upgrades, sep="\n")
    print(*[u.roi for u in upgrades], sep="\n")
