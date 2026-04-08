# 🎯 Two Sum II - Input Array Is Sorted (LeetCode 167)

## 📖 Problem Statement
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers as a 1-based list `[index1, index2]`.

## 💡 Intuition
Since the input array is **sorted**, we can leverage the monotonic property of the sum. Starting from both ends, we can efficiently narrow down the search space:
- If the current sum is **too small**, we need a larger value → move the `left` pointer right.
- If the current sum is **too large**, we need a smaller value → move the `right` pointer left.
- If it matches the `target`, we've found our answer.

## 🛠️ Approach
1. Initialize `left = 0` and `right = len(numbers) - 1`.
2. While `left < right`:
   - Calculate `current_sum = numbers[left] + numbers[right]`.
   - If `current_sum < target`: increment `left`.
   - If `current_sum > target`: decrement `right`.
   - If `current_sum == target`: return `[left + 1, right + 1]` (1-based indexing).
3. The problem guarantees exactly one valid solution, so no fallback is needed.

## 📊 Complexity
| Metric          | Value | Explanation                              |
|-----------------|-------|------------------------------------------|
| ⏱️ Time         | `O(n)`| Each element is visited at most once.    |
| 💾 Space        | `O(1)`| Only two pointers are used.              |

## 💻 Code
```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
