import Edamam

Edamam.appID = "818a6ce2"
Edamam.appKey = "601ce45d5c4b47772011c677abe0211f"

test = Edamam.RecipeSearch({'q':'scrambled egg and salmon', 'to':10}).getResults()

print("Results:")
for result in test:
    print(result.label + "\t" + result.url)
