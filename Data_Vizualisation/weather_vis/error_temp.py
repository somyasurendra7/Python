import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
# plotting highs and lows
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])

		except ValueError:
			print("The date and time data is missing for: " , current_date)

		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

# plotting the graph
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c='green', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1)
plt.title("Yearly High and Low Temperature for Death valley", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig("temp_05.png", bbox_inch='tight')
plt.show()



