import requests

appID = None
appKey = None

class RecipeSearch():

    def __init__(self, parameters = {}):
        self.parameters = parameters
        self.parameters["app_id"] = appID
        self.parameters["app_key"] = appKey
        self._request = None

    def getResults(self):
        self._request = requests.get("https://api.edamam.com/search", params=self.parameters)
        hits = self._request.json()["hits"]
        result = []
        for hit in hits:
            result.append(Recipe(hit["recipe"]))
        return result

class Recipe():

    def __init__(self, source = None):
        if source != None:
            self.uri = source["uri"]
            self.label = source["label"]
            self.image = source["image"]
            self.source = source["source"]
            self.url = source["url"]
            self.makes = source["yield"]
            self.calories = source["calories"]
            self.totalWeight = source["totalWeight"]
            self.ingredients = [Ingredient(x) for x in source["ingredients"]]
            self.nutrients = [Nutrient(source["totalNutrients"][x]) for x in source["totalNutrients"]]
            self.totalDaily = source["totalDaily"]
            self.dietLabels = source["dietLabels"]
            self.healthLabels = source["healthLabels"]
        else:
            self.uri = None
            self.label = None
            self.image = None
            self.source = None
            self.url = None
            self.makes = None
            self.calories = None
            self.totalWeight = None
            self.ingredients = None
            self.totalNutrients = None
            self.totalDaily = None
            self.dietLabels = None
            self.healthLabels = None

class Ingredient():

    def __init__(self, source = None):
        if source != None:
            self.text = source["text"]
            self.weight = source["weight"]
        else:
            self.text = None
            self.weight = None

class Nutrient():

    def __init__(self, source = None):
        if source != None:
            self.label = source["label"]
            self.quantity = source["quantity"]
            self.unit = source["unit"]
        else:
            self.label = None
            self.quantity = None
            self.unit = None


