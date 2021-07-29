# Question 2
que=["orange","Orange","ORANGE","cherry","strawberry","STRAWBERRY"]
# Question 3
for value in que:
    if value == "orange":
        print(value)
# Question 4
for item in que:
    if item.title()== "Orange":
        print(item)
# Question 5
for word in que:
    if word == "ORANGE" or word == "STRAWBERRY":
        print(word)


