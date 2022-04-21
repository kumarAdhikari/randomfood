
def checkNonVeg(ingreient):
    meat = ["beef", "chicken", "pork", "fish", "shrimp", "red snapper", "lamb", "goat", "clams", "mussels", "egg",
            "eggs", "prawns", "ham"]
    for x in range(0, len(ingreient)-1):
        for xx in range(0, len(meat)-1):
            if meat[xx] in ingreient[x].lower():
                return True
    return False


ingreident1 = ["beef ham", "chicken", "tomatoes", "green beans"] #True
ingreident2 = ["tomatoes", "apple", "orange", "green beans"] #False
ingreident3 = ["Prawns", "fish Pork", "goat meat"] #True
ingreident4 = ["tomatoes sauce", "beans beans", "something"] #False
ingreident5 = ["Eggs scrambled", "gravy beef"] #True
check = [ingreident1, ingreident2, ingreident3, ingreident4, ingreident5]
result = []
expecation = [True, False, True, False, True]
for x in range(0, 5):
    result.append(checkNonVeg(check[x]))

if result == expecation:
    print("TEST PASSED")
else:
    print("TEST FAILED")

