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


@app.route('/randomvegterianfood', methods=['POST', 'GET'])
def veg_response():
    nonvege = False
    while nonvege == False:
        apikey_url = "https://www.themealdb.com/api/json/v1/1/random.php"
        try:
            response = requests.get(apikey_url)
        except:
            response = requests.get(apikey_url)
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
        meat = ["beef", "chicken", "pork", "egg","eggs", "fish", "prawn", "prawn", "egg white", "shrimp", "anchovy", "anchovy fillet", "prawns", "chicken stock", "chicken breast", "chicken thighs", "chicken thigh", "chicken legs", "clams", "mussels", "ground beef", "lamb", "goat"]
        nonveg = False
        for x in range(0, len(ingredient_index)):
            tem = ingredient_index[x]
            tem = str(tem)
            temp1 = response['meals'][0][tem]
            if temp1 == " " or temp1 == "":
                pass
            else:
                if temp1.lower() in meat:
                    nonveg = True
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
        if meal_name in meat:
            nonvege = True
        if nonveg == False:
            nonvege = True

    return render_template("nonveg.html",list_receipe =list_receipe, length_receipe = length_receipe, meal_name=meal_name, nationality=nationality, receipe=receipe, ingredient=ingredient,measure=measure, thumbnail=thumbnail, number_in=number_in)




if __name__ == '__main__':
    app.run()
