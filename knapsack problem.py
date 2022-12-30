import functools


def knapsack_dyn_ints(w, weights, values):
    weights, values = zip(*[(w, v) for w, v in zip(weights, values) if v > 0]) # filters out items with no value
    print(weights, values)
    print()
    bestVals = [0 for _ in range(w + 1)]  # index is the actual weight in this case
    bestItems = [[[]] for _ in range(w + 1)]

    # at each weight you need to store the max value achieved and the combo of items that got you there

    for weight in range(w + 1):
        bestVal = bestVals[weight - 1]
        bestCombos = bestItems[weight - 1]
        for item in range(len(weights)):
            if weight - weights[item] < 0:
                continue

            if not bestItems[weight-weights[item]]:
                bestItems[weight-weights[item]] = [[]]
            for combo in bestItems[weight-weights[item]]:
                comboVal = bestVals[weight-weights[item]]
                if item not in combo:
                    comboVal += values[item]
                    if comboVal == bestVal:
                        if combo + [item] not in bestCombos:
                            bestCombos.append(combo + [item])
                    if comboVal > bestVal:
                        bestCombos = [combo + [item]]
                        bestVal = comboVal
        bestVals[weight] = bestVal
        bestItems[weight] = bestCombos

    print(bestItems)
    print(bestVals)
    print()

    print(bestItems[bestVals.index(bestVals[-1])])
    print(bestVals[-1])

