from upgrade import Upgrade
import examples

def gen_dominance(upgrades):
    costs = [u.name for u in sorted(upgrades, key=lambda u: u.cost)]
    rois = [u.name for u in sorted(upgrades, key=lambda u: u.roi)]

    # TODO: Update this to be a lot more efficient... not O(n^2)
    table = {}
    for i, u in enumerate(costs):
        more_expensive = set(costs[i+1:])
        slower_roi = set(rois[rois.index(u)+1:])

        table[u] = more_expensive & slower_roi

    return table

if __name__ == "__main__":
    upgrades = examples.gen_random(5)
    
    print(*[f"Name: {u.name} | Cost: {u.cost} | ROI: {u.roi}" for u in upgrades], sep='\n')
    print(*gen_dominance(upgrades).items(), sep="\n")
