from pygal_maps_world.maps import World


wm = World()
wm.title = "Population of North American Countries"
wm.add('North America', {'ca': 34126000, 'us' : 30930000, 'mx': 113425670})

wm.render_to_file("Population map.svg")

