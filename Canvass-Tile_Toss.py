#CANVAS TILES TOSS
import matplotlib.pyplot as plt

# Groups
groups = [
    "G9-5B","G9-1B","G9-20","G10-5B","G10-10B",
    "G11-1A","G11-10B","G12-5B","G12-5A","G13-1A",
    "G13-10A","G14-1A","G14-20","G15-1B","G15-5B"
]

# Heads and Tails per group
heads = [48, 51, 38, 56, 45, 43, 54, 52, 54, 49, 46, 42, 56, 49, 51]
tails = [52, 49, 62, 44, 55, 57, 46, 48, 46, 51, 52, 58, 44, 51, 49]

# Cumulative counts (as given)
cumulative_heads = [48, 99, 137, 193, 238, 261, 335, 387, 441, 490, 538, 580, 636, 655, 736]
cumulative_tails = [52, 101, 163, 207, 262, 319, 365, 413, 459, 510, 562, 620, 664, 715, 764]

# --- Bar chart for Heads vs Tails ---
plt.figure(figsize=(12,5))
x = range(len(groups))
plt.bar(x, heads, width=0.4, label='Heads', color='skyblue')
plt.bar([i + 0.4 for i in x], tails, width=0.4, label='Tails', color='salmon')
plt.xticks([i + 0.2 for i in x], groups, rotation=45)
plt.xlabel("Group")
plt.ylabel("Number of Tosses")
plt.title("Canvass Tile Toss Heads vs Tails per Group (Groups 9-15)")
plt.legend()
plt.tight_layout()
plt.show()


