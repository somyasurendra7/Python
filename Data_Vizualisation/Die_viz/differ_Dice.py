from Die_viz.Die import Die
import pygal

# create a die
die1 = Die(20)
die2 = Die(50)

# storing rolls
results =[]
for rolls in range(50000):
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

hist.title = "Rolling multi-sided die 50000 times"
hist.x_labels = list(range(2,70))
hist.x_title = 'Result'
hist._y_title = 'Frequency'
hist.add('D50 + D20', frequencies)
hist.render_to_file("multi_sided_die.svg")
