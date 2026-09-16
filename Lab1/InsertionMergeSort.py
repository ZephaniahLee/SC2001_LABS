import random
import time

def insertionSort(arr, left, right):
    comparisons = 0

    for i in range(left + 1, right + 1): #Left and right are for hybridsort
        cur = arr[i]
        j = i - 1
        
        while j >= left: 
            comparisons += 1

            #Shift arr[j] up by one when current number is smaller
            if cur < arr[j]: #Keeps stability by only shifting when cur is strictly smaller than arr[j]
                arr[j+1] = arr[j]
                j -= 1

            else:
                break

        #Finally place current number in "sorted" position
        arr[j+1] = cur

    return comparisons

def mergeSort(arr, left, right):
    #If left = right -> single element array, left cannot be more than right
    if left >= right:
        return 0

    comparisons = 0

    #Take lower mid
    mid = (left + right) // 2

    
    comparisons += mergeSort(arr, left, mid)
    comparisons += mergeSort(arr, mid + 1, right)

    comparisons += merge(arr, left, mid, right)

    return comparisons

def insertionMergeSort(arr, left, right, S):
        #Should never happen if S > 1
        if left >= right:
            return 0

        #If subarray is small enough, use insertion sort
        if right - left + 1 <= S: #+1 to count actual size instead of hops
            return insertionSort(arr, left, right)

        comparisons = 0
    
        #Take lower mid
        mid = (left + right) // 2
    
        
        comparisons += insertionMergeSort(arr, left, mid, S)
        comparisons += insertionMergeSort(arr, mid + 1, right, S)
    
        comparisons += merge(arr, left, mid, right)
    
        return comparisons



def merge(arr, left, mid, right):
    leftArr = arr[left:mid + 1] #mid + 1 because end is exclusive
    rightArr = arr[mid + 1: right + 1] #right + 1 because end is exclusive

    #Left array index
    i = 0

    #Right array index
    j = 0

    #Main array index
    k = left

    comparisons = 0

    #While either array not done
    while (i < len(leftArr)) and (j < len(rightArr)):
        comparisons += 1

        if leftArr[i] <= rightArr[j]: #<= keeps stability by placing first from left first when equal
            arr[k] = leftArr[i]
            i += 1

        else :
            arr[k] = rightArr[j]
            j += 1

        k += 1

    #Left array not done. Place remaining elements in main array.
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    #Right array not done. Place remaning elements in main array.
    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1

    return comparisons


"""
Array Creation
"""

def generateArray(n):
    arr = []

    for i in range(n):
        arr.append(random.randint(0, n - 1))

    return arr

sizes = [
    1000,
    10000,
    100000,
    500000,
    1000000,
    5000000,
    10000000
]

#Storing the arrays in a dictionary for easier access
arrayDict = {}

for n in sizes:
    arrayDict[n] = generateArray(n)

print("All arrays generated.")

#Note: All sorting algorithms are in place. Create a copy of the array when sorting and pass that copy into the sorting function.