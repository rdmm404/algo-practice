"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]



Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""


def bruteforce(nums: list[int]) -> list[int]:
    output = []
    for num in nums:
        output.append(num**2)
    output.sort()
    return output


def solution(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    output = [0] * len(nums)
    out = len(nums) - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            output[out] = left_square
            left += 1
        else:
            output[out] = right_square
            right -= 1

        out -= 1

    return output


if __name__ == "__main__":
    assert solution([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
