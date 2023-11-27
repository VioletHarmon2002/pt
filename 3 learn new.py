length = float(input("Enter the pikeperch length: "))

if length <= 37:
    print(f"The pikeperch is undersized, and it's missing: {(37 - length)} cm to reach the minimum size.")
else:
    print("The pikeperch is of a good size.")

