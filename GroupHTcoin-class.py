# 1
# Import the matplotlib library and give it a shorter name "plt"
# This library is used to create graphs and charts
import matplotlib.pyplot as plt


# Create a list of numbers from 1 to 100
# This represents the number of coin flip attempts
attempts = list(range(1, 101))


# -------- 10B Coin --------

# This list stores the running total of HEADS
# after each flip for the 10B coin
head_10B = [
1,1,1,1,2,3,3,4,4,4,4,5,5,6,6,7,7,8,8,9,
10,11,11,11,12,13,13,14,15,15,16,17,17,17,18,19,19,19,20,20,
21,22,23,24,24,24,24,24,25,26,27,28,28,28,29,30,30,31,31,31,
32,32,33,33,34,34,35,35,36,36,36,37,38,39,40,40,41,42,43,43,
44,45,46,46,47,47,48,48,49,50,51,51,52,53,54,54,54,54,54,54
]

# This list stores the running total of TAILS
# after each flip for the 10B coin
tail_10B = [
0,1,2,3,3,3,4,4,5,6,7,7,8,8,9,9,10,10,11,11,
11,11,12,13,13,13,14,14,14,15,15,15,16,17,17,17,18,19,19,20,
20,20,20,20,21,22,23,24,24,24,24,24,25,26,26,26,27,27,28,29,
29,30,30,31,31,32,32,33,33,34,35,35,35,35,35,36,36,36,36,37,
37,37,37,38,38,39,39,40,40,40,40,41,41,41,41,42,43,44,45,46
]


# -------- 1A Coin --------

# Running total of HEADS for 1A coin
head_1A = [
1,1,2,3,3,3,3,4,5,6,7,8,8,8,8,9,10,10,11,11,
12,13,13,14,14,15,15,16,17,17,18,18,18,19,19,19,19,20,20,21,
22,23,23,24,24,25,25,26,26,26,26,27,28,28,28,29,29,29,29,29,
29,30,31,31,31,31,32,33,34,34,35,35,36,36,37,38,38,38,38,38,
38,38,38,39,39,39,39,39,40,40,40,40,41,41,42,42,42,42,43,43
]

# Running total of TAILS for 1A coin
tail_1A = [
0,1,1,1,2,3,4,4,4,4,4,4,5,6,7,7,7,8,8,9,
9,9,10,10,11,11,12,12,12,13,13,14,15,15,16,17,18,18,19,19,
19,19,20,20,21,21,22,22,23,24,25,25,25,26,27,27,28,29,30,31,
32,32,32,33,34,35,35,35,35,36,36,37,37,38,38,38,39,40,41,42,
43,44,45,45,46,47,48,49,49,50,51,52,52,53,53,54,55,56,56,57
]


# Create a new figure (the full window that will contain the graphs)
# figsize controls the size of the window (width, height)
plt.figure(figsize=(8, 10))


# -----------------------------
# Top Graph – 1A Coin
# -----------------------------

# Create a subplot layout:
# (2 rows, 1 column, and this is graph number 1)
plt.subplot(2, 1, 1)

# Plot attempts on x-axis and heads on y-axis
plt.plot(attempts, head_1A)

# Plot attempts on x-axis and tails on y-axis
plt.plot(attempts, tail_1A)

# Add a title to this graph
plt.title("1A Coin Running Total")

# Label for x-axis
plt.xlabel("Number of Attempts")

# Label for y-axis
plt.ylabel("Running Total")

# Add a legend to explain which line is Head and which is Tail
plt.legend(["Head", "Tail"])


# -----------------------------
# Bottom Graph – 10B Coin
# -----------------------------

# Create second subplot:
# (2 rows, 1 column, and this is graph number 2)
plt.subplot(2, 1, 2)

# Plot running total of heads for 10B
plt.plot(attempts, head_10B)

# Plot running total of tails for 10B
plt.plot(attempts, tail_10B)

# Add title
plt.title("10B Coin Running Total")

# Label x-axis
plt.xlabel("Number of Attempts")

# Label y-axis
plt.ylabel("Running Total")

# Add legend
plt.legend(["Head", "Tail"])


# Automatically adjust spacing so graphs don't overlap
plt.tight_layout()

# Display the graphs on the screen
plt.show()


