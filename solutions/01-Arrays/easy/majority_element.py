"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
"""

from collections import defaultdict


def bruteforce(nums: list[int]) -> int:
    """bruteforce in memory space basically"""
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
        if counts[num] >= len(nums) / 2:
            return num
    return 0


def solution(nums: list[int]) -> int:
    count = 0
    candidate = nums[0]
    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


if __name__ == "__main__":
    assert bruteforce([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution([2, 2, 1, 1, 1, 2, 2]) == 2
