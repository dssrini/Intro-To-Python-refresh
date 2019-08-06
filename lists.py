shopList = ["Apples", "Oranges", "Bananas", "Cheese"]
print shopList
# print shopList[0]
# print shopList[3]
# print shopList[0:2]
# print shopList[:3]

shopList.append("Blueberries")
print shopList

shopList[0] = "Cherries"
print shopList

del shopList[1]
print shopList

print len(shopList)

shopList2 = ["Bread", "Jam", "Peanut Butter"]

print shopList + shopList2
print shopList * 2

listNum = [1,4,7,23,6]
print max(listNum)
print min(listNum)