import random
import timeit

ar = [random.randint(0,i) for i in range(0,10000)]
# ar = [4,2,6,7,1,0]
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