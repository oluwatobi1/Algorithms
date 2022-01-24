// Given an array of sorted numbers and a target sum, find a pair in the array whose 
// sum is equal to the given target.

// Write a function to return the indices of the two numbers (i.e. the pair) such
//  that they add up to the given target.

// Input: [1, 2, 3, 4, 6], target=6
// Output: [1, 3]
// Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6


const pair_with_target_sum = function(arr, target_sum) {
    // TODO: Write your code here
    if (arr.length == 0) {
        return []
    }
    var startPointer = 0,
        endPointer = arr.length - 1;

    while (startPointer < endPointer) {
        let currSum = arr[startPointer] + arr[endPointer]
        if (currSum === target_sum) {
            return [startPointer, endPointer]
        } else if (currSum > target_sum) {
            endPointer -= 1
        } else if (currSum < target_sum) {
            startPointer += 1
        }
    }
    return [1, -1]
};

console.log(pair_with_target_sum([1, 2, 3, 4, 6], 6));
console.log(pair_with_target_sum([2, 5, 9, 11], 11));
console.log(pair_with_target_sum([], 0));
console.log(pair_with_target_sum([3, 4, 5, 6, 7, 8], 20));