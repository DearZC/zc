arr = [7, 4, 3, 67, 34, 1, 8]
n = len(arr)
for i in range(0, n-1):
    for j in range(0, n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)


for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(j,i,i*j),end = ' ')
    print(' ')


class a(object):
    x = 1
    
class b(a):
    pass

class c(a):
    pass

print(a.x, b.x, c.x)
b.x = 2
print(a.x, b.x, c.x)
a.x = 3
print(a.x, b.x, c.x)