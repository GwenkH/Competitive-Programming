import sys

input = sys.stdin.readline

n = int(input())

tree_mass = []

for i in range(n):
    line = int(input())
    tree_mass.append(line)

list_a = []
list_b = []


psum = []
psum.append(tree_mass[0])
sums = []


for i in range(1, len(tree_mass)):
    psum.append(psum[i-1] + tree_mass[i])


q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)


for i in range(q):
    sum = psum[list_b[i]] - psum[list_a[i]-1]
    sums.append(sum)


for x in sums: 
    print(x)

