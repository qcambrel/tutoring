import csv
from itertools import combinations


# Read recipes.csv into a list of lists
data = []
with open('recipes.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		data.append(row)


# Slice column names out of data
column_names = data[0][1:]
data = data[1:]


# Transpose data then define list of recipe names
columns = list(zip(*data))
recipes = columns[0]
columns = columns[1:]


# Build the dictionary cookbook with each individual recipe having its own 
# subdictionary with the other column names for keys. This allows for an 
# easy lookup of all data relating to each recipe.
cookbook = {}
for k in range(len(recipes)):
	current_recipe = recipes[k]
	cookbook[current_recipe] = {}
	for i in range(len(column_names)):
		recipe_info = column_names[i]
		cookbook[current_recipe][recipe_info] = columns[i][k]


# Define the helper function plan_party.
def plan_party():
	'''Takes user input if no arguments are passed to get_total_servings.'''
	party_size = input("How many dishes are you preparing for the party? ")
	guest_platter = []
	while len(guest_platter) < int(party_size):
		party_recipe = input("What recipe would you like to include for the party? ")
		guest_platter.append(party_recipe)
		print("You have added {} item to the guest platter.".format(len(guest_platter)))
	return guest_platter


# Define the function get_total_servings to meet the first requirement. (description.md)
def get_total_servings(*args):
	'''Takes in any number of recipes then computes the total number of servings given the recipes passed.'''
	if args:
		guest_platter = args
	else:
		guest_platter = plan_party()
	servings = [int(cookbook[dish]['Servings']) for dish in guest_platter]
	return "{} servings".format(sum(servings))


# Define helper function get_recipe_combinations
def filter_combinations(recipe_combinations, serving_count):
	'''Filters the recipe combinations object based on serving count.'''
	filtered_recipe_combinations = []
	for combo in recipe_combinations:
		servings = list(zip(*combo))[1]
		if sum(servings) >= serving_count:
			recipes = []
			for sample in combo:
				recipe = list(cookbook.keys())[sample[0]]
				recipes.append(recipe)
			filtered_recipe_combinations.append(recipes)
	return filtered_recipe_combinations


# Define the function get_recipe_combinations to meet the second requirement. (see description.md)
def get_recipe_combinations(**kwargs):
	'''Given a serving and recipe count, finds all possible recipe combinations.'''
	if kwargs:
		serving_count = kwargs['serving_count']
		recipe_count = kwargs['recipe_count']
	else:
		serving_count = int(input("How many servings are you planning for? "))
		recipe_count = int(input("How many recipes do you want to include? "))
	
	# Using enumerate cookbook.keys() enables the tracking of the index of a 
	# recipe key so that that recipe key can be searched via its index when 
	# the associated serving size is evaluated in filter_combinations.
	servings = [(i, int(cookbook[recipe]['Servings'])) for i, recipe in enumerate(cookbook.keys())] 
	recipe_combinations = list(combinations(servings, recipe_count))
	filtered_recipe_combinations = filter_combinations(recipe_combinations, serving_count)
	if filtered_recipe_combinations:
		return filtered_recipe_combinations
	else:
		return 'No combinations match the requirements.'


# Some simple tests
assert get_total_servings('Bulgogi', 'Miso Soup', 'Paratha') == '18 servings'
assert ['Bulgogi', 'Gourmet Mushroom Risotto', 'Paratha'] in get_recipe_combinations(serving_count=20, recipe_count=3)
assert get_recipe_combinations(serving_count=25, recipe_count=3) == 'No combinations match the requirements.'