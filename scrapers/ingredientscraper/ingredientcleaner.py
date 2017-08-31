import sqlite3
ingredientin = open('cleanedingredients.txt', 'r')
totalingredientlist = []
outingredientlist = []
database = "/home/adam/database/ingredientrecipedb.sqlite3"
database2 = "/home/adam/database/recipedb.sqlite3"
conn = sqlite3.connect(database)
conn2 = sqlite3.connect(database2)
conn.text_factory = str
conn2.text_factory = str
c = conn.cursor()
c2 = conn2.cursor()
# for line in ingredientin:
#     # line = line.strip()
#     # if " Or " in line:
#     #     linelist = line.split(" Or ")
#     #     print(linelist)
#     #     totalingredientlist.append(linelist[0])
#     #     totalingredientlist.append(linelist[1])
#     # else:
#     #     totalingredientlist.append(line)
#
#     totalingredientlist.append(line)
# count = 0
# while count < len(totalingredientlist):
#     elementindex = count
#     if totalingredientlist[count].lower().startswith("side") or \
#             totalingredientlist[count].lower().startswith("splash") or \
#             totalingredientlist[count].lower().startswith("sprig") or \
#             totalingredientlist[count].lower().startswith("stale") or \
#             totalingredientlist[count].lower().startswith("stalk") or \
#             totalingredientlist[count].lower().startswith("sifted") or \
#             totalingredientlist[count].lower().startswith("sleeve") or \
#             totalingredientlist[count].lower().startswith("slice") or \
#             totalingredientlist[count].lower().startswith("table spoon") \
#             or totalingredientlist[count].lower().startswith("tablepoon") \
#             or totalingredientlist[count].lower().startswith("tablespoon") \
#             or totalingredientlist[count].lower().startswith("tablespooon") \
#             or totalingredientlist[count].lower().startswith("tsp") \
#             or totalingredientlist[count].lower().startswith("tbsp") \
#             or totalingredientlist[count].lower().startswith("teaspoon") \
#             or totalingredientlist[count].lower().startswith("recipe") \
#             or totalingredientlist[count].lower().startswith("lb") \
#             or totalingredientlist[count].lower().startswith("special equipment") \
#             or totalingredientlist[count].lower().startswith("small handful") \
#             or totalingredientlist[count].lower().startswith("oz") \
#             or totalingredientlist[count].lower().startswith("other") \
#             or totalingredientlist[count].lower().startswith("stick") \
#             or totalingredientlist[count].lower().startswith("thick") \
#             or totalingredientlist[count].lower().startswith("strip") \
#             or totalingredientlist[count].lower().startswith("strained") \
#             or totalingredientlist[count].lower().startswith("pint") \
#             or totalingredientlist[count].lower().startswith("cup") \
#             or ":" in totalingredientlist[count].lower() \
#             or " andor " in totalingredientlist[count].lower() \
#             or ", recipe follows" in totalingredientlist[count].lower() \
#             or "\xc2" in totalingredientlist[count].lower() \
#             or "\xe2" in totalingredientlist[count].lower() \
#             or " and " in totalingredientlist[count].lower() \
#             or "," in totalingredientlist[count].lower() \
#             or " for " in totalingredientlist[count].lower() \
#             or ";" in totalingredientlist[count].lower() \
#             or totalingredientlist[count - 1] == totalingredientlist[count] \
#             or (totalingredientlist[count - 1] + "s") == totalingredientlist[count] \
#             or len(totalingredientlist[count].strip()) == 1:
#         del totalingredientlist[elementindex]
#         count -= 1
#         print("deleted item")
#     if "  " in totalingredientlist[count]:
#         print repr(totalingredientlist[count])
#         totalingredientlist[count] = ' '.join(totalingredientlist[count].split())
#         print(totalingredientlist[count])
#         print("string modified")
#         count += 1
#     else:
#         count += 1
# ingredientin.close()
# totalingredientlist.sort()
# ingredientout = open('cleanedingredients.txt', 'w')
for element in c.execute('SELECT * FROM recipe'):
    print(element)
    c2.execute('''INSERT INTO recipe (name, author, ingredients, recipeyield, difficulty, totaltime, activetime, directions) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8]))
conn2.commit()
c.close()



