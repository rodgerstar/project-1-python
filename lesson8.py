#Dictionary

student = {"name":"jane, sarah", "id": 1234,  "age" : 21, "gender": "female"}


print(student["name"])   #key

print(student)

student["weight"] = 61

print(student)

#  set
# only once existence per item, unordered

people = {"jane", "bill", "kevo","jane"}
print(people)

# add ,pop ,discard, count
people.add("merit")
print(people)
people.discard("bill")
print(people)
print(len(people))