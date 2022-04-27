// We are given an unsorted array containing n numbers taken from the range 1 to n. 
// The array has some numbers appearing twice, find all these duplicate numbers using constant space.

// Example 1:

// Input: [3, 4, 4, 5, 5]
// Output: [4, 5]
// Example 2:

// Input: [5, 4, 7, 2, 3, 5, 3]
// Output: [3, 5]

const find_all_duplicates = function(nums) {
    duplicateNumbers = [];
    // TODO: Write your code here
    let i = 0;
    while (i < nums.length) {
        if (nums[i] !== i + 1) {
            let supposedIndex = nums[i] - 1;
            if (nums[i] !== nums[supposedIndex]) {
                [nums[i], nums[supposedIndex]] = [nums[supposedIndex], nums[i]]
            } else {
                duplicateNumbers.push(nums[i])
                i++;
            }

        } else {
            i++
        }
    }
    return duplicateNumbers;
};