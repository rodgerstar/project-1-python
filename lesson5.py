entered_value = input("Enter the score: ")
if not entered_value.isnumeric():
    print("please enter a valid number")
    exit(0)

print (entered_value)


score = int(entered_value)


if score >= 78:
    print("A")
elif 71 <= score <= 77:
    print("A-")
elif score >= 64 and score <= 70:
    print("B+")
elif score >= 57 and score <= 63:
    print("B")
elif score >= 50 and score <= 56:
    print("B-")
elif score >= 43 and score <= 49:
    print("C+")
else:
    print("C")
