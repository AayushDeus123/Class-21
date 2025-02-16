#Play with list
L = [3,5,4,2,8,1,7,6,10,9]
count = 0

for i in (L):
    count += i
print('The sum of all the values is ',count)

avg = count / len(L)
print('The average of all the values is ',avg)

L.sort()
print('The largest number of the values is ',L[0])
print('The smallest number of the values is ',L[-1])