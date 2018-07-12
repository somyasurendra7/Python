import csv
from matplotlib import pyplot as plt


filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

# getting high temperatures from the file
	highs = []
	for row in reader:
		high = int(row[1])
		highs.append(high)

	print(row)

# plotting the graph
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs, c='red')

plt.title("Temperature for Satika", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig("temp_01.png", bbox_inch='tight')
plt.show()
