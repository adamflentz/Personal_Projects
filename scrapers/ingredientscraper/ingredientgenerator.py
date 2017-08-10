import sqlite3, json, re

database = "/home/adam/database/recipedb.sqlite3"
conn = sqlite3.connect(database)
c = conn.cursor()
errorlist = []
totalingredientlist = []
error = open('errorlist.txt', 'w')
ingredient = open('ingredientlist.txt', 'w')
count = 0
for element in c.execute('''select ingredients from recipe'''):
    ingredientlist = list(element)

    for element in ingredientlist:
        data = json.loads(element)
        for x in data:
            x = ''.join([i for i in x if not i.isdigit()])
            x = x.replace('ounces', '').replace('loosely packed', '').replace('Percent', '').replace('-To--', '').replace('To   ', '').replace(',recipe follows', '').replace('Cans', '').replace('teaspoons', '').replace('tablespoons', '').replace('cups', '').replace('cup', '').replace('tablespoon', '').replace('ounce', '').replace('teaspoon', '').replace('bottle', '').replace('/', '').replace('big', '').split(',')
            if len(x) > 1:
                del x[-1]
            x = ','.join(x).title()
            x = re.sub(r'\([^)]*\)', '', x).strip()
            if x.startswith("A ") or x.startswith("About "):
                errorlist.append(x)
            elif "Extra-Virgin" in x or "All-Purpose" in x:
                if x not in totalingredientlist:
                    totalingredientlist.append(x)
            elif "." in x or "-" in x or "%" in x or "*" in x or "(" in x or ")" in x or "+" in x:
                errorlist.append(x)
            else:
                if len(totalingredientlist) == 0:
                    totalingredientlist.append(x)
                elif " Or " in x:
                    minilist = x.split(" Or ")
                    for element in minilist:
                        if element not in totalingredientlist:
                            totalingredientlist.append(element)
                elif x not in totalingredientlist:
                    totalingredientlist.append(x)
                x = x.encode(encoding='UTF-8').replace('  ', ' ').replace('  ', ' ')
            count += 1
            print(count)

totalingredientlist.sort(reverse=True)
count = 0
for element in totalingredientlist:
    element = element.encode(encoding="UTF-8")
    ingredient.write(element + "\n")
ingredient.close()
for element in errorlist:
    element = element.encode(encoding='UTF-8')
    error.write(element + "\n")

