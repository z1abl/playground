import timeit

ar = list(range(0,10000))
l = 0
r = len(ar)-1
t = 77 #target
i = 0

def binary_search(l=l,r=r):
    global i
    i+=1
    m = (l+r)//2
    print(f'l:{l},r:{r},m:{m},i:{i}')
    if l > r:
        print('t is not in the range')
        return
    elif ar[m] == t:
        print(f'found it: {m}')
        return
    elif ar[m] > t:
        binary_search(l=l, r=m-1)
    elif ar[m] < t:
        binary_search(l=m+1, r=r)

# 100 - 0.000103236
# 1000 - 0.000124602
# 10000 - 0.000122547
# 100000 - 0.00019446199

elapsed_time = timeit.timeit(binary_search,number=1)
print(elapsed_time)