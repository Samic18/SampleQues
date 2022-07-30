'''
Given an unsorted integer array, find the smallest missing positive integer in it.

solution1: HASHING
A simple solution would be to search for all positive numbers in the given array, starting from 1. 
The time complexity of this solution is O(n2) since the first missing positive number must lie within the range [1, n+1] in an array of size n.

 SOL2:
The time complexity can be improved using sorting. The idea is to sort the array and perform a linear scan of the sorted array to find the first missing positive number. 
The time complexity of this solution is O(n.log(n)). However, the solution is far from optimal. 
This post provides an overview of some available alternatives to solve this problem in O(n) time.
'''

def findSmallestMissing(nums):
 
    # initialize the set from array elements
    distinct = {*nums}
 
    # return first smallest missing positive number from the set
    index = 1
    while True:
        if index not in distinct:
            return index
        index += 1
 
 
if __name__ == '__main__':
 
    nums = [1, 4, 2, -1, 6, 5]
    print('The smallest missing positive number from the array is',
        findSmallestMissing(nums))
 
 '''
 The idea is to segregate positive and negative numbers. 
 We can easily do this in linear time and constant space using the Quicksort algorithm’s partitioning technique. 
 The idea is to use 0 as a pivot element and make one pass of the partition process. 
 After the partition step, all positive numbers are put together on one side of the array. 
 The idea is to ignore all non-positive elements and process the subarray containing all positive elements, say nums[0, k-1] for pivot index k.

We initially check if the smallest missing number lies in range 1 to k. 
To check whether the smallest missing number lies in range 1 to k, use array elements as index and mark array elements as negative, i.e., 
for each subarray element x, we get the absolute value of the element abs(x) and make the element at index abs(x)-1 negative.

Finally, traverse the subarray once again and find the first index, which has a positive value. 
If a positive number is located at index i, then the smallest missing number is i+1. If no positive is found, then the smallest missing number must be k+1.
'''
def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
 
 
# Linear time routine for partitioning step of Quicksort
def partition(nums):
    pIndex = 0
 
    # each time we find a positive number, `pIndex` is incremented, and
    # that element would be placed before the pivot
    for i in range(len(nums)):
        if nums[i] > 0:        # pivot is 0:
            swap(nums, i, pIndex)
            pIndex += 1
 
    # return index of the first non-positive number
    return pIndex
 
 
# Function to find the smallest missing positive number from an unsorted array
def findSmallestMissing(nums):
 
    k = partition(nums)
 
    # Case 1. The missing number is in range 1 to k
 
    # do for each array element
    for i in range(k):
 
        # get the value of the current element
        val = abs(nums[i])
 
        # make element at index `val-1` negative if it is positive
        if val-1 < k and nums[val-1] >= 0:
            nums[val-1] = -nums[val-1]
 
    # check for missing numbers from 1 to k
    for i in range(k):
        if nums[i] > 0:
            return i + 1
 
    # Case 2. If numbers from 1 to k are present in the array,
    # then the missing number is `k + 1` e.g. [1, 2, 3, 4] —> 5
 
    return k + 1
