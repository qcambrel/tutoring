This student's project had two requirements:

- Write a function that informs the total servings of the recipes selected by the user. The user will need to specify any number of recipes as they desire and the function will return the summative servings of these recipes assuming the servings of different recipes are additive. Say, the user may input "Bulgogi", "Miso Soup", and "Paratha". The function will inform the user with the total servings to be 18. If the user inputs nothing, print out a message to indicate 0 servings.
- Write a function that informs a list of combinations of recipes that meet the user's requirement on the servings. The user will need to specify the total servings and the number of recipes. The function should list all of the possible combinations of recipes and their summative servings equal to or more than the user's target servings, assuming the servings are additive. For example, the user may indicate the total servings to be 20 with 3 recipes. The function will return a recipe combo to be ["Bulgogi", "Gourmet Mushroom Risotto", "Paratha"]. If none of the recipe combinations meet the requirement, print out a warning message.

We started with a 'recipes.csv' file from which to extract the necessary data.

The solution uses the csv and itertools modules respectively. Both of which come preinstalled in the Python standard library. No additional packages are required.

python==3.8.5