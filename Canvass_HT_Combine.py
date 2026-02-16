import matplotlib.pyplot as plt

# Toss types and totals
toss_types = ["Canvass Table Toss", "Canvass Tile Toss"]
totals = [1600, 1500]

# Bar chart
plt.figure(figsize=(8,5))
plt.bar(toss_types, totals, color=['pink', 'blue'])
plt.ylabel("Total Tosses")
plt.title("Comparison of Canvass Table Toss and Tile Toss")
for i, total in enumerate(totals):
    plt.text(i, total + 20, str(total), ha='center', fontweight='bold')
plt.ylim(0, max(totals) + 200)
plt.show()
