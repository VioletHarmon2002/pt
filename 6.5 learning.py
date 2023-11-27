#Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list except
# that all uneven(нечетные) numbers have been removed. For testing, write a main program where you create a list,
# call the function, and then print out both the original as well as the cut-down list.

def remove_odd_integers(list_of_integers):
    even_integers = []
    for number in list_of_integers:
        if number % 2 == 0:
             even_integers.append(number)
    return even_integers


list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result1 = remove_odd_integers(list_of_integers)
print(result1)











