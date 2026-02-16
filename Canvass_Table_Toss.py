# CANVASS TABLE TOSS
import matplotlib.pyplot as plt

# Data
groups = [
    "G1-1B","G1-2pesos","G2-1B","G2-5A","G3-1B","G3-10A",
    "G4-5A","G4-5B","G5-1A","G5-1B","G6-5B","G6-20",
    "G7-5A","G7-10A","G8-1A","G8-10B"
]

heads = [50, 46, 51, 54, 53, 52, 55, 53, 59, 43, 46, 48, 49, 50, 52, 56]
tails = [50, 54, 49, 46, 47, 48, 45, 47, 41, 57, 54, 52, 51, 50, 48, 44]
cumulative_heads = [50, 96, 147, 201, 254, 306, 361, 414, 473, 516, 552, 610, 659, 709, 761, 817]
cumulative_tails = [50, 104, 153, 199, 246, 294, 339, 386, 427, 484, 538, 590, 641, 691, 739, 783]

# Bar chart of Heads vs Tails per group
plt.figure(figsize=(12,5))
x = range(len(groups))
plt.bar(x, heads, width=0.4, label='Heads', color='skyblue')
plt.bar([i + 0.4 for i in x], tails, width=0.4, label='Tails', color='salmon')
plt.xticks([i + 0.2 for i in x], groups, rotation=45)
plt.xlabel("Group")
plt.ylabel("Number of Tosses")
plt.title("Canvass Table Toss Heads vs Tails per Group (Groups 1-8) ")
plt.legend()
plt.tight_layout()
plt.show()


