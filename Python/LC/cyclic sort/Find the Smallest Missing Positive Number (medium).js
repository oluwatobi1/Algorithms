// Given an unsorted array containing numbers, find the smallest missing positive number in it.

// Note: Positive numbers start from ‘1’.

// Example 1:

// Input: [-3, 1, 5, 4, 2]
// Output: 3
// Explanation: The smallest missing positive number is '3'
// Example 2:

// Input: [3, -2, 0, 1, 2]
// Output: 4
// Example 3:

// Input: [3, 2, 5, 1]
// Output: 4

const find_first_smallest_missing_positive = function(nums) {
    // TODO: Write your code here
    let i = 0;
    while (i < nums.length) {
        let supposedIndex = nums[i] - 1;
        if (nums[i] > 0 && nums[i] < nums.length && nums[i] !== nums[supposedIndex]) {
            [nums[i], nums[supposedIndex]] = [nums[supposedIndex], nums[i]]
        } else {
            i++;
        }
    };
    console.log(nums)
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== i + 1) {
            return i + 1
        }
    }
    return -1;
};