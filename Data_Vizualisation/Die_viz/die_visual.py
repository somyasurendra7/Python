from Die_viz.Die import Die
import pygal


# create a die
die = Die()

# storing rolls
results =[]
for rolls in range(10000):
	result = die.roll()
	results.append(result)

# analyzing the frequency of rolls
frequencies =[]
for value in range(1, die.num_sides+1):
	freq = results.count(value)
	frequencies.append(freq)

# Visual
hist = pygal.Bar()

hist.title = "Rolling a 6 sided die 10000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist._y_title = 'Frequency'
hist.add('D6', frequencies)
hist.render_to_file("6-die.svg")

