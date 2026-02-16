import matplotlib.pyplot as plt

head_total = []
tail_total = []

with open("coin_data.txt", "r") as file:
    next(file)  # skip header
    for line in file:
        h, t = map(int, line.split())
        head_total.append(h)
        tail_total.append(t)

attempts = range(1, len(head_total) + 1)

plt.figure(figsize=(10,6))
plt.plot(attempts, head_total, label="Total of H")
plt.plot(attempts, tail_total, label="Total of T")

plt.title("New Combined Running Total")
plt.xlabel("Number of Attempts")
plt.ylabel("Running Total")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()