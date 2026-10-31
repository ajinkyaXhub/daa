jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

jobs.sort(key=lambda x: x[2], reverse=True)

n = max(job[1] for job in jobs)
slot = [None] * n
profit = 0

for job in jobs:
    for j in range(min(n, job[1]) - 1, -1, -1):
        if slot[j] is None:
            slot[j] = job[0]
            profit += job[2]
            break

print("Scheduled Jobs:", slot)
print("Maximum Profit:", profit)
