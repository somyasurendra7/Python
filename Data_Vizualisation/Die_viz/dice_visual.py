from Die_viz.Die import Die
import pygal


# create a die
die1 = Die()
die2 = Die()

# storing rolls
results =[]
for rolls in range(10000):
	result = die1.roll() + die2.roll()
	results.append(result)

# analyzing the frequency of rolls
frequencies =[]
max_result = die1.num_sides+die2.num_sides
for value in range(2, max_result+1):
	freq = results.count(value)
	frequencies.append(freq)

# Visual
hist = pygal.Bar()

hist.title = "Rolling 2 6 sided die 10000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist._y_title = 'Frequency'
hist.add('D6 + D6', frequencies)
hist.render_to_file("6-die_01.svg")


