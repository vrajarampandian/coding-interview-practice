# https://leetcode.com/problems/contains-duplicate/submissions/
# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#  

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

#  

# Constraints:

#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109


class Solution:

    # Time: O(n^2)
    # Memory: O(1)
    def containsDuplicate1(self, nums: List[int]) -> bool:
        # iterate each number and try to find the number in the remaining array
        # if found return True
        # else check all the numers
        # if nothing found finally return False
        pass
    
    # Time: O(n * logn) + O(n)
    # Memory: O(1) (provided that we can perform in-place sorting)
    def containsDuplicate2(self, nums: List[int]) -> bool:
        # sort the input array (O(n*logn))
        # Iterate from second number, check if this is equal to the previous number
        # if equal, return True
        # Otherwise, if nothing found in array finally return False
        pass
    
    
    # Time: O(n)
    # Memory: O(n)
    def containsDuplicate3(self, nums: List[int]) -> bool:
        # create a dict
        # iterate each numbers, for every  number
        # check if the number already exists in the dict
        # if exists return True
        # if not, put the number in to dict
        # finally if nothing found return False
        pass

    # Time: O(n)
    # Memory: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set from the nums array
        # check if length(set) == length(nums)
        # if equal, return False
        # Otherwise return True
        return len(set(nums)) != len(nums)
        

      