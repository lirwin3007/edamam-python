import Edamam

Edamam.appID = "INSERT APP ID"
Edamam.appKey = "INSERT APP KEY"

test = Edamam.RecipeSearch({'q':'scrambled egg and salmon', 'to':10}).getResults()

print("Results:")
for result in test:
    print(result.label + "\t" + result.url)
