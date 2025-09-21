"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""


def bruteforce(height: list[int]) -> int:
    max_water = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            water = min(height[i], height[j]) * (j - i)
            max_water = max(max_water, water)

    return max_water


def solution(height: list[int]) -> int:
    max_water = 0
    i = 0
    j = len(height) - 1

    while i < j:
        water = min(height[i], height[j]) * (j - i)
        max_water = max(max_water, water)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_water


if __name__ == "__main__":
    assert solution([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
