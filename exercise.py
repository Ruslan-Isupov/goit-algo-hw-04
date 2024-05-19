import timeit
import random


def time_counter(func,data):
    start = timeit.default_timer()
    result = func(data[:])
    time_difference = timeit.default_timer() - start
    return "{:.5f}".format(time_difference)


# #Insertion sort 
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >=0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
        data[j+1] = key 
    return data


#Merge sort 
def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Timsort
def sort_data(data):
    data.sort()
    return data
    
def sorted_data(data):
    return sorted(data)


def random_data (n):
    unsorted_data = [random.randint(0, 10) for _ in range(n)]
    return unsorted_data
    

# # The Smallest_data, n=10
data = random_data(10)

# #Small_data, n=100
# data = random_data(100)

# #Medium_data, n=1000
# data = random_data(1000)

# #The Biggest_data, n=10000
# data = random_data(10000)


print("Insertion_sort",time_counter(insertion_sort,data))
print("Merge_sort",time_counter(merge_sort,data))
print("Sorted_data",time_counter(sorted_data,data))
print("Sort_data",time_counter(sort_data,data))

