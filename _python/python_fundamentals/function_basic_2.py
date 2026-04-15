# 1. Generates a list of integers counting down from the given number to 0.
def count_down(num):
    list_count = []
    for i in range(num, -1, -1):
        list_count += [i]
    return list_count
print(count_down(5))

# 2. Prints the first element of a two item list and returns the second element.
def print_and_return(list):
    print(list[0])
    return list[1]
print_and_return([1,2])
print(print_and_return([1,2]))

# 3. Calculates the sum of the list's first value and the total number of elements in the list
def first_plus_length(list):
    for i in range(len(list)):
        return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))

# 4. Creates a new list containing only elements greater than the second value of the original list; returns False if the list has fewer than 2 elements.
def values_greater(list):
    list_greater = []
    if len(list) < 2:
        return False
    for i in range(len(list)):
        if list[i] > list[1]:
            list_greater += [list[i]]
    return list_greater
print(values_greater([1,3,5,7,9]))

# 5. Returns a list of a specific 'size' where every element is the provided 'value'.
def length_value(size, value):
    list_value = []
    for i in range(size):
        list_value += [value]
    return list_value
print(length_value(3, 5))