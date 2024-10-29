#list

scores = [90, 66, 75, 32, 54, 49, 95, 88]

# access a value
print(scores[4]) #5th
print(scores[0]) #1st

#add
scores.append(66)
print(scores)

#remove
scores.pop(2)
print(scores)

#accending order
scores.sort()
print(scores)

#decending order
scores.sort(reverse=True)
print(scores)
