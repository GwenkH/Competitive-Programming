from logging import exception


my_list = [45, 87, 39, 32, 93, 86, 12, 44, 75, 50]
sorted_list = sorted(my_list)

# Display the original (unsorted values)
print("before: ", end="")
for n in my_list:
    print(f"{n} ", end="")
print()

# Exchange sort inner loop here...
"""
marker = 0
for ...  # start from marker + 1
    if marker value is greater...
        # swap the values in the two slots
"""
def exchange_sort(lst: list): #Sorts by putting smallest numbers first
    for marker in range(len(lst)-1): #Starting marker that is compared
        for num in range(marker+1, len(lst)-1): #Every num past the marker is compared to the marker
            if lst[marker] > lst[num]:
                lst[marker], lst[num] = lst[num], lst[marker]

def bubble_sort(lst:list): #Sorts by putting largest numnber last
    for i in range(len(lst)-1): #Number of cycles
        for j in range(len(lst)-1): #Iterating through lst
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def selection_sort(lst:list):
    for marker in range(len(lst)-1): #marker
        min = marker
        for num in range(marker+1, len(lst)): #Cycling through rest of the nums if current minimum is greater than the current item then swap
            if lst[num] < lst[min]:
                min = num
        
        if min!= marker:
            lst[marker], lst[min] = lst[min], lst[marker] #Swaps nums

def binary_search(lst, target): #Lst needs to be sorted
    l = 0
    r = len(lst)
    while l <= r:
        mid = l + r // 2
        print(mid)
        if lst[mid] == target:
            return mid
    
        elif lst[mid] < target:
            l = mid + 1
    
        elif lst[mid] > target: 
            r = mid - 1 
        #if mid not mid-1 and target not in list, mid will always = r (creates infinite loop) or mid will be out of range
    if l > r: #return -1 when num not in list, this occurs once r < l, whole list has been searched
        return -1



search = binary_search(sorted_list, 36)
# selection_sort(my_list)
# bubble_sort(my_list)
# exchange_sort(my_list)

# Display the values again, now after ONE PASS of the exchange sort algorithm.
print("after : ", end="")
for n in sorted_list:
    print(f"{n} ", end="")
print()

print(search)