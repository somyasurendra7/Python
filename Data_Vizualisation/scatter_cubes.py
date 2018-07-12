import matplotlib.pyplot as plt

x_value = list(range(1,5))
y_vlaue = [x**3 for x in x_value]

plt.scatter(x_value, y_vlaue, c=y_vlaue, cmap=plt.cm.Reds, edgecolors='none', s=40)
plt.title("Cubes")
plt.xlabel("Values")
plt.ylabel("Cubes of values")
plt.axis([0,5, 0,80])
plt.savefig("cubes_plot_01.png", bbox_inch='tight')
plt.show()