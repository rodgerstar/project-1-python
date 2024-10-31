# loops

while True:
    print("hello, loops")
    break

scores = [90, 78, 67, 76, 34, 65, 56, 99, 45, 59, 66, 44, 71, 51, 81, 74, 61, 59, 95, 72]

# for each loop
for score in scores:
    if score >= 50 and score <= 70 and score % 2== 0:
        print(score)