import random
import timeit

ar = [random.randint(0,i) for i in range(0,100)]
print(ar)
# ar = [4,2,6,7,1]
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
elapsed_time = timeit.timeit(bubble_sort,number=1)
print(elapsed_time)