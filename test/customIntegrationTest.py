def customized(ingreient, customer_preferance):
    for ingre in ingreient:
        for customer_prefix in customer_preferance:
            if customer_prefix.lower() in ingre.lower():
                return True
    return False

'''def sample(food, customer):
    print(food, customer)
    prefe_len = len(customer)
    for x in food:
        for xx in customer:
            if xx in x:
                print("FOOD HERE")'''



ingreident1 = ["Beef", "chicken", "tomatoes", "green beans"] #True
ingreident2 = ["tomatoes", "apple", "orange", "green beans"] #False
ingreident3 = ["Prawns", "fish Pork", "goat meat"] #False
ingreident4 = ["tomatoes sauce", "beans beans", "something"] #False
ingreident5 = ["Eggs scrambled", "gravy beef"] #True
prferences = ["beef", "eggs"]

check = [ingreident1, ingreident2, ingreident3, ingreident4, ingreident5]
result = []
expecation = [True, False, False, False, True]

for x in range(0, 5):
    result.append(customized(check[x], prferences))
    print(customized(check[x], prferences))


if result == expecation:
    print("TEST PASSED")
else:
    print("TEST FAILED")