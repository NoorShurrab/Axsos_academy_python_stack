# 1. Iterate through the list and replace every positive number with the string "big"
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggie_size([-2, 7, -2, 8, -2, 9]))

# 2. Count the total number of positive integers in the list and store that count in the final position of the list.
def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count +=1
    list[len(list)-1] = count
    return list
print(count_positives([-2, 7, 8, -2, 9]))

# 3. calculates the  sum of all numerical elements in the list and returns that sum.
def sum_total(list):
    sum = 0;
    for i in range(len(list)):
        sum += list[i]
    return sum
print(sum_total([2, 3, 5, 8, 9]))

# 4. Calculate the average of all numbers in the list by dividing the total sum by the list length
def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
        average = sum / len(list)
    return average
print(average([1, 2, 3, 4]))

# 5. Determine the total number of elements in list
def length(list):
        count = 0
        for i in list:
            count += 1
        return count
    #return len(list)
print(length([1, 2, 3, 4, 5]))


# 6. Return the lowest value in the list; if the list is empty, return False.
def minimum(list):
    if len(list) == 0:
        return False
    for i in list:
        if i < list[0]:
            list[0] = i
    return list[0]
print(minimum([4, 5, 6, 3]))

# 7. Return the highest value in the list; if the list is empty, return False.
def maximum(list):
    if len(list) == 0:
        return False
    for i in list:
        if i > list[0]:
            list[0] = i
    return list[0]
print(maximum([6, 4, 3, 8]))

# 8. Analyze the list and return a dictionary containing sumTotal, average, minimum, maximum, and length.
def ultimate_analysis(list):
    sum = 0
    for i in list:
        sum += i
        average = sum / len(list)
        if i < list[0]:
            list[0] = i
        if i > list[0]:
            list[0] = i
    return {"sumTotal": sum, "average": average, "minimum": list[0], "maximum": list[0] , "length": len(list)}
print(ultimate_analysis([1, 2, 3, 4, 5]))

# 9. Reverse the order of elements in the list without creating a new list
def reverse_list(list):
    for i in range(0, len(list) // 2):
        list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
    return list
print(reverse_list([1, 2, 3, 4, 5]))