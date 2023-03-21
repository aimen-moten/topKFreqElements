# Solution to Leetcode 347
# ------------

# Algorithm:
    # create an empty hashMap
    # loop through the hashMap to add all numbers to the hashMap if not already present and increment their counts as seen
    # initialise the return list
    # while k is not 0
        # set a max = 0 
        # loop through each key in the hashMap keys and find the maximum value by comparing the corresponding value with the existing maxValue
            # Note the key of that value as well in another variable
        # after the loop, add that key to our return list
        # set that key's corresponding value to -1 so that it doesn't affect the next maximum
        # decrement k by 1
    # return the return list

# Code:

def topKFrequent(nums: list[int], k: int) -> list[int]:
        res = {}
        for n in nums:
            res[n] = 1 + res.get(n, 0)
        retList = []
        while k > 0:
            maxValue= 0
            maxN= -1
            for n in res.keys():
                if maxValue < res.get(n):
                     maxValue = res.get(n)
                     maxN = n
            retList.append(maxN)
            res[maxN] = -1
            k = k-1
        return retList

print(topKFrequent([1,1,1,2,2,3,3,3,3,3,4,4,4,4,4,4,4,5], 2))