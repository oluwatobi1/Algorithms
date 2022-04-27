// Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive 
// numbers in the array.

// Example 1:

// Input: [3, -1, 4, 5, 5], k=3
// Output: [1, 2, 6]
// Explanation: The smallest missing positive numbers are 1, 2 and 6.
// Example 2:

// Input: [2, 3, 4], k=3
// Output: [1, 5, 6]
// Explanation: The smallest missing positive numbers are 1, 5 and 6.
// Example 3:

// Input: [-2, -3, 4], k=2
// Output: [1, 2]
// Explanation: The smallest missing positive numbers are 1 and 2.

const find_first_k_missing_positive = function(nums, k) {
    missingNumbers = [];
    // TODO: Write your code here
    let min = Number.POSITIVE_INFINITY;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
            min = Math.min(min, nums[i])
        }
    }
    let i = 0;
    while (i < nums.length) {
        let supposedIndex = nums[i] - min;
        if (nums[i] >= min && nums[i] < nums.length + min && nums[i] !== nums[supposedIndex]) {
            [nums[i], nums[supposedIndex]] = [nums[supposedIndex], nums[i]]
        } else {
            i++
        }
    }
    padStart(missingNumbers, nums[0], k)
    console.log(missingNumbers, nums)

    let end = Number.NEGATIVE_INFINITY
    let check = false
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] - min !== i) {

        } else {
            if (check) {
                appendRange(missingNumbers, end + 1, nums[i], k)
            }
            end = Math.max(end, nums[i])
            check = true
        }

    }
    padEnd(missingNumbers, end, k)
    return missingNumbers;
};

function appendRange(arr, start, stop, k) {
    for (let i = start; i < stop; i++) {
        if (arr.length < k) {
            arr.push(i)
        } else {
            break
        }
    }
}

function padStart(arr, start, k) {
    for (let i = 1; i < start; i++) {
        if (arr.length < k) {
            arr.push(i)
        } else {
            break
        }
    }
}

function padEnd(arr, end, k) {
    let i = end + 1;
    while (arr.length < k) {
        arr.push(i)
        i++;
    }
}