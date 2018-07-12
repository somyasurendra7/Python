# plotting the random walk
import matplotlib.pyplot as plt
from Running_walk import RandomWalk

while True:
	rw = RandomWalk(50000)
	rw.fine_walk()

	point_numbers = list(range(rw.num_points))
	# plotting random walk
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolors='none', s=1)
	# first and last points
	plt.scatter(0, 0, c='red', edgecolors='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
	# hiding plot axis
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.savefig("Random_walk_01.png", bbox_inch='tight')
	# plt.figure(figsize=(10,6))
	plt.show()

	keep_running = input("Do you still want to run? (y/n): ")
	if keep_running == 'n':
		break






