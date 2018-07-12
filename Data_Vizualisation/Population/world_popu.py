import json
from Population.country_code import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

	# population data
	cc_population = {}
	for data in pop_data:
		if data['Year'] == '2010':
			country_name = data['Country Name']
			population  = int(float(data['Value']))
			code = get_country_code(country_name)
			if code:
				cc_population[code] = population

	# grouping countries on the basis of population
	cc_pop_01, cc_pop_02, cc_pop_03 = {}, {}, {}
	for cc, pop in cc_population.items():
		if pop < 10000000:
			cc_pop_01[cc] = pop
		elif pop < 1000000000:
			cc_pop_02[cc] = pop
		else:
			cc_pop_03 = pop

	# print(len(cc_pop_01), len(cc_pop_02), len(cc_pop_03))


wm_style = RotateStyle('#336700')
wm = World(style = wm_style)
wm.title = "World Population in 2010, by Country"
wm.add('0-10M', cc_pop_01)
wm.add('10-1Bn', cc_pop_02)
wm.add('>1Bn', cc_pop_03)
wm.render_to_file("world_population_2010.svg")
