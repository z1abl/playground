ar = list(range(0,100))
l = 0
r = len(ar)-1
t = 101 #target
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

binary_search()