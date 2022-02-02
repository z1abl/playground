import random
import timeit

ar = [random.randint(0,i) for i in range(0,10000)]
# ar = [4,2,6,7,9,0,1,5,3,8,6,5]
# print(ar)

def bubble_sort():
    for i in range(0,len(ar)-1):
        for j in range(0,len(ar)-(i+1)):
            if ar[j] > ar[j+1]:
                temp = ar[j+1]
                ar[j+1] = ar[j]
                ar[j] = temp

    print(ar)

# 100 - 0.0013446829999999958
# 1000 - 0.16796927
# 10000 - 12.324815534
# elapsed_time = timeit.timeit(bubble_sort,number=1)
# print(elapsed_time)

def selection_sort():
    for i in range(0,len(ar)-1):
        min = i
        for j in range(i+1,len(ar)):
            if ar[j] < ar[min]:
                min = j
        if i != min:
            temp = ar[min]
            ar[min] = ar[i]
            ar[i] = temp
    print(ar)

# 100 - 0.0025180630618706346
# 1000 - 0.07813125709071755
# 10000 - 6.288507524062879
# elapsed_time = timeit.timeit(selection_sort,number=1)
# print(elapsed_time)

def insertion_sort():
    for i in range(1,len(ar)):
        j = i
        while ar[j] < ar[j-1] and j > 0:
            temp = ar[j]
            ar[j] = ar[j-1]
            ar[j-1] = temp
            j-=1
    print(ar)

# 100 - 0.000914299045689404
# 1000 - 0.12861040199641138
# 10000 - 5.670234284014441
# elapsed_time = timeit.timeit(insertion_sort,number=1)
# print(elapsed_time)


# https://towardsdatascience.com/how-to-implement-merge-sort-algorithm-in-python-4662a89ae48c
def merge_lists(left_sublist,right_sublist):
    i,j = 0,0
    result = []
    #iterate through both left and right sublist
    while i<len(left_sublist) and j<len(right_sublist):
        #if left value is lower than right then append it to the result
        if left_sublist[i] <= right_sublist[j]:
            result.append(left_sublist[i])
            i += 1
        else:
            #if right value is lower than left then append it to the result
            result.append(right_sublist[j])
            j += 1
    #concatenate the rest of the left and right sublists
    print('****initial result****')
    print(f'result:{result}')
    print(f'left_sublist:{left_sublist[i:]}')
    print(f'right_sublist:{right_sublist[j:]}')

    result += left_sublist[i:]
    result += right_sublist[j:]

    print(f'****returned result:{result}')

    return result

def merge_sort(input_list):
    #if list contains only 1 element return it
    if len(input_list) <= 1:
        return input_list
    else:
        #split the lists into two sublists and recursively split sublists
        midpoint = len(input_list)//2
        print(f'left_sublist:{input_list[:midpoint]}')
        left_sublist = merge_sort(input_list[:midpoint])
        print(f'right_sublist:{input_list[midpoint:]}')
        right_sublist = merge_sort(input_list[midpoint:])
        #return the merged list using the merge_list function above
        print(f'merge lists:left_sublist:{left_sublist},right_sublist:{right_sublist}')
        return merge_lists(left_sublist,right_sublist)

# 100 - 0.0003791959024965763
# 1000 - 0.005112813087180257
# 10000 - 0.12110225507058203
# elapsed_time = timeit.timeit(stmt="merge_sort(ar)",number=1,globals=globals())
# print(elapsed_time)



# https://www.educative.io/edpresso/how-to-implement-quicksort-in-python
def quick_sort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    left = quick_sort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = quick_sort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr

# 100 - 0.0003042519965674728
# 1000 - 0.004059301980305463
# 10000 - 0.052230767003493384
# elapsed_time = timeit.timeit(stmt="quick_sort(ar)",number=1,globals=globals())
# print(elapsed_time)