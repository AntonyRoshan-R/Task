'''Input
arr:3 2 1 7 5 4
Output
7
Explanation
Second largest among even position elements(1 3 5) is 3
Second largest among odd position element is 4
Thus output is 3+4 = 7
Sample Input
arr:1 8 0 2 3 5 6
Sample Output
8  '''

n = int(input())
a = list(map(int,input().split()))
even = []
odd = []
for i in range (n):
    if i % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

even = sorted(even)
odd = sorted(odd)
print(even[-2] + odd[-2])
