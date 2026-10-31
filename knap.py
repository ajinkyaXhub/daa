weight = [10, 20, 30]
profit = [60, 100, 120]

capacity = 50
total = 0

ratio = []

for i in range(len(weight)):
    ratio.append((profit[i] / weight[i], weight[i], profit[i]))

ratio.sort(reverse=True)

for r, w, p in ratio:
    if capacity >= w:
        total += p
        capacity -= w
    else:
        total += r * capacity
        break

print("Maximum Profit:", total)
