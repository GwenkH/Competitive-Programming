#Question 1
from re import T


num = int(input())

total = 0
# Running sum
sum = 5

# Divisible by 4
if num % 4 == 0:
    total += 1

# Divisible by 5
if num % 5 == 0:
    total += 1

# Ignore case of divisible by 5
while sum <= num:
    # Add four until creating num divisible by 5
    sum += 4
    if (num-sum) % 5 == 0:
        total += 1

print(total)