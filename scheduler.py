from upgrade import Upgrade
import examples
import copy

def gen_dominance(upgrades):
    costs = [u.name for u in sorted(upgrades, key=lambda u: u.cost)]
    rois = [u.name for u in sorted(upgrades, key=lambda u: u.roi)]

    # TODO: Update this to be a lot more efficient... not O(n^2)
    table = {}
    for i, u in enumerate(costs):
        cheaper = set(costs[:i])
        faster_roi = set(rois[:rois.index(u)])

        table[u] = cheaper & faster_roi

    return table

def efficiency(upgrades, rate=1):
    time = 0
    for u in upgrades:
        time += u.cost / rate
        rate += u.rate

    return time

def brute_force(table, lookup, before=[]):
    best_order = []
    best_time = float("inf")

    if len(table.keys()) == 1:
        order = before + [lookup[list(table)[0]]]
        return order, efficiency(order)

    for u1, d1 in table.items():
        if d1 != set():
            continue

        sub_table = copy.deepcopy(table)

        del sub_table[u1]
        
        for u2, d2 in sub_table.items():
            d2.discard(u1)

        order, time = brute_force(sub_table, lookup, before+[lookup[u1]])
        if time < best_time:
            best_time = time
            best_order = order

    return best_order, best_time

if __name__ == "__main__":
    upgrades = examples.gen_random(12)
    lookup = {u.name: u for u in upgrades}
    brute_force(gen_dominance(upgrades), lookup)

