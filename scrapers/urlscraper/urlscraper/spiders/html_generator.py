urllist = []
urllist.append("http://www.foodnetwork.com/recipes/a-z/123/p/1")
urllist.append("http://www.foodnetwork.com/recipes/a-z/123/p/2")
outdoc = open("urllist.txt", "w")
for item in range(ord("a"), ord("w") + 1, 1):
    for number in range (1, 100):
        itemurl = "http://www.foodnetwork.com/recipes/a-z/" + chr(item) + "/p/" + str(number)
        urllist.append(itemurl)
urllist.append("http://www.foodnetwork.com/recipes/a-z/xyz/p/1")
urllist.append("http://www.foodnetwork.com/recipes/a-z/xyz/p/2")
urllist.append("http://www.foodnetwork.com/recipes/a-z/xyz/p/3")
urllist.append("http://www.foodnetwork.com/recipes/a-z/xyz/p/4")
for item in urllist:
    outdoc.write(item)
    outdoc.write("\n")
print(urllist)
