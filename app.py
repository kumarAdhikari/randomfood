from flask import Flask,redirect,url_for,render_template,request
import requests

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/randomfood', methods=['POST', 'GET'])
def initial_response():
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
    list_receipe = receipe.split("\r\n\r\n")
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
        if temp1 == " " or temp1 == "":
            pass
        else:
            ingredient.append(temp1)

    for x in range(0, len(measure_index)):
        tem = measure_index[x]
        tem = str(tem)
        temp1 = response['meals'][0][tem]
        if temp1 == " " or temp1 == "":
            pass
        else:
            measure.append(temp1)
    number_in = len(ingredient)-1
    return render_template("initialrandomfood.html",list_receipe =list_receipe, length_receipe = length_receipe, meal_name=meal_name, nationality=nationality, receipe=receipe, ingredient=ingredient,measure=measure, thumbnail=thumbnail, number_in=number_in)


if __name__ == '__main__':
    app.run()
