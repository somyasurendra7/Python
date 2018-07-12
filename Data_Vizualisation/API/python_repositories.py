import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)

# store the response in a variable
response_dict = r.json()
print('Total repositories: ', response_dict['total_count'])
# items in repo
names, stars = [], []
repo_dicts = response_dict['items']
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

# creating visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most Starred Python projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('Python_repositories.svg')