# scatter plots
import matplotlib.pyplot as plt


# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1,1000001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, edgecolors='none', s= 40)
# title and labels
plt.title("Squares", fontsize=24)
plt.xlabel("Values", fontsize=20)
plt.ylabel("Squares of values", fontsize=20)
plt.axis([0, 1100, 0, 110000])
# saving plot
plt.savefig("squares_plot02.png")

plt.show()

