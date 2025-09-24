"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -10^7 <= k <= 10^7
"""

from collections import defaultdict


def bruteforce(target: int, nums: list[int]) -> int:
    """didnt do it"""
    return 0


def solution(nums: list[int], k: int) -> int:
    prefixes = defaultdict(int)
    prefixes[0] = 1
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num
        need = curr_sum - k
        if need in prefixes:
            count += prefixes[need]
        prefixes[curr_sum] += 1

    return count


if __name__ == "__main__":
    assert solution([-1, 1, 3, -1, 3, 1, 1, 1, 2], 5) == 5
