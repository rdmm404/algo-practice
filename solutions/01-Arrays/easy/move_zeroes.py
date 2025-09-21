"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""


def bruteforce(nums: list[int]) -> None:
    """Bruteforce wouldn't help I think"""


def solution(nums: list[int]) -> None:
    left = 0
    right = left + 1

    if len(nums) < 2:
        return

    while right < len(nums):
        if nums[left] == 0 and nums[right]:
            if nums[right] == 0:
                right += 1
                continue
            nums[left] = nums[right]
            nums[right] = 0

        left += 1
        right += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    solution(nums)
    assert nums == [1, 3, 12, 0, 0, 0]
