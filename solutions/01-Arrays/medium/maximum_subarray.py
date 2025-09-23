"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


def bruteforce(height: list[int]) -> int:
    """didnt do it"""
    return 0


def solution(nums: list[int]) -> int:
    max_sum = float("-inf")
    curr_sum = 0

    for num in nums:
        if curr_sum <= 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

    return int(max_sum)


def solution_return_indexes(nums: list[int]) -> tuple[int, int, int]:
    max_sum = float("-inf")
    curr_sum = 0
    start_idx = 0
    end_idx = 0
    for i, num in enumerate(nums):
        if curr_sum <= 0:
            start_idx = i
            curr_sum = 0
        curr_sum += num
        if curr_sum > max_sum:
            end_idx = i
            max_sum = curr_sum

    return int(max_sum), start_idx, end_idx


if __name__ == "__main__":
    assert solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution_return_indexes([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == (6, 3, 6)
