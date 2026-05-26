# list = ["apple","grapes","orange","watermelon","kiwi"]
# newlist = []
# for i in list:
#     if "a" in i:
#         newlist.append(i)
# print(newlist)
                        #   list comprehensive..............................................




list = ["apple","grapes","orange","watermelon","kiwi"]
newlist=[i for i in list if "a" not in i]
print(newlist)

