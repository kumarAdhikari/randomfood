from flask import Flask, redirect, url_for, render_template, request
import requests

app = Flask(__name__)


def foodgenerator():
    apikey_url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(apikey_url)
    heart = "\u2764\ufe0f"
    response = response.json()
    meal_name = response['meals'][0]["strMeal"]
    nationality = response['meals'][0]["strArea"]
    receipe = str(response['meals'][0]["strInstructions"])
    thumbnail = str(response['meals'][0]["strMealThumb"])
    ingredient_index = []
    measure_index = []
    list_receipe = receipe.split("\r\n")
    length_receipe = len(list_receipe)
    for x in response['meals'][0]:
        if "strIngredient" in x:
            ingredient_index.append(x)

    for x in response['meals'][0]:
        if "strMeasure" in x:
            measure_index.append(x)

    ingredient = []
    measure = []

    for x in range(0, len(ingredient_index)):
        tem = ingredient_index[x]
        tem = str(tem)
        temp1 = response['meals'][0][tem]
        if temp1 == " " or temp1 == "" or temp1 is None:
            pass
        else:
            ingredient.append(temp1)

    for x in range(0, len(measure_index)):
        tem = measure_index[x]
        tem = str(tem)
        temp1 = response['meals'][0][tem]
        if temp1 == " " or temp1 == "" or temp1 is None:
            pass
        else:
            measure.append(temp1)
    number_in = len(ingredient) - 1
    return list_receipe, length_receipe, meal_name, nationality, receipe, ingredient, measure, thumbnail, number_in


def checkNonVeg(ingreient):
    meat = ["beef", "chicken", "pork", "fish", "shrimp", "red snapper", "lamb", "goat", "clams", "mussels", "egg",
            "eggs", "prawns", "ham", "oxtail"]
    for x in range(0, len(ingreient)-1):
        for xx in range(0, len(meat)-1):
            if meat[xx] in ingreient[x].lower():
                return True
    return False


def customized(ingreient, customer_preferance):
    for ingre in ingreient:
        for customer_prefix in customer_preferance:
            if customer_prefix.lower() in ingre.lower():
                return True
    return False

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/randomfood', methods=['POST', 'GET'])
def initial_response():
    list_receipe, length_receipe, meal_name, nationality, receipe, ingredient, measure, thumbnail, number_in = foodgenerator()
    return render_template("initialrandomfood.html", list_receipe=list_receipe, length_receipe=length_receipe, meal_name=meal_name,
                           nationality=nationality, receipe=receipe, ingredient=ingredient, measure=measure,
                           thumbnail=thumbnail, number_in=number_in)


@app.route('/randomvegterianfood', methods=['POST', 'GET'])
def veg_response():
    veg = False
    while not veg:
        list_receipe, length_receipe, meal_name, nationality, receipe, ingredient, measure, thumbnail, number_in = foodgenerator()
        if not checkNonVeg(ingredient):
            veg = True
    return render_template("nonveg.html", list_receipe=list_receipe, length_receipe=length_receipe, meal_name=meal_name,
                           nationality=nationality, receipe=receipe, ingredient=ingredient, measure=measure,
                           thumbnail=thumbnail, number_in=number_in)

@app.route('/customfood', methods=['POST', 'GET'])
def custom_response():
    if request.method == 'POST':
        custom = False
        itemsa = request.form["exclude_item"]
        if itemsa is not None:
            items = itemsa.split(",")
        else:
            items = ["nothing"]
        while not custom:
            list_receipe, length_receipe, meal_name, nationality, receipe, ingredient, measure, thumbnail, number_in = foodgenerator()
            if not customized(ingredient, items):
                custom = True
        return render_template("custom.html", list_receipe=list_receipe, length_receipe=length_receipe,
                               meal_name=meal_name,
                               nationality=nationality, receipe=receipe, ingredient=ingredient, measure=measure,
                               thumbnail=thumbnail, number_in=number_in, itemsa=itemsa)


if __name__ == '__main__':
    app.run()

'''        meat = ["beef gravy", "chicken gravy", "beef", "chicken", "pork", "egg", "goat meat", "lamb meat",
                "goat leg meat", "lamb leg meat", "eggs", "fish", "prawn", "prawn", "egg white", "shrimp", "anchovy",
                "anchovy fillet", "prawns", "chicken stock", "chicken breast", "chicken thighs", "chicken thigh",
                "chicken legs", "clams", "mussels", "ground beef", "lamb", "goat"]'''
