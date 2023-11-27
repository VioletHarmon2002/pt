import random

results = []

times = input("How many times to roll? ")

if times != "":
    times = int(times)

    for _ in range(times):
        roll = random.randint(1, 6)
        results.append(roll)

    total = sum(results)
    print("Results:", results)
    print("Sum of the rolled numbers:", total)
else:
    print("No dice rolled.")





