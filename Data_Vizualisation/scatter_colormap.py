# using a colormap
import matplotlib.pyplot as plt


x_values = list(range(1,1000001))
y_values = [x**2 for x in x_values]
# colormap
plt.scatter(x_values, y_values, c=y_values , cmap=plt.cm.Blues, edgecolors='none', s= 40)
# title and labels
plt.title("Squares", fontsize=24)
plt.xlabel("Values", fontsize=20)
plt.ylabel("Squares of values", fontsize=20)

# saving the plots to a file
plt.savefig('sqaures_plot_01.png', bbox_inches="tight")

plt.show()



