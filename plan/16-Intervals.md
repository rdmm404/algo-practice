## Intervals

### Study Questions (To Learn Patterns)

#### **1. Merge Intervals**

- **Difficulty:** Medium
- **Description:** Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
- **Reason:** Fundamental interval problem. The core idea is to sort by start times and then iterate, merging overlapping intervals.
- **Focus:** Sorting by start times is key. Maintain a `merged_list`. If the current interval overlaps with the last interval in `merged_list` (current_start <= last_merged_end), update the end of the last merged interval. Otherwise, add the current interval to `merged_list`.

#### **2. Insert Interval**

- **Difficulty:** Medium
- **Description:** You are given an array of non-overlapping `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i`-th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval. Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).
- **Reason:** Involves finding the correct position for `newInterval` and then merging it with any overlapping existing intervals.
- **Focus:** Iterate through `intervals`. Add all intervals that end before `newInterval` starts. Then, merge `newInterval` with all overlapping intervals (current_interval_start <= newInterval_end AND current_interval_end >= newInterval_start). Finally, add remaining intervals.

#### **3. Non-overlapping Intervals**

- **Difficulty:** Medium
- **Description:** Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
- **Reason:** Greedy approach. Sort by end times. Select the interval that finishes earliest, as this leaves the most room for subsequent intervals.
- **Focus:** Sort intervals by their end points. Keep track of the `end_time` of the last selected non-overlapping interval. Iterate through the sorted intervals. If an interval's start time is `>= end_time`, it doesn't overlap; select it and update `end_time`. The count of selected intervals helps determine the minimum to remove.

#### **4. Meeting Rooms**

- **Difficulty:** Easy
- **Description:** Given an array of meeting time `intervals` consisting of start and end times `[[s1,e1],[s2,e2],...]` (`si < ei`), determine if a person could attend all meetings.
- **Reason:** Simple application of sorting. If, after sorting by start times, any meeting starts before the previous one ends, then it's not possible.
- **Focus:** Sort intervals by start times. Iterate and check if `intervals[i].start < intervals[i-1].end`.

#### **5. Meeting Rooms II**

- **Difficulty:** Medium
- **Description:** Given an array of meeting time `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.
- **Reason:** Two common approaches:
  1.  Sort by start times. Use a min-priority queue to store end times of meetings currently in progress.
  2.  Separate start and end times into two arrays, sort them. Use two pointers to track active meetings.
- **Focus:** For PQ method: if current meeting starts after earliest end time in PQ, reuse room (pop PQ). Add current meeting's end time to PQ. Max PQ size is the answer. For two-pointer: if `start[i] < end[j]`, increment room count (new meeting starts before one ends). Else, decrement room count (a meeting ended).

#### **6. Interval List Intersections**

- **Difficulty:** Medium
- **Description:** You are given two lists of closed intervals, `firstList` and `secondList`, where each list of intervals is pairwise non-overlapping and in sorted order. Return the intersection of these two interval lists.
- **Reason:** Two-pointer approach. Compare the current intervals from both lists to find overlaps.
- **Focus:** Use two pointers, `i` for `firstList` and `j` for `secondList`. Calculate `overlap_start = max(firstList[i].start, secondList[j].start)` and `overlap_end = min(firstList[i].end, secondList[j].end)`. If `overlap_start <= overlap_end`, an intersection exists. Advance the pointer of the interval that finishes earlier.

#### **7. Minimum Number of Arrows to Burst Balloons**

- **Difficulty:** Medium
- **Description:** Given an array `points` where `points[i] = [x_start, x_end]`. An arrow shot at `x` bursts all balloons whose `x_start <= x <= x_end`. Find the minimum number of arrows to burst all balloons.
- **Reason:** Greedy approach. Sort balloons by their end coordinates. Shoot an arrow at the end of the first balloon. This arrow bursts this balloon and potentially others. Skip burst balloons and repeat.
- **Focus:** Sort by end points. Keep track of the `arrow_position` (end of the last burst balloon). If a new balloon starts after `arrow_position`, increment arrow count and update `arrow_position` to this new balloon's end.

#### **8. Teemo Attacking**

- **Difficulty:** Easy
- **Description:** Teemo attacks Ashe. Teemo's attack at second `t` will poison Ashe for `duration` seconds, starting from `t` and ending at `t + duration - 1`. If Teemo attacks again before the previous poison effect ends, the timer for it is reset. Given `timeSeries` (sorted attack times) and `duration`, return the total seconds Ashe is poisoned.
- **Reason:** Iterate through attacks. For each attack, the poison duration is either `duration` or `timeSeries[i] + duration - timeSeries[i-1]` if it overlaps with the previous attack's effect.
- **Focus:** Calculate the end time of the previous poison effect. For the current attack, if it starts before the previous poison ends, the added poisoned time is `timeSeries[i] - timeSeries[i-1]`. Otherwise, it's `duration`.

#### **9. Data Stream as Disjoint Intervals**

- **Difficulty:** Hard
- **Description:** Given a data stream input of non-negative integers `a_1, a_2, ..., a_n`, summarize the numbers seen so far as a list of disjoint intervals. Implement the `SummaryRanges` class.
- **Reason:** Involves maintaining a sorted list of disjoint intervals and merging/adjusting them as new numbers arrive. A `TreeMap` or sorted list can be used.
- **Focus:** When a number `val` is added:
  1.  Find intervals `prev` (ends just before `val`) and `next` (starts just after `val`).
  2.  Handle cases: `val` merges `prev` and `next`, `val` extends `prev`, `val` extends `next`, `val` is covered by an existing interval, or `val` forms a new interval.

#### **10. Employee Free Time**

- **Difficulty:** Hard
- **Description:** We are given a list `schedule` of employees, which represents the working time for each employee. Each employee has a list of non-overlapping `Intervals`, sorted. Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
- **Reason:** First, flatten all intervals into a single list and sort them by start times. Then, iterate through this sorted list, merging overlapping/adjacent busy times. The gaps between these merged busy times are the common free times.
- **Focus:** Collect all intervals. Sort them. Merge these intervals to get a timeline of busy periods. Then, find the gaps between these busy periods.

### Practice Questions (To Apply Patterns)

#### **1. Summary Ranges**

- **Difficulty:** Easy
- **Description:** You are given a sorted unique integer array `nums`. Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

#### **2. Missing Ranges**

- **Difficulty:** Easy
- **Description:** You are given an inclusive range `[lower, upper]` and a sorted unique integer array `nums`, where all elements are in the inclusive range. A number `x` is considered missing if `x` is in the range `[lower, upper]` and `x` is not in `nums`. Return the shortest sorted list of ranges that cover every missing number exactly.

#### **3. Can Attend All Meetings** (Same as Meeting Rooms I)

- **Difficulty:** Easy
- **Description:** Given an array of meeting time `intervals` consisting of start and end times, determine if a person could attend all meetings.

#### **4. Car Pooling**

- **Difficulty:** Medium
- **Description:** There is a car with `capacity` empty seats. The vehicle only drives east. You are given `capacity` and an array `trips`. Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or `false` otherwise. (Can be solved by processing events at start/end points of trips).

#### **5. My Calendar I**

- **Difficulty:** Medium
- **Description:** Implement a `MyCalendar` class to store your events. A new event can be added if adding the event will not cause a double booking. Your class will have one method, `book(int start, int end)`.

#### **6. My Calendar II**

- **Difficulty:** Medium
- **Description:** Implement a `MyCalendarTwo` class to store your events. A new event can be added if adding the event will not cause a triple booking.

#### **7. My Calendar III**

- **Difficulty:** Hard
- **Description:** Implement a `MyCalendarThree` class to store your events. A new event can be added if adding the event will not cause a K-booking (i.e., K events are overlapping). `book(start, end)` returns the maximum K-booking after adding the event. (Sweep line algorithm).

#### **8. Add Bold Tag in String**

- **Difficulty:** Medium
- **Description:** Given a string `s` and a list of strings `dict`, you need to add a closed pair of bold tag `<b>` and `</b>` to wrap the substrings in `s` that exist in `dict`. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you should combine them.

#### **9. Range Module**

- **Difficulty:** Hard
- **Description:** A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals `[start, end)`. Implement `addRange`, `queryRange`, and `removeRange`.

#### **10. Find Right Interval**

- **Difficulty:** Medium
- **Description:** You are given an array of `intervals`. For each interval `i`, find a "right" interval `j` such that `start_j >= end_i` and `start_j` is minimized. Return an array of right interval indices. If no such interval exists, store -1.

#### **11. Remove Covered Intervals**

- **Difficulty:** Medium
- **Description:** Given a list of `intervals`, remove all intervals that are covered by another interval in the list. An interval `[a,b)` is covered by `[c,d)` if `c <= a` and `b <= d`. Return the number of remaining intervals.

#### **12. Maximum White Tiles Covered by a Carpet**

- **Difficulty:** Medium
- **Description:** You are given a 2D integer array `tiles` where `tiles[i] = [li, ri]` represents that every tile `j` such that `li <= j <= ri` is white. You are also given an integer `carpetLen`. Return the maximum number of white tiles that can be covered by a carpet of length `carpetLen`. (Sliding window on sorted tile start/end points).

#### **13. Amount of Time for Binary Tree to Be Infected**

- **Difficulty:** Medium
- **Description:** You are given the `root` of a binary tree with unique values, and an integer `start`. At minute `0`, an infection starts from the node with value `start`. Each minute, a node that is already infected can infect its directly connected uninfected neighbors. Return the number of minutes needed for the entire tree to be infected. (Convert tree to graph, then BFS. Not strictly intervals, but graph traversal often involves managing "time" or "distance" which can feel interval-like).

#### **14. Merge Similar Items**

- **Difficulty:** Easy
- **Description:** You are given two 2D integer arrays, `items1` and `items2`, representing two sets of items. Each item `items[i] = [value_i, weight_i]` represents an item with `value_i` and `weight_i`. Merge the two sets of items. The merged items are represented as a 2D array `ret` where `ret[j] = [value_j, weight_j]`. If there are items with the same value, their weights should be summed up. Return `ret` sorted by value.

#### **15. Minimum Interval to Include Each Query**

- **Difficulty:** Hard
- **Description:** You are given a 2D integer array `intervals`, where `intervals[i] = [left_i, right_i]` describes the `i`-th interval, and an integer array `queries`. The answer to the `j`-th query is the size of the smallest interval `i` such that `left_i <= queries[j] <= right_i`. If no such interval exists, the answer is -1. Return an array containing the answers to the queries. (Sort queries and intervals, use a min-heap).

#### **16. Number of Flowers in Full Bloom**

- **Difficulty:** Medium
- **Description:** You are given a 0-indexed 2D integer array `flowers`, where `flowers[i] = [start_i, end_i]` means the `i`-th flower will be in full bloom from `start_i` to `end_i` (inclusive). You are also given a 0-indexed integer array `persons` of distinct integers, where `persons[j]` is the time that the `j`-th person will arrive to see the flowers. Return an integer array `answer` of the same size as `persons`, where `answer[j]` is the number of flowers that are in full bloom when the `j`-th person arrives. (Sweep line or binary search on sorted start/end times).

#### **17. Maximum Population Year**

- **Difficulty:** Easy
- **Description:** You are given a 2D integer array `logs` where `logs[i] = [birth_i, death_i]` indicates the birth and death years of the `i`-th person. The population of some year `x` is the number of people alive during that year. Return the earliest year with the maximum population. (Sweep line / difference array).

#### **18. Corporate Flight Bookings**

- **Difficulty:** Medium
- **Description:** There are `n` flights, and they are labeled from `1` to `n`. You are given an array of flight bookings `bookings`, where `bookings[i] = [first_i, last_i, seats_i]` represents a booking for flights `first_i` through `last_i` (inclusive) with `seats_i` seats reserved for each flight in the range. Return an array `answer` of length `n`, where `answer[i]` is the total number of seats reserved for flight `i + 1`. (Difference array / sweep line).

#### **19. Interval List Intersections** (Practice)

- **Difficulty:** Medium
- **Description:** You are given two lists of closed intervals, `firstList` and `secondList`. Return the intersection of these two interval lists.

#### **20. Non-overlapping Intervals** (Practice)

- **Difficulty:** Medium
- **Description:** Given an array of `intervals`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

This completes the plan for all the requested topics! I hope this comprehensive guide helps you master these coding patterns. Good luck with your preparation!
